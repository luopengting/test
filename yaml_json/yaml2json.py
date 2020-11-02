import json
import yaml


def read_yaml(file_path):
    test_file = open(file_path, "r")
    # 先将yaml转换为dict格式
    generate_dict = yaml.load(test_file, Loader=yaml.FullLoader)
    print(generate_dict)
    generate_json = json.dumps(generate_dict, sort_keys=False, indent=4, separators=(',', ': '))
    print(generate_json)
    return generate_dict


if __name__ == "__main__":
    file_path = "../yaml_json/test_config.yaml"
    read_yaml(file_path)
