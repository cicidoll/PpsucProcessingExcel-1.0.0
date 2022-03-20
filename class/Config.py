from pathlib import Path
from .Utils import load_json

# 当前项目所在的路径
current_path: Path = Path(".").resolve()
# config所在文件夹
config_path: Path = Path('config')
# config文件名
config_file_name: str = "config.json"



class Config:
    """ 读取config.json文件配置基类 """
    # 拼接路径
    config_file_path = str(current_path / config_path / config_file_name)

    # 读取json文件并初始化参数
    json_data: dict = {
        # excel文件相关设置
        "excel_file_config": {
            # excel所在文件夹名
            "excel_file_path": "",
            # excel文件名
            "excel_file_name": ""
        },
        # 建筑楼全称
        "building_lists": [],
        # 分析所有教室是否有课
        "classrooms_is_empty_dict_config":{
            # 分析所有教室是否有课结果的存储路径
            "classrooms_is_empty_dict_path": "data",
            # 分析所有教室是否有课结果的存储文件名
            "classrooms_is_empty_dict_name": "classrooms_is_empty_dict.json"
        },
        # 将教室分类至各教学楼
        "buildings_dicts_config": {
            # 将教室分类至各教学楼的结果存储路径
            "buildings_dicts_path": "",
            # 将教室分类至各教学楼的结果存储文件名
            "buildings_dicts_name": ""
        },
        # 教学楼简称&全称对应
        "classroom_names_dict": {}
    }
    # 初始化数据
    json_data = load_json(config_file_path)

class ExcelFileConfig(Config):
    """ 分析所有教室是否有课的配置 """
    # 带路径的输出文件名
    file_name_with_path: Path = None

    def __init__(self) -> None:
        self.file_name_with_path = self.create_file_name_with_path()

    def create_file_name_with_path(self) -> Path:
        excel_file_config: dict = {
            "excel_file_path": "",
            "excel_file_name": ""
        }
        # 初始化数据
        excel_file_config = Config.json_data["excel_file_config"]
        # 更新路径数据
        file_name_with_path: Path = current_path / excel_file_config["excel_file_path"] / excel_file_config["excel_file_name"]
        return file_name_with_path

class ClassRoomNamesDictConfig(Config):
    """ 教学楼简称&全称对应 """
    classroom_names_dict: dict = {
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
    # 初始化参数
    classroom_names_dict = Config.json_data["classroom_names_dict"]

class ClassroomsIsEmptyDictConfig(Config):
    """ 分析所有教室是否有课的配置 """
    # 带路径的输出文件名
    file_name_with_path: Path = None

    def __init__(self) -> None:
        self.file_name_with_path = self.create_file_name_with_path()

    def create_file_name_with_path(self) -> Path:
        classrooms_is_empty_dict_config: dict = {
            "classrooms_is_empty_dict_path": "",
            "classrooms_is_empty_dict_name": ""
        }
        # 初始化数据
        classrooms_is_empty_dict_config = Config.json_data["classrooms_is_empty_dict_config"]
        # 更新路径数据
        file_name_with_path: Path = current_path / classrooms_is_empty_dict_config["classrooms_is_empty_dict_path"] / classrooms_is_empty_dict_config["classrooms_is_empty_dict_name"]
        return file_name_with_path


class BuildingsDictsConfig(Config):
    """ 将教室分类至各教学楼 """
    # 带路径的输出文件名
    file_name_with_path: Path = None

    def __init__(self) -> None:
        self.file_name_with_path = self.create_file_name_with_path()

    def create_file_name_with_path(self):
        buildings_dicts_config: dict = {
            "buildings_dicts_path": "",
            "buildings_dicts_name": ""
        }
        # 初始化数据
        buildings_dicts_config = Config.json_data["buildings_dicts_config"]
        # 更新路径数据
        file_name_with_path: Path = current_path / buildings_dicts_config["buildings_dicts_path"] / buildings_dicts_config["buildings_dicts_name"]
        return file_name_with_path