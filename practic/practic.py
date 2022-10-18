def alingment(list_):
    l_1 = []
    while len(list_) < 9:
        for i in list_:
            if type(i) is not list:
                l_1.append(i)
            elif type(i) is list:
                l_1.extend(i)
        list_ = l_1
        l_1 = []
    for i in list_:
        if type(i) is not list:
            l_1.append(i)
        elif type(i) is list:
            l_1.extend(i)
    list_ = l_1
    print(list_)


def alingment(s):
    if s == []:
        return s
    elif type(s[0]) == list:
        return (alingment(s[0]) + alingment(s[1:]))
    return (s[:1] + alingment(s[1:]))


list_1 = [[1], [2, 3], [[4, 5], 6], [7, [8, [9]]]]

print(fff(list_1))
