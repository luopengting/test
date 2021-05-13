import re

from checkpoint_compare.checkpoint_compare import get_epoch_and_step

FILENAME_REGEX = r'-(?P<epoch>\d+)_(?P<step>\d+)'

ckpt_files = [
    'fast------.ckpt',
    'faster_rcnn-1_100.ckpt',
    'faster_rcnn-0_20.ckpt',
    'faster_rcnn-1_10.ckpt',
    'faster_rcnn-1-30.ckpt',
    'faster_rcnn-1_11-1-1_5.ckpt'
]

ckpt_files = filter(lambda x: re.search(FILENAME_REGEX, x), ckpt_files)
# ckpt_files = sorted(ckpt_files, key=lambda x: get_epoch_and_step(x))
ckpt_files = sorted(ckpt_files, key=get_epoch_and_step)

print(ckpt_files)
