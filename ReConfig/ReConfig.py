import json
import os
import yaml
import pytest

# fileYaml = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.yaml']
#
# filePath = os.getcwd()


def get_config_path():

    yamlConfig = []
    cookieConfig = []
    for dirpath, dirnames, filenames in os.walk("."):
        for file in filenames:

            if file.endswith(".yaml"):
                yamlConfig.append(os.path.join(dirpath, file))

            if file.endswith(".txt"):
                cookieConfig.append(os.path.join(dirpath, file))
    # print(yamlConfig, '/n', cookieConfig)

    return yamlConfig, cookieConfig


def Case():
    data, _ = get_config_path()
    return data


@pytest.mark.parametrize("file", Case())
def load_yaml_Config():
    files = Case()
    for file in files:
        with open(file, encoding='utf-8') as f:
            content = f.read()
            content = yaml.load(content, Loader=yaml.FullLoader)
    print(content)
    return content


    # def load_text_Config(self, file):
    #     with open(file) as f:
    #         content = json.dump(f)
    #     return content



def test_001():

    load_yaml_Config()












