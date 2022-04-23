from interval import Interval

from .Utils import save_json_file
from .Utils import load_json
from .Config import ClassroomsIsEmptyDictConfig, ProcessIsEmptyJsonConfig

class ProcessIsEmptyJson:
    """ 处理QueryClassroomIsEmpty导出的json文件
        得到根据周几和时间段分类的排课表
    """

    # 从Config类中获取[QueryClassroomIsEmpty]导出的带路径文件名
    classrooms_is_empty_dict_name_with_path = ClassroomsIsEmptyDictConfig().file_name_with_path

    # 从Config类中获取[细分时间段排课表]导出的带路径文件名
    process_is_empty_json_name_with_path, other_classrooms_json_name_with_path = ProcessIsEmptyJsonConfig().file_name_with_path

    def __init__(self) -> None:
        process_data_dict, other_classrooms_data_dict = self.process_json()
        self.save_data(
            process_data_dict,
            other_classrooms_data_dict
        )

    def process_json(self):
        """ 处理数据 """
        # 获取classrooms_is_empty_json数据
        classrooms_is_empty_dict: dict = load_json(ProcessIsEmptyJson.classrooms_is_empty_dict_name_with_path)
        # 教室名列表
        classrooms_name_list: list = list(classrooms_is_empty_dict.keys())
        # 时间段选择器
        time_list: list = ['am12', 'am34', 'pm12', 'pm34', 'pm56']
        # 导出时间表排课数据
        process_data_dict: dict = {
            'day1': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day2': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day3': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day4': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day5': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day6': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            },
            'day7': {
                'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
            }
        }
        # 导出教室特定教学周数据
        other_classrooms_data_dict: dict = {}
        # -----------------------------
        # 开始处理数据

        # 定义 周几数值区间处理字典
        def day_in_interval(sub):
            # 定义区间判定字典
            interval_dict: dict = {
                Interval(0, 4) : 'day1',
                Interval(5, 9) : 'day2',
                Interval(10, 14) : 'day3',
                Interval(15, 19) : 'day4',
                Interval(20, 24) : 'day5',
                Interval(25, 29) : 'day6',
                Interval(30, 34) : 'day7'
            }
            for key in interval_dict.keys():
                if sub in key:
                    return interval_dict.get(key, 'error')

        for key, value in classrooms_is_empty_dict.items():
            # 记录细分教学周的额外排课数据
            other_classroom_data: list = []
            for sub_result_index in range(len(value)):
                # 获取当前遍历的排课判断是在周几哪个时间段
                sub_day = day_in_interval(sub_result_index)
                sub_time = time_list[sub_result_index % 5]
                

                if value[sub_result_index] == '1':
                    continue
                elif value[sub_result_index] == '0':
                    process_data_dict[sub_day][sub_time].append(key)
                elif value[sub_result_index] != '1' and value[sub_result_index] != '0':
                    other_classroom_data.append(
                        { 
                            'day': sub_day,
                            'time': sub_time,
                            'week': value[sub_result_index]
                        }
                    )
            other_classrooms_data_dict.update(
                {key: other_classroom_data}
            )
        # ---------------------------------
        return process_data_dict, other_classrooms_data_dict

    def save_data(self, process_data_dict, other_classrooms_data_dict) -> None:
        # 导出为json文件
        save_json_file(
            ProcessIsEmptyJson.process_is_empty_json_name_with_path,
            process_data_dict
        )
        save_json_file(
            ProcessIsEmptyJson.other_classrooms_json_name_with_path,
            other_classrooms_data_dict
        )