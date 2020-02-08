import itchat
from collections import Counter

itchat.auto_login(hotReload=True)

# roomslist = itchat.get_chatrooms()
# print(roomslist)
#群名称
itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
# myroom=itchat.search_chatrooms(name=u'5.25野狼户外紫荆关漂流')
# print(myroom)
myroom=itchat.search_chatrooms(name=u'帅张球友群-北京分队')
gsq=itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)
# for g in gsq['MemberList']:
#     print(g)
nick_list = [g["DisplayName"] for g in gsq['MemberList'] if "测试" in g["DisplayName"]]
# sex_list = (g["Sex"] for g in gsq['MemberList'])
# cont = Counter(sex_list)
# print(cont)
# city_list = (g["City"] for g in gsq["MemberList"])
# pro_list = (g["Provience"] for g in gsq["MemberList"])
print(nick_list)
print(len(nick_list))