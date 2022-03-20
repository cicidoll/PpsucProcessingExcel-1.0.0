from Class.GetClassRoomLists import GetClassRoomLists
from Class.QueryClassroomIsEmpty import QueryClassroomIsEmpty

def main():
    # 获取 所有教室名与教学楼全称对应字典
    GetClassRoomLists()
    # 分析所有教室列表的有无课情况
    QueryClassroomIsEmpty()

if __name__ == "__main__":
    main()