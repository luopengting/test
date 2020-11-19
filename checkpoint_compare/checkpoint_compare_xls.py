import collections
import numpy as np
import os
import re
import xlsxwriter

from mindspore.train.serialization import load_checkpoint


FILENAME_REGEX = r'-(?P<epoch>\d+)_(?P<step>\d+)'


def get_epoch_and_step(ckpt_filename):
    pattern = re.search(FILENAME_REGEX, ckpt_filename)
    if pattern:
        nums = pattern.groupdict()
        return int(nums.get('epoch')), int(nums.get('step'))
    return None, None


class CkptMetric:
    def __init__(self, ckpt_dir, output_dir, device="GPU"):
        self._metrics = ["direct_diff", "diff1", "variance"]
        # if not os.path.exists(ckpt_dir) or not os.path.isdir(ckpt_dir):
        #     raise ValueError("Please input correct dir path.")
        self._ckpt_dir = ckpt_dir

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self._output_dir = output_dir

        if device == "GPU":
            self._dtype = np.float16
        else:
            self._dtype = np.float32

        # ckpt_files = []
        # for file_name in os.listdir(ckpt_dir):
        #     if file_name.endswith('.ckpt'):
        #         ckpt_files.append(file_name)
        from compare_checkpoint import ckpt_files

        ckpt_files = filter(lambda x: re.search(FILENAME_REGEX, x), ckpt_files)
        self.ckpt_files = sorted(ckpt_files, key=lambda x: get_epoch_and_step(x))

        self._params_dict = self._get_params_dict()
        self._parameters = self._get_parameters()
        self._data = self.organize_data()

    def _get_params_dict(self):
        """"""
        # params_dict = []
        # for file_name in self.ckpt_files:
        #     param_dict = dict()
        #     param_dict_tmp = load_checkpoint(os.path.join(self._ckpt_dir, file_name))
        #     for key, value in param_dict_tmp.items():
        #         value = value.asnumpy().astype(self._dtype)
        #         param_dict.update({key: value})
        from compare_checkpoint import params_dict
        return params_dict

    def _get_parameters(self):
        parameters = list()
        for ckpt_params in self._params_dict:
            for param in ckpt_params:
                if param not in parameters:
                    parameters.append(param)
        return parameters

    def organize_data(self):
        data = collections.defaultdict(None)
        parameters = self._parameters
        for op in parameters:
            op_data = []
            for ckpt_params in self._params_dict:
                if ckpt_params.get(op) is not None:
                    op_data.append(ckpt_params.get(op))
            data[op] = op_data
        return data

    def _prepare_for_diff(self, op_name):
        op_data = self._data.get(op_name)
        if len(op_data) < 2:
            raise ValueError("Length of the data is: %s. Can not calculate diff." % len(op_data))

        # calculate diff
        later_data = op_data[1:]
        older_data = op_data[:-1]

        if older_data[0].shape != later_data[0].shape:
            raise ValueError(
                "Numbers of parameters is not equal: %s, %s." % (older_data[0].shape, later_data[0].shape))

        return older_data, later_data

    def _cal_direct_diff(self, op_name):
        older_data, later_data = self._prepare_for_diff(op_name)
        data_diff = np.abs(np.subtract(later_data, older_data))

        return data_diff

    def _cal_diff1(self, op_name):
        older_data, later_data = self._prepare_for_diff(op_name)
        avg_latest = np.average(np.abs(later_data), axis=0)
        avg_oldest = np.average(np.abs(older_data), axis=0)
        data_diff = np.abs(avg_latest - avg_oldest) / ((avg_latest + avg_oldest) + 1e-10)

        return data_diff

    def _cal_variance(self, op_name):
        op_data = self._data.get(op_name)
        # calculate variance
        variance = np.var(op_data, axis=0)

        return variance

    def _get_metric(self, param_key, metric_name):
        if metric_name == "direct_diff":
            return self._cal_direct_diff(param_key)
        elif metric_name == "diff1":
            return self._cal_diff1(param_key)
        else:
            return self._cal_variance(param_key)

    def print_metric(self, metric, report_file):
        report_file = os.path.join(self._output_dir, report_file)
        if os.path.exists(report_file):
            os.remove(report_file)
        for metric, value in metric.items():
            value_str = ""
            for name, v in value.items():
                if isinstance(v, list):
                    value_str += " | %s: %20s" % (name, v)
                elif isinstance(v, str):
                    value_str += " | %s: %s" % (name, v)
                else:
                    value_str += " | %s: %0.8f" % (name, v)
            with open(report_file, "a") as f:
                print(metric.ljust(55), value_str, file=f)
        print("Write metric ended.")

    def _get_sorted_index(self, value, top=3):
        value = value.reshape(-1)
        top = min(top, value.shape[0])
        sorted_index = np.argsort(-value).tolist()[:top]
        return value, sorted_index

    def metric_report(self, report_file_name, metrics=None, top=3):
        if metrics is None:
            metrics = self._metrics
        if not set(metrics).issubset(self._metrics):
            raise ValueError("Metrics should be in %s." % self._metrics)

        report_file = os.path.join(self._output_dir, report_file_name + '.xlsx')
        if os.path.exists(report_file):
            os.remove(report_file)

        workbook = xlsxwriter.Workbook(report_file)

        source_worksheet = workbook.add_worksheet("source")
        source_worksheet.set_column(1, 1, 140)
        source_worksheet.set_row(1, 50)
        source_info = {
            'ckpt_dir': os.path.realpath(self._ckpt_dir),
            'ckpt_files': '\n'.join(self.ckpt_files)
        }
        for row, key in enumerate(source_info):
            source_worksheet.write(row, 0, key)
            source_worksheet.write(row, 1, source_info.get(key))

        detail_worksheet = workbook.add_worksheet("detail")
        detail_worksheet.set_column(0, 0, 55)
        detail_worksheet.set_column(1, len(metrics), 20)
        detail_columns = metrics
        for col, metric_name in enumerate(detail_columns):
            detail_worksheet.write(0, col + 1, metric_name)

        metrics_value = dict()

        row = 1
        for key in self._parameters:
            metrics_value[key] = dict()
            detail_worksheet.write(row, 0, key)
            for metric_name in metrics:
                value = self._get_metric(key, metric_name)
                if metric_name == "variance":
                    value, sorted_index = self._get_sorted_index(value, top)
                    metrics_value[key].update({metric_name: value})
                    value = value[sorted_index]
                else:
                    metrics_value[key].update({metric_name: value})
                    value = np.max(value)
                col = detail_columns.index(metric_name) + 1

                if isinstance(value, (list, np.ndarray)):
                    value = ",".join([str(v) for v in value])
                detail_worksheet.write(row, col, value)
            row += 1
        workbook.close()
        print("Write metric ended.")


def variance_compare(variance_dict1, variance_dict2, report_file):
    # base on variance1
    if os.path.exists(report_file):
        os.remove(report_file)
    f = open(report_file, "a")
    for op, value1 in variance_dict1.items():
        if op not in variance_dict2:
            print(op, "not in dict2.", file=f)
        value2 = variance_dict2.get(op)

        variance1, sorted_index1 = value1
        variance2, sorted_index2 = value2
        if variance1.shape != variance2.shape:
            print(op, "Their shape is not equal: %s, %s." % (variance1.shape, variance2.shape), file=f)

        print(op.ljust(55), ": ", variance1.reshape(-1)[sorted_index1], variance2.reshape(-1)[sorted_index2], file=f)

    f.close()


def variance_compare_output_xls(variance_dict1, variance_dict2, report_file):
    report_file = report_file + ".xlsx"
    # base on variance1
    if os.path.exists(report_file):
        os.remove(report_file)
    f = open(report_file, "a")
    for op, value1 in variance_dict1.items():
        if op not in variance_dict2:
            print(op, "not in dict2.", file=f)
        value2 = variance_dict2.get(op)

        variance1, sorted_index1 = value1
        variance2, sorted_index2 = value2
        if variance1.shape != variance2.shape:
            print(op, "Their shape is not equal: %s, %s." % (variance1.shape, variance2.shape), file=f)

        print(op.ljust(55), ": ", variance1.reshape(-1)[sorted_index1], variance2.reshape(-1)[sorted_index2], file=f)

    f.close()


if __name__ == "__main__":
    output_dir = "./result"
    gpu_metric = CkptMetric("./gpu_step100_momentum", output_dir)
    gpu_variance_dict = gpu_metric.metric_report("gpu_step100_momentum")

    # dchip_metric = CkptMetric("./dchip_step100_momentum", output_dir)
    # dchip_variance_dict = dchip_metric.get_metric_report("dchip_step100_momentum")
    #
    # variance_compare_output_xls(gpu_variance_dict, dchip_variance_dict,
    #                             os.path.join(output_dir, "dchip_variance_based_on_gpu.variance"))
    # variance_compare_output_xls(dchip_variance_dict, gpu_variance_dict,
    #                             os.path.join(output_dir, "gpu_variance_based_on_dchip.variance"))
