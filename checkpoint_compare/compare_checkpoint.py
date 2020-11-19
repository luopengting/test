import collections
import numpy as np
import re


FILENAME_REGEX = r'-(?P<epoch>\d+)_(?P<step>\d+)'

ckpt_files = ['faster_rcnn-1_100.ckpt', 'faster_rcnn-0_20.ckpt', 'faster_rcnn-1_10.ckpt', 'faster_rcnn-1-30.ckpt']
params_dict = [
    {
        'backbone.layer4.2.bn3.moving_variance': np.random.rand(10),
        'moments.backbone.layer4.2.bn3.gamma': np.random.rand(4, 4),
        'moments.rpn_with_loss.rpn_convs_list.0.rpn_conv.weight': np.random.rand(4, 4, 4)
    },
    {
        'backbone.layer4.2.bn3.moving_variance': np.random.rand(10),
        'moments.backbone.layer4.2.bn3.gamma': np.random.rand(4, 4),
        'moments.rpn_with_loss.rpn_convs_list.0.rpn_conv.weight': np.random.rand(4, 4, 4)
    },
    {
        'backbone.layer4.2.bn3.moving_variance': np.random.rand(10),
        'moments.backbone.layer4.2.bn3.gamma': np.random.rand(4, 4),
        'moments.rpn_with_loss.rpn_convs_list.0.rpn_conv.weight': np.random.rand(4, 4, 4)
    }
]


def get_epoch_and_step(ckpt_filename):
    pattern = re.search(FILENAME_REGEX, ckpt_filename)
    if pattern:
        nums = pattern.groupdict()
        return int(nums.get('epoch')), int(nums.get('step'))
    return None, None


if __name__ == "__main__":
    ckpt_files = filter(lambda x: re.search(FILENAME_REGEX, x), ckpt_files)
    sorted_files = sorted(ckpt_files, key=lambda x: get_epoch_and_step(x))

    ops = list()
    for ckpt_params in params_dict:
        for param in ckpt_params:
            if param not in ops:
                ops.append(param)

    data = collections.defaultdict(None)

    metrics = collections.defaultdict(dict)
    for op in ops:
        op_data = []
        for ckpt_params in params_dict:
            op_data.append(ckpt_params.get(op))
        data[op] = op_data

        # calculate diff
        latest_data = op_data[1:]
        oldest_data = op_data[:-1]

        data_diff = np.abs(np.subtract(latest_data, oldest_data))
        metrics[op].update({'direct_diff': np.max(data_diff)})

        avg_latest = np.average(np.abs(latest_data), axis=0)
        avg_oldest = np.average(np.abs(oldest_data), axis=0)
        data_diff_1 = np.abs(avg_latest - avg_oldest) / ((avg_latest + avg_oldest) + 1e-10)
        metrics[op].update({'diff_1': np.max(data_diff_1)})

        # calculate variance
        variance = np.var(op_data, axis=0).reshape(-1)
        sorted_variance = variance[np.argsort(-variance)]
        metrics[op].update({'variance': sorted_variance[:5]})

    for metric, value in metrics.items():
        print(metric, value)
