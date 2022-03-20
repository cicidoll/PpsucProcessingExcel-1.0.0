import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from .Config import ExcelFileConfig

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
        workbook: Workbook = self.init_workbook(ExcelFileConfig().file_name_with_path)
        # 初始化第一个sheet表格名
        first_sheetname: str = self.get_sheetsname(workbook)
        first_sheet: Workbook = self.get_sheet_object(workbook, first_sheetname)
        return first_sheet


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