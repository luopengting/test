from mindinsight.lineagemgr.api.model import filter_summary_lineage

summary_base_dir = "/data/luopengting/summaries/test_lineage_summary_dir_base_ye2w76l4"
condition_keys = ["summary_dir", "lineage_type", "loss_function", "optimizer", "network", "dataset_mark"]
search_condition = {
    # "loss": {
    #     "in": 0.029999999329447746
    # },
    # "epoch": {
    #     "lt": False
    # },
    # "lineage_type": {'lt': "model"},
    # "sorted_name": "dataset_mak",
    # "sorted_type": "descending",
    # "dataset_mark": {
    #     'in': '2'
    # }
    # "device_num": {
    #     "le": "ddddd"
    # },
    # 'batch_size': {
    #     'lt': 2,
    #     'gt': 'xxx'
    # },
    # 'model_size': {
    #     'eq': 222
    # }
}

summary_lineage = filter_summary_lineage(summary_base_dir, search_condition)

print(summary_lineage)
