from pathlib import Path
import json

def load_json(file_name_path: str) -> dict:
    """ 读取json文件 """
    try:
        with open(file_name_path,'r',encoding='utf8')as(jsonFile):
            json_data = json.load(jsonFile)
            return json_data
    except Exception as e:
        pass

def save_json_file(file_name_with_path: str, json_data: dict) -> None:
    """ 接收数据并保存为json文件 """
    # 加入 ensure_ascii=False 选项。导出json文件不乱码
    # jsondata = json.dumps(json_data, ensure_ascii=False, separators=(',',':'))
    jsondata = json.dumps(json_data, ensure_ascii=False)
    with open( Path(file_name_with_path), 'w', encoding='utf-8') as write_file:
        write_file.write(jsondata)
        write_file.close()