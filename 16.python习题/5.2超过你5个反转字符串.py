def fanzhuan_5(string):
    str_list = string.split(' ')
    return ' '.join([s[::-1] if len(s)>5 else s for s in str_list])

import re
def spin_words(sentence):
    return re.sub(r"\w{5,}", lambda w:w.group(0)[::-1], sentence)

if __name__ == '__main__':
    string = 'Hey fellow warriors'
    result = spin_words(string)
    print(result)
