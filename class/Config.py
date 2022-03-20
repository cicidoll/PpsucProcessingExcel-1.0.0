from pathlib import Path
from Utils import load_json

# 当前项目所在的路径
current_path = Path(".").resolve()


class Config:
    # config文件名
    config_file_name: str = "config.json"
    # 拼接路径
    config_file_path = str(current_path / config_file_name)

    # 读取json文件并初始化参数
    json_data: dict = {
        # excel所在文件夹名
        "excel_files_path": "",
        # excel文件名
        "excel_file_name": "",
        # 建筑楼全称
        "building_lists": []
    }
    # 初始化数据
    json_data = load_json(config_file_path)

class ClassRoomNamesDict:
    # config文件名
    classroom_names_dict_file_name: str = "classroom_names_dict_config.json"
    # 拼接路径
    classroom_names_dict_file_path = str(current_path / classroom_names_dict_file_name)
    json_data: dict = {
        "木励警楼": "",
        "木区阶": "",
        "团育警中楼": "",
        "团育警西楼": "",
        "团铸剑楼": "",
        "团阶": "",
        "团西院": "",
        "战训馆": "",
        "团综合训练馆": "",
        "靶场": "",
        "实验楼": ""
    }
    # 初始化数据
    json_data = load_json(classroom_names_dict_file_path)

class ClassroomsIsEmptyDictConfig:
    # config文件名
    classrooms_is_empty_dict_file_name: str = "classrooms_is_empty_dict_config.json"
    # 拼接路径
    classrooms_is_empty_dict_file_path = str(current_path / classrooms_is_empty_dict_file_name)
    json_data: dict = {
        "classrooms_is_empty_dict_path": "",
        "classrooms_is_empty_dict_name": ""
    }
    # 读取数据
    json_data = load_json(classrooms_is_empty_dict_file_path)
    # 更新路径数据
    json_data.update(
        { "classrooms_is_empty_dict_path": str(
            current_path / json_data["classrooms_is_empty_dict_path"]
        )}
    )