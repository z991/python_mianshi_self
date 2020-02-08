l_ha = [2, 4, 1, 2, 5, 6]

l_heng = [3, 1, 3, 5, 6, 4]

l_desk = []

while l_ha and l_heng:
    heng1 = l_heng[0]
    l_desk.append(heng1)
    l_heng.pop(0)
    if l_desk.count(heng1) == 2:
        l_ha.extend(l_desk[l_desk.index(heng1):-1])
        del l_desk[l_desk.index(heng1):-1]

    ha1 = l_ha[0]
    l_desk.append(ha1)
    l_ha.pop(0)
    if l_desk.count(ha1) == 2:
        l_ha.extend(l_desk[l_desk.index(ha1):-1])
        del l_desk[l_desk.index(ha1):-1]








print("l_ha====", l_ha)
print("l_heng====", l_heng)
print("l_desk====", l_desk)
"""
heng1 = l_heng[0]
    l_desk.append(heng1)
    l_heng.pop(0)
    if l_desk.count(heng1) == 2:
        l_ha.extend(l_desk[l_desk.index(ha1):-1])
        del l_desk[l_desk.index(ha1):-1]
"""

def jump_floor(number):
    if number == 0:
        return 0
    prev, curr = 1, 2
    for _ in range(3, number+1):
        prev, curr = curr, prev+curr
    return curr


if __name__ == '__main__':
    res = jump_floor(6)
    print(res)