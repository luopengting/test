a = [1, 2, 3]
b = [4, 5, 6]


res_ = {
                "model_lineages": {
                    "metric": {"acc": 0.1234561}
                }
            }
expected_res_ ={
                "model_lineages": {
                    "metric": {"acc": 0.1234562}
                }
            }



def deal_float_for_dict(res, expected_res):
    decimal_num = 5
    for key in res:
        value = res[key]
        expected_value = expected_res[key]
        if isinstance(value, dict):
            deal_float_for_dict(value, expected_value)
        elif isinstance(value, float):
            res[key] = round(value, decimal_num)
            expected_res[key] = round(expected_value, decimal_num)

deal_float_for_dict(res_, expected_res_)

print(res_, expected_res_)
