"""
时间和日期的综合小练习
1.计算你的生日比如近30年来(1990-2019)，每年的生日是星期几,统计一下星期几出现的次数比较多
2,生日提醒,距离生日还有几天(距离下次生日还有多少天)

"""
import datetime
from collections import Counter
week_dict = {0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"}

def birth_week(birth):
    """
    :param birth: '06-12'
    :return:
    """
    # 获取生日当天的星期几的列表
    week_list = [(datetime.datetime.strptime(str(year)+'-'+birth, '%Y-%m-%d')).weekday() for year in range(1990, 2020)]
    result = week_dict[Counter(week_list).most_common(1)[0][0]]
    return week_list, result

def notice_birthday(birthday):
    """
    下次生日提醒
    :param birthday: "06-12"
    :return:
    """
    year = datetime.datetime.now().year
    today = datetime.datetime.now()
    # 下次生日的日期
    birthday_next = datetime.datetime.strptime(str(year) + '-' + birthday, '%Y-%m-%d')

    if birthday_next < today: # 如果今年生日已过则取下一年生日的日期
        birthday_next = datetime.datetime.strptime(str(year+1) + '-' + birthday, '%Y-%m-%d')
    days = (birthday_next - today).days
    return '距离您下次生日还有{}天'.format(days)

