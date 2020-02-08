def capitals(string):
    if isinstance(string, str):
    # for index, s in enumerate(string):
        return [index for index, s in enumerate(string) if s.isupper()]
if __name__ == '__main__':
    string = 'CodEW7888889aRs'
    result = capitals(string)
    pass
