import time
import linecache

def cost_time(func):
    def wrap(*args):
        s = time.time()
        func(*args)
        print('Cost:{}'.format(time.time()-s))
    return wrap



# with open('nginx_log_less','a+') as fw: # 打开文件
#     for i in range(1, 30):
#         print(i)
#         fw.write('2019010331835|;0id51NaXIO@sina.com|;79a0ace82f1395944a2f60c0be5c77b2|;171.111.62.101|;|;|;|;GET|;/otsmobile/app/mgs/mgw.htm|;operationType=com.cars.otsmobile.queryLeftTicket&requestData=[{"train_date":"20190403","purpose_codes":"00","from_station":"OSQ","to_station":"ZJZ","station_train_code":"","start_time_begin":"0000","start_time_end":"2400","train_headers":"QB#","train_flag":"","seat_type":"0","seatBack_Type":"","ticket_num":"","dfpStr":"","secret_str":"false.null","app_version":"182","baseDTO":{"check_code":"a24dc99d9c52ead7225fab1b2cae0072","device_no":"XI8Fmk1npbEDAJdN8AwAfK3E","mobile_no":"","user_name":"0id51NaXIO@sina.com","os_type":"i","time_str":"20190318104234","version_no":"4.1.9"}}]&ts=1552876954266&sign=d355f93046d0f4f6828d69d7cdef83f0|;58.216.109.109|;1.1 oudxin109:0 (Cdn Cache Server V2.0)|;|;|;MTPotal/5 CFNetwork/902.2+\n')

log_nginx = {"name": "lgofile201904", "start": 0, "end": 0}


def final_nginx(now_time, start=0):
    """
    :param now_time:
    :param start:
    :return:

    now_time = "20190401190520" 查找的 20190401190400 到 2019 0401 190459
    """
    now_time = now_time[0:11]+'00'
    log_dict = {"name": 'logfil'+now_time, "start": start, "end": start, "now_time": now_time}

    # 判断读取哪个文件
    #TODO 时间判断

    # 根据现在的时间判断上一分钟的时间
    # TODO

    last_time = int(log_dict[now_time]) - 100
    start = log_dict.get("start")
    with open('nginx_log_less','r+') as file:
        for lin in file.readline()[start:]:
            # now_time = "20190401190520" 查找的 20190401190400 到 20190401190459
            if lin[0:13] <= last_time[0:11]+'59':
                start = start + 1
            elif now_time < lin[0:13]:
                break
        log_dict["end"] = start
        return log_dict



#
@cost_time
def read_nginx():
    with open('nginx_log_less','r+') as file:
        for line in file.readline()[60:]:
            if line[0:13] == '2019010331835':
                print(line[0:13])
                time.sleep(1)
            elif line[0:13] == '2019010405835':
                print('ok')
            elif line[0:13] == '2019010406835':
                print('okkk')

if __name__ == '__main__':
    read_nginx()