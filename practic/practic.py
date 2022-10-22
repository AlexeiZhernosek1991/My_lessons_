def list_6_(list_: list):
    print(list_[::-1])
    list_a = []
    list_1 = []
    for i in list_:
        if type(i) == str:
            list_a.append(i)
        else:
            list_1.append(i)
    list_1.sort()
    list_a.sort()
    list_1.extend(list_a)
    print(list_1)
    print(list_[1:7])
    list_.pop(4)
    print(list_)
    print(set(list_))
    list_new = []
    for i in list_:
        if type(i) == str:
            list_new.append(i)
    print(list_new)


list_ = [1, 6, 5, 3, 4, 'as', 'ef', 'w', 'a', 'w']

list_6_(list_)
