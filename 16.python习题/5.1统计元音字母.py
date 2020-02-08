# def tongji_yuanyin(string):
#     return len([s for s in string if s in ['a','e','i','o','u']])

# def tongji_yuanyin(inputStr):
#     return sum([1 for s in inputStr if s in ['a','e','i','o','u']])

def tongji_yuanyin(inputStr):
    return sum(c in 'aeiou' for c in inputStr)

if __name__ == '__main__':
    string = 'asdfdsdaaaaadffdsd'
    result = tongji_yuanyin(string)
    print(result)