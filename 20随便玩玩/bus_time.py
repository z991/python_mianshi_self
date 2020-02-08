from optparse import OptionParser

import requests
from bs4 import BeautifulSoup
from dingtalkchatbot.chatbot import DingtalkChatbot


def send_dingding(message):
    """
    利用钉钉推送公交信息
    :param message:
    :return:
    """
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=623a7fdc4d9e037895e4aeeb128de88c19ae32e2f314c4e4142c560bc6a271b9"
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(msg=message, is_at_all=True)


def get_bus_info(options):
    """
    获取实时公交信息
    :param options:  根据不同的传参获取要查询的公交信息
    :return:
    """
    if options.zhuan:  # 查询专89公交信息
        url = "http://www.bjbus.com/home/ajax_rtbus_data.php?act=busTime&selBLine=%E4%B8%9389&selBDir=4706638298751012656&selBStop=4"
        time_range = range(6)
    else:  # 查询379公交信息
        url = "http://www.bjbus.com/home/ajax_rtbus_data.php?act=busTime&selBLine=379&selBDir=4875586505827891750&selBStop=23"
        time_range = range(6)
    response = requests.get(url=url)
    res_json = response.json()
    # 对公交接口返回的结果进行解析并处理
    html = res_json.get("html")
    soup = BeautifulSoup(html, features="lxml")
    str_text = soup.article.text.split()
    min_flag = str_text[-1]
    if min_flag == "分钟":
        if int(str_text[-2]) in time_range:  # 如果公交到达时间满足条件，则发送钉钉信息
            message = f"最近一辆车距离{str_text[0]}还有 {str_text[4]} 站， {str_text[6]} {str_text[7]} {str_text[8]} 分钟"
            send_dingding(message)
    else:
        pass


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--san", action="store_true", dest="san", default=False,
                      help="san-379")
    parser.add_option("-z", "--zhuan", action="store_true", dest="zhuan", default=False,
                      help="zhuan-专89")

    (options, args) = parser.parse_args()
    get_bus_info(options)
