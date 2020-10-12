import json
import yaml

test_file = open("../yaml_json/test_config.yaml", "r")
# 先将yaml转换为dict格式
generate_dict = yaml.load(test_file, Loader=yaml.FullLoader)
print(generate_dict)
generate_json = json.dumps(generate_dict, sort_keys=False, indent=4, separators=(',', ': '))
print(generate_json)
