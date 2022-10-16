# def tellefon_(text_: str):
#     dict_alf = {
#         ".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
#         "A": 2, "B": 22, "C": 22,
#         "D": 3, "E": 33, "F": 33,
#         "G": 4, "H": 44, "I": 444,
#         "J": 5, "K": 55, "L": 555,
#         "M": 6, "N": 66, "O": 666,
#         "P": 7, "Q": 77, "R": 777, "S": 7777,
#         "T": 8, "U": 88, "V": 888,
#         "W": 9, "X": 99, "Y": 999, "Z": 9999
#     }
#     list_ = []
#     for i in text_.upper():
#         if i in dict_alf:
#             list_.append(str(dict_alf[i]))
#         elif i not in dict_alf:
#             list_.append(i)
#     print(list_)
#
#
# tellefon_('sdkm!fom,csn:o15817')



def tellefon_(text_: str):
    dict_alf = {
        ".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
        "A": 2, "B": 22, "C": 22,
        "D": 3, "E": 33, "F": 33,
        "G": 4, "H": 44, "I": 444,
        "J": 5, "K": 55, "L": 555,
        "M": 6, "N": 66, "O": 666,
        "P": 7, "Q": 77, "R": 777, "S": 7777,
        "T": 8, "U": 88, "V": 888,
        "W": 9, "X": 99, "Y": 999, "Z": 9999
    }
    for i in text_.upper():
        if i in dict_alf:
            print(str(dict_alf[i]), end=" ")
        elif i.isdigit():
            print(i, end=" ")
        else:
            print(end='')


tellefon_('sdkm!fom,csn:(o1581)7')
