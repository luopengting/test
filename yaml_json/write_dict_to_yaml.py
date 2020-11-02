import os
import yaml


def generate_yaml(config_dict, yaml_file):

    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(config_dict, file)
    file.close()


config_dict = {
        'summary_base_dir': '/home/summaries',
        'name': ['a', 'b'],
        'parameters': {
            'learning_rate': {
                'bounds': [0.001, 0.002],
                'type': 'int'
            },
            'batch_size': {
                'choice': [16, 32, 64]
            }
        }
    }

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "generated.yaml")
generate_yaml(config_dict, yaml_path)

from yaml_json.yaml2json import read_yaml

new_config_dict = read_yaml(yaml_path)

assert config_dict == new_config_dict
