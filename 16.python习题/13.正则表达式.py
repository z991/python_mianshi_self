import re
from re import findall,search

secret_code='hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

content = 'Hello 1234567 is a number. Regex String'
# result = re.match('.*?(\d+).*', content).group(1)
# print(result)
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
# 而re.search匹配整个字符串，直到找到一个匹配
result = re.search('a (\w+)', content).group(1)
print(result)

a='xz123'
b=re.findall('x.',a)

a='xyxy123'
re.findall('x*',a)

re.findall('xx.*xx',secret_code)
Out=['xxIxxfasdjifja134xxlovexx23345sdfxxyouxx']

re.findall('xx.*?xx',secret_code)
Out=['xxIxx', 'xxlovexx', 'xxyouxx']

re.findall('xx(.*?)xx',secret_code)
Out=['I', 'love', 'you']

s2='asdfxxIxx123xxlovexxdfd'

f=re.search('xx(.*?)xx123xx(.*?)xx',s2)

out="<re.Match object; span=(4, 20), match='xxIxx123xxlovexx'>"

re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
Out='love'