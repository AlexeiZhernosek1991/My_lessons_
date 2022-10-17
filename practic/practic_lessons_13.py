# № 7
def countrange(list_, a: float, b: float) -> int:
    sum_i = 0
    for i in list_:
        if a < float(i) < b:
            sum_i += 1
    return sum_i


list_7 = [0, 5, 9, -1, -8, 5, 5, -9, 1]

print(countrange(list_7, 0, 5))
print(countrange(list_7, -1.5, 10))
print(countrange(list_7, -10, 10))


# № 8
def list_in_list(list_: list):
    list_sum = 0
    for list_in in list_:
        if type(list_in) == list:
            list_sum += 1
    print(list_sum)


list_8 = [{0, 5, 9}, [1, -8], [2, 3, 4, 5], (5, 5, -9, 1)]

list_in_list(list_8)


# № 9

def word_anagram(word1: str, word2: str):
    print(word1[::-1] == word2)


word_anagram('life', 'efil')
word_anagram('life', 'ufo')


# № 6
def list_6_(list_):
    print(list_[::-1])
    # print(list_.sort)
    # print(list_.sort(reverse=True))
    print(list_[1:7])
    list_.pop(4)
    print(list_)
    print(set(list_))
    list_new = []
    for i in list_:
        if type(i) == str:
            list_new.append(i)
    print(list_new)


list_6 = [1, 6, 5, 3, 4, 'as', 'ef', 'w', 'a', 'w']

list_6_(list_6)


# № 1
def bmi_(w, h):
    my_bmi = w / h ** 2
    if my_bmi < 18.5:
        print('Дефицит массы тела')
    elif 18.5 < my_bmi < 24.9:
        print('Нормальная масса тела')
    elif 25 < my_bmi < 29.9:
        print('Увеличение массы тела')
    elif 30 < my_bmi < 34.9:
        print('Ожирение 1 степени')
    elif 35 < my_bmi < 39.9:
        print('Ожирение 2 степени')
    elif my_bmi >= 40:
        print('Ожирение 3 степени')


bmi_(105, 1.76)


# № 2
def figure_(side):
    if side == 3:
        print('треугольник')
    elif side == 4:
        print('четырехугольник')
    elif side == 5:
        print('пятиугольник')
    elif side == 6:
        print('шестиугольник')
    elif side == 7:
        print('септагон')
    elif side == 8:
        print('октогон')
    elif side == 9:
        print('ноногон')
    elif side == 10:
        print('десятиугольник')
    else:
        print('вы вышли за допустимый диапазон от 3 до 10 сторон')


figure_(5)


# № 5

def div_(a, b):
    division = a
    s = 0
    while division != 0:
        if a % division == 0 and b % division == 0:
            a = a / division
            b = b / division
            print(f'{a} /{b}')
            division = 0
        else:
            division -= 1


div_(12, 33)


# № 4
def data(day, month, age):
    if day == 31 and month == 12:
        print(f'{1},{1},{age + 1}')
    elif month == 2 and day == 28 and age % 4 == 0:
        print(f'{29},{2},{age}')
    elif month == 2 and day == 28 and age % 100 == 0 and age % 400:
        print(f'{29},{2},{age}')
    elif month == 2 and day == 28:
        print(f'{1},{3},{age}')
    elif month in [4, 9, 11, 6] and day == 30:
        print(f'{1}, {month + 1}, {age}')
    elif day == 31:
        print(f'{1}, {month + 1}, {age}')
    elif 0 < day < 31:
        print(f'{day + 1}, {month}, {age}')
    elif 31 < day < 0 or 12 < month < 0:
        print("Error")


data(33, 2, 1993)
data(28, 2, 1993)


# №10
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


# №3
def delivery_(a):
    sum_delivery = a / a * 10.95 + (a - 1) * 2.95
    return sum_delivery


print(delivery_(int(input('введите количества товара >>>'))))
