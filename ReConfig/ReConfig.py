import json
import os
import yaml
import pytest

# fileYaml = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.yaml']
#
# filePath = os.getcwd()


def get_testCase():

    testcase = []

    for dirpath, dirnames, filenames in os.walk("."):
        for file in filenames:
            if file.endswith("dzm.yaml"):
                testcase.append(os.path.join(dirpath, file))
    print(testcase)
    return testcase



@pytest.mark.parametrize("file", get_testCase())
def load_yaml_Config(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
        content = yaml.load(content, Loader=yaml.FullLoader)
    print(content['dzm_search_base_data'])
    print(type(content))
    return content['dzm_search_base_data']


    # def load_text_Config(self, file):
    #     with open(file) as f:
    #         content = json.dump(f)
    #     return content




def test_Case():
    data = get_testCase()
    return load_yaml_Config(data[0])









