# from interval import Interval

list1 = list(range(1, 36))

# def test(sub):

#     test_dict: dict = {
#         Interval(1, 5) : '111',
#         Interval(6, 10) : '222',
#         Interval(11, 15) : '333',
#         Interval(16, 20) : '444',
#         Interval(21, 25) : '555',
#         Interval(26, 30) : '666',
#         Interval(31, 35) : '777',

#     }

#     for key in test_dict.keys():
#         if sub in key:
#             return test_dict.get(key, 'error')


# for i in list1:
#     print(test(i))
# sub_day = "day1"
# time_interval_data: dict = {
#     'am12': [], 'am34': [], 'pm12': [], 'pm34': [], 'pm56': []
# }

# temp_data_dict = {
#     sub_day: time_interval_data
# }

# print(temp_data_dict)

list2: list = ['am12', 'am34', 'pm12', 'pm34', 'pm56']

for index in range(len(list1)):
    sub_result = index % 5
    print(list2[sub_result])