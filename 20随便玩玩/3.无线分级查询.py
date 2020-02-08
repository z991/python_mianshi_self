
def test2(a,*args,**kwargs):
    c = args[0]
    print(c)
    d = kwargs
    print(d)
    return "ok"

def test_1(a, func, *args, **kwargs):
    func(a, *args, **kwargs)

lists = [
    {'id':1, 'title':'t1', 'parent_id':0},
    {'id':2, 'title':'t2', 'parent_id':0},
    {'id':3, 'title':'t1_1', 'parent_id':1},
    {'id':4, 'title':'t1_2', 'parent_id':1},
    {'id':5, 'title':'t1_2_1', 'parent_id':4},
    {'id':6, 'title':'t2_1', 'parent_id':5},
]

def dg_list(list):
    res = {}
    for ld in list:
        ld.setdefault("children", [])
        res[ld['id']] = ld
        if ld['parent_id'] in res:
            res[ld['parent_id']]['children'].append(ld)
    # for c in res:
    #     if not res[c]['children']:
    #         res[c].pop("children")

    value = [v for v in res.values() if v['parent_id'] == 0]
    return value




if __name__ == "__main__":
    result = dg_list(lists)
    print(result)
