import collections
import numpy as np
import os
import re

from mindspore.train.serialization import load_checkpoint


FILENAME_REGEX = r'-(?P<epoch>\d+)_(?P<step>\d+)'


def get_epoch_and_step(ckpt_filename):
    pattern = re.search(FILENAME_REGEX, ckpt_filename)
    if pattern:
        nums = pattern.groupdict()
        return int(nums.get('epoch')), int(nums.get('step'))
    return None, None


class CkptMetric:
    def __init__(self, ckpt_dir, device="GPU"):
        if not os.path.exists(ckpt_dir) or not os.path.isdir(ckpt_dir):
            raise ValueError("Please input correct dir path.")
        self._ckpt_dir = ckpt_dir

        if device == "GPU":
            self._dtype = np.float16
        else:
            self._dtype = np.float32

        ckpt_files = []
        for file_name in os.listdir(ckpt_dir):
            if file_name.endswith('.ckpt'):
                ckpt_files.append(file_name)

        ckpt_files = filter(lambda x: re.search(FILENAME_REGEX, x), ckpt_files)
        self.ckpt_files = sorted(ckpt_files, key=lambda x: get_epoch_and_step(x))

        self._params_dict = self._get_params_dict()
        self._ops = self._get_ops()
        self._data = self.organize_data()

    def _get_params_dict(self):
        """"""
        params_dict = []
        for file_name in self.ckpt_files:
            param_dict = dict()
            param_dict_tmp = load_checkpoint(os.path.join(self._ckpt_dir, file_name))
            for key, value in param_dict_tmp.items():
                value = value.asnumpy().astype(self._dtype)
                param_dict.update({key: value})
        return params_dict

    def _get_ops(self):
        ops = list()
        for ckpt_params in self._params_dict:
            for param in ckpt_params:
                if param not in ops:
                    ops.append(param)
        return ops

    def organize_data(self):
        data = collections.defaultdict(None)
        ops = self._ops
        for op in ops:
            op_data = []
            for ckpt_params in self._params_dict:
                if ckpt_params.get(op) is not None:
                    op_data.append(ckpt_params.get(op))
            data[op] = op_data
        return data

    def get_metric_report(self, top=3):
        metrics = collections.defaultdict(dict)
        ops = self._ops
        for op in ops:
            sorted_variance, variance_shape, sorted_index = self._get_top_variance(op, top)
            metrics[op].update({'variance': sorted_variance})

            try:
                data_diff, data_diff_1 = self._cal_diff(op)
                metrics[op].update({'direct_diff': np.max(data_diff)})
                metrics[op].update({'diff_1': np.max(data_diff_1)})
            except ValueError as e:
                metrics[op].update({'error': str(e)})

        self.print_metric(metrics)

    def _cal_diff(self, op_name):
        op_data = self._data.get(op_name)
        if len(op_data) < 2:
            raise ValueError("Length of the data is: %s. Can not calculate diff." % len(op_data))

        # calculate diff
        latest_data = op_data[1:]
        oldest_data = op_data[:-1]

        data_diff = np.abs(np.subtract(latest_data, oldest_data))

        avg_latest = np.average(np.abs(latest_data), axis=0)
        avg_oldest = np.average(np.abs(oldest_data), axis=0)
        data_diff_1 = np.abs(avg_latest - avg_oldest) / ((avg_latest + avg_oldest) + 1e-10)

        return data_diff, data_diff_1

    def _cal_variance(self, op_name):
        op_data = self._data.get(op_name)

        # calculate variance
        variance = np.var(op_data, axis=0)

        return variance

    def _get_top_variance(self, op_name, top=3):
        variance = self._cal_variance(op_name).reshape(-1)
        sorted_index = list(np.argsort(-variance))
        sorted_variance = list(variance[sorted_index])

        return sorted_variance[:top], variance.shape, sorted_index[:top]

    def print_metric(self, metric):
        for metric, value in metric.items():
            value_str = ""
            for name, v in value.items():
                if isinstance(v, list):
                    value_str += " | %s: %20s" % (name, v)
                elif isinstance(v, str):
                    value_str += " | %s: %s" % (name, v)
                else:
                    value_str += " | %s: %0.8f" % (name, v)
            print(metric.ljust(55), value_str)


if __name__ == "__main__":
    gpu_metric = CkptMetric("")
    gpu_metric.get_metric_report()
