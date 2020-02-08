def get_middle(s):
    return s[(len(s)-1)//2: len(s)//2+1]

if __name__ == '__main__':
    s = 'testingqwertyuiop['
    print(len(s))
    result = get_middle(s)
    print(result)