import re
from openpyxl.worksheet.worksheet import Worksheet

from .Config import Config, ClassRoomNamesDictConfig, BuildingsDictsConfig
from .ExcelWorksheet import ExcelWorksheet
from .Utils import save_json_file

class GetClassRoomLists():
    """ 获取 所有教室名与教学楼全称对应字典 """
    # 所有教室列表
    classroom_names_list: list = []
    # 所有教室名与教学楼全称对应字典
    buildings_dicts:dict = {}

    def __init__(self) -> None:
        # 获取xlsx表格实例
        excel_Worksheet: ExcelWorksheet = ExcelWorksheet()
        excel_Worksheet_first_sheet: Worksheet = excel_Worksheet.first_sheet
        GetClassRoomLists.buildings_dicts = self.get_buildings_dicts(
            self.get_classroom_names_list(
                excel_Worksheet_first_sheet
            )
        )
        self.save_buildings_dicts()

    def get_classroom_names_list(self, excel_Worksheet_first_sheet: Worksheet) -> list:
        """ 从xlsx实例中提取所有教室 """
        cell: tuple = excel_Worksheet_first_sheet["A"]
        pattern = r'中国人民公安大学'
        # 初始化xlsx表格中提取到的教室列表
        all_classroom_names_list: list = []
        for i in cell:
            if i.value == None or \
                i.value == '' or \
                re.match(pattern, i.value) != None: continue
            all_classroom_names_list.append(i.value)
        return all_classroom_names_list

    def get_buildings_dicts(self, all_classroom_names_list:list) -> dict:
        """ 将所有教室名整理进教学楼全称对应字典 """
        # 获取教学建筑简称与全称的对应
        classroom_names_dict: dict = ClassRoomNamesDictConfig.classroom_names_dict
        # 初始化数据存储
        buildings_dicts: dict = {}
        for classroom in Config.json_data["building_lists"]:
            buildings_dicts.update(
                { classroom: [] }
            )
        # 遍历并存储数据
        classroom_list:list = []
        for classroom in all_classroom_names_list:
            for sub_names_dict in classroom_names_dict.keys():
                pattern = r'' + sub_names_dict + ''
                if re.match(pattern, classroom) is not None:
                    sub_buildings_dicts_value: list = buildings_dicts[
                        classroom_names_dict[sub_names_dict]
                    ]
                    sub_buildings_dicts_value.append(classroom)
                    classroom_list.append(classroom)
                    break
        GetClassRoomLists.classroom_names_list = classroom_list
        return buildings_dicts

    def save_buildings_dicts(self) -> None:
        """ 将所有教室名与教学楼全称对应字典输出为json文件 """
        file_name_with_path = BuildingsDictsConfig().file_name_with_path
        save_json_file(
            file_name_with_path,
            GetClassRoomLists.buildings_dicts
        )