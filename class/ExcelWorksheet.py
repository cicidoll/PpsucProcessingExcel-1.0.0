import openpyxl
from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from Config import Config

class ExcelWorksheet():
    """ 读取xlsx文件并返回第一个sheet对象 """
    # excel表格中的第一个sheet表格对象
    first_sheet: Worksheet = None

    def __init__(self):
        # 初始化第一个sheet表格对象
        ExcelWorksheet.first_sheet = self.init_first_sheet()
        
    def init_first_sheet(self) -> Worksheet:
        """ 初始化第一个sheet表格对象 """
        # 初始化xlsx对象
        workbook: Workbook = self.init_workbook(self.join_path())
        # 初始化第一个sheet表格名
        first_sheetname: str = self.get_sheetsname(workbook)
        first_sheet: Workbook = self.get_sheet_object(workbook, first_sheetname)
        return first_sheet

    def join_path(self) -> str:
        """ 获取excel表格所在路径 """
        # excel所在文件夹名
        excel_files_path: str = Config.json_data["excel_files_path"]
        # excel文件名
        excel_file_name: str = Config.json_data["excel_file_name"]
        # 当前项目所在的路径
        current_path = Path(".").resolve()
        # 拼接路径
        excel_data_path = str(current_path / excel_files_path / excel_file_name)
        return excel_data_path

    def init_workbook(self, excel_data_path) -> Workbook:
        """ 获取xlsx表格对象 """
        workbook: Workbook = openpyxl.load_workbook(excel_data_path)
        return workbook

    def get_sheetsname(self, workbook: Workbook)-> str:
        """ 获取第一个sheet表格名 """
        first_sheetname: str = workbook.sheetnames[0]
        return first_sheetname

    def get_sheet_object( self,
                          workbook: Workbook,
                          sheetname: str) -> Worksheet:
        """ 返回指定表名的worksheet对象 """
        return workbook[sheetname]