import operator


def num_sort_string(string):
    if len(string) == 0:
        return ""
    num_str_dict = {}
    string_split = string.split(' ')
    for string in string_split:
        for s in string:
            if s.isdigit():
                num_str_dict.update({s: string})
    sort_str_dict = sorted(num_str_dict.items(), key=operator.itemgetter(0))
    return ' '.join([num_str[1] for num_str in sort_str_dict])


# import re
# def order(text):
#     if len(text) == 0: return ""
#     arr = text.split()
#     arr_index=[re.sub('[^\d+]','',each) for each in arr]
#     new_arr=[each[1] for each in sorted(zip(arr_index, arr),key=lambda x:x[0])]
#     return (''.join(new_arr))

# def order(words):
#     return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))

def extract_number(word):
    for l in word:
        if l.isdigit(): return int(l)
    return None


def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))


d = {'lilee': 25, 'wangyan': 21, 'liqun': 32, 'lidaming': 19}
result = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(result)

if __name__ == '__main__':
    string = "4of Fo1r pe6ople g3ood th5e the2"
    result = order(string)
    print(result)
