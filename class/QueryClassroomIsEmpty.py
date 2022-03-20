from openpyxl.worksheet.worksheet import Worksheet

from .ExcelWorksheet import ExcelWorksheet
from .GetClassRoomLists import GetClassRoomLists
from .Config import ClassroomsIsEmptyDictConfig
from .Utils import save_json_file

class QueryClassroomIsEmpty:
    """ 分析所有教室列表的有无课情况 """
    # 初始化存储
    classrooms_is_empty_dict: dict = {}

    def __init__(self) -> None:
        self.get_classrooms_is_empty_dict()
        self.save_classrooms_is_empty_dict()

    def get_classrooms_is_empty_dict(self):
        """ 分析表格数据 """
        # 载入xlsx对象类
        excel_worksheet: Worksheet = ExcelWorksheet().first_sheet
        classroom_names_list = GetClassRoomLists().classroom_names_list
        # 获取A列数据
        cell: tuple = excel_worksheet["A"]
        # 开始遍历所有教室
        for sub_classroom in classroom_names_list:
            for i in cell:
                if i.value == sub_classroom:
                    # 获取当前教室所在xlsx表格中的行、列
                    column, row = i.column, i.row
                    break
            # 对是否有课进行分析(1:有课 0:无课)
            sub_is_empty_list: list = []
            for sub in excel_worksheet[row][1:36]:
                if sub.value == '':
                    sub_is_empty_list.append(0)
                elif sub.value != '':
                    sub_is_empty_list.append(1)
            # 更新分析结果至类变量
            QueryClassroomIsEmpty.classrooms_is_empty_dict.update(
                {sub_classroom: sub_is_empty_list}
            )

    def save_classrooms_is_empty_dict(self) -> None:
        """ 将分析后的数据保存为json """
        file_name_with_path = ClassroomsIsEmptyDictConfig().file_name_with_path
        save_json_file(
            file_name_with_path,
            QueryClassroomIsEmpty.classrooms_is_empty_dict
        )