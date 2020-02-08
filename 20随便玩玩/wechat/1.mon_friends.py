from wxpy import *
from collections import defaultdict, Counter
from pyecharts.charts import Pie
import time


bot = Bot(cache_path=True)


def get_friends(friends):
    """
    解析每个好友的具体信息
    :param friends:
    :return:
    """
    all_friends = []
    for friend in friends:
        my_friend = defaultdict(lambda: '')
        my_friend['sex'] = friend.sex
        my_friend['name'] = friend.name
        my_friend['city'] = friend.city
        my_friend['province'] = friend.province
        my_friend['is_friend'] = friend.is_friend
        all_friends.append(my_friend)
    return all_friends

def stat_friends_sex(my_friends):
    """
    过滤好友的性别并统计
    :param my_friends:
    :return:
    """
    print("start statistic all friends sex ...")
    sex_infos = [f['sex'] for f in my_friends]
    return Counter(sex_infos)


def show(stat_sexs, my_friends):
    """
    用pyecharts进行统计
    :param stat_sexs:
    :return:
    """
    attr = ["男", "女", "未知"]
    v1 = [stat_sexs[1], stat_sexs[2], stat_sexs[0]]
    pie = Pie("微信{}好友男女比例".format(len(my_friends)))
    pie.add("", attr, v1, is_label_show=True)
    pie.render()


start = time.time()
print("Get all the friends..,.")
friends = bot.friends()
my_friends = get_friends(friends)
print("Total have {}, cost time {}".format(len(my_friends), time.time()-start))
show(stat_friends_sex(my_friends), my_friends)