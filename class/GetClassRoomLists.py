import re
from openpyxl.worksheet.worksheet import Worksheet

from Config import Config, ClassRoomNamesDict
from ExcelWorksheet import ExcelWorksheet

class GetClassRoomLists():
    """ 获取 所有教室名与教学楼全称对应字典 """
    # 获取xlsx表格实例
    excel_Worksheet: ExcelWorksheet = ExcelWorksheet()
    excel_Worksheet_first_sheet: Worksheet = excel_Worksheet.first_sheet
    # 所有教室名与教学楼全称对应字典
    buildings_dicts:dict = {}

    def __init__(self) -> None:
        GetClassRoomLists.buildings_dicts = self.get_buildings_dicts(
            self.get_classroom_names_list(
                GetClassRoomLists.excel_Worksheet_first_sheet
            )
        )

    def get_classroom_names_list(self, excel_Worksheet_first_sheet: Worksheet) -> list:
        """ 从xlsx实例中提取所有教室 """
        cell: tuple = excel_Worksheet_first_sheet["A"]
        pattern = r'中国人民公安大学'
        # 初始化xlsx表格中提取到的教室列表
        classroom_names_list: list = []
        for i in cell:
            if i.value == None or \
                i.value == '' or \
                re.match(pattern, i.value) != None: continue
            classroom_names_list.append(i.value)
        return classroom_names_list

    def get_buildings_dicts(self, classroom_names_list:list) -> dict:
        """ 将所有教室名整理进教学楼全称对应字典 """
        # 获取教学建筑简称与全称的对应
        classroom_names_dict: dict = ClassRoomNamesDict.json_data
        # 初始化数据存储
        buildings_dicts: dict = {}
        for classroom in Config.json_data["building_lists"]:
            buildings_dicts.update(
                { classroom: [] }
            )
        # 遍历并存储数据
        for classroom in classroom_names_list:
            for sub_names_dict in classroom_names_dict.keys():
                pattern = r'' + sub_names_dict + ''
                if re.match(pattern, classroom) is not None:
                    sub_buildings_dicts_value: list = buildings_dicts[
                        classroom_names_dict[sub_names_dict]
                    ]
                    sub_buildings_dicts_value.append(classroom)
                    break

        return buildings_dicts