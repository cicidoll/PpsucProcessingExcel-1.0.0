import json

def load_json(file_name_path: str) -> dict:
    """ 读取json文件 """
    try:
        with open(file_name_path,'r',encoding='utf8')as(jsonFile):
            json_data = json.load(jsonFile)
            return json_data
    except Exception as e:
        pass