from wxpy import *

bot = Bot(cache_path=True)
print("启动机器人。。。。。")


# 监控所有群
@bot.register(chats=Group)
def auto_monitor_group(msg):
    """
    监听所有的群的的消息
    :param msg:
    :return:
    """
    print('\n群里有消息')
    # 出现红包
    if msg.type == 'Note' and '红包' in msg.text:
        notice_hongbao(msg, notice_person='leoxin')

    # 普通消息
    elif msg.type == 'Text':
        forward_text_msg(msg, person_in_group='123', notice_person_name='leoxin')

def forward_text_msg(msg, person_in_group='123', notice_person_name='leoxin'):
    print('马上转消息...')
    # 转发给某人
    group = ensure_one(bot.groups().search(person_in_group))
    notice_person = ensure_one(group.search(notice_person_name))

    res = None
    prefix_text=''
    if msg.member.name == notice_person_name:
        prefix_text = '群{}:中的老板:{} 发消息了:'.format(msg.chat.name, msg.member.name)
    else:
        prefix_text = '群{}:中的其他人:{} 发消息了:'.format(msg.chat.name, msg.member.name)
    print(prefix_text)
    res = msg.forward(notice_person, prefix=prefix_text)
    print('发送成功\n') if res else print('发送失败\n')


def notice_hongbao(msg, notice_person=''):
    """
    抢红包提醒，如果有需要指定的提醒人,则发给他，若没有则发给文件助手
    :param msg:
    :param notice_person:
    :return:
    """
    print("提醒红包...")
    group_name = msg.chat.name
    text = '群:{} 发红包啦,快抢'.format(group_name)
    print('text')
    if notice_person:
        friend = bot.friends().search(notice_person)[0]
        [friend.send(text) for i in range(3)]
    else:
        [bot.file_helper.send(text) for i in range(3)]
