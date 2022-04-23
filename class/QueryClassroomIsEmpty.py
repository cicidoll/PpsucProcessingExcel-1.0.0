import re
from unittest import result
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
                    sub_is_empty_list.append('0')
                elif sub.value != '':
                    reg_result = self.reg_str(sub.value)
                    sub_is_empty_list.append(reg_result)
            # 更新分析结果至类变量
            QueryClassroomIsEmpty.classrooms_is_empty_dict.update(
                {sub_classroom: sub_is_empty_list}
            )

    def reg_str(self, input_string: str):
        ''' 判断当前教学周 '''
        pattern_1 = re.compile(r'\d{1,2}-\d{1,2}\n')
        if re.search(pattern_1, input_string) is not None:
            result = ''
            re_search_lists = list(set(pattern_1.findall(input_string)))
            lists_len = len(re_search_lists)
            for index in range(lists_len):
                sub_find = re_search_lists[index]
                # 记录教学周的分隔符
                split_str = '、' if lists_len > 1 and index < (lists_len-1) else ''
                sub_result: str = sub_find.strip('\n') + split_str
                result += sub_result
        else:
            result = '1'
        return result

    def save_classrooms_is_empty_dict(self) -> None:
        """ 将分析后的数据保存为json """
        file_name_with_path = ClassroomsIsEmptyDictConfig().file_name_with_path
        save_json_file(
            file_name_with_path,
            QueryClassroomIsEmpty.classrooms_is_empty_dict
        )