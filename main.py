from Class.GetClassRoomLists import GetClassRoomLists
from Class.QueryClassroomIsEmpty import QueryClassroomIsEmpty
from Class.ProcessIsEmptyJson import ProcessIsEmptyJson

def main():
    # 获取 所有教室名与教学楼全称对应字典
    GetClassRoomLists()
    # 分析所有教室列表的有无课情况
    QueryClassroomIsEmpty()
    # 处理上一步导出的排课表,分析得出具体时间段的排课表
    ProcessIsEmptyJson()


if __name__ == "__main__":
    main()