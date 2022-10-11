import random
import math

# Задача №3
list_a = [random.randint(1, 99) for i in range(1, 8)]  # генератор спискска
list_2 = []  # пустой список для четных чисел
list_1 = []  # пустой список для нечетных чисел
result_ = 0  # переменная для конечного результата
for i in list_a:  # цикл для итереации сгенерированого списка
    if i % 2 == 0:  # условие для отбора четных чисел из списка
        list_2.append(i)  # добавление четных чисел в список
    else:
        list_1.append(i)
if len(list_1) > len(list_2):
    result_ = list_a[1] * list_a[3] * list_a[6]
else:
    result_ = sum(list_a)
print(result_)


# Задача №4
def ap_(list_1, list_2):
    new_list = []
    for i in list_1:
        for s in list_2:
            if i == s:
                new_list.append(i)
    return new_list


list_a = [5, [1, 2], 2, 'r', 4, 'ee']
list_b = [4, 'we', 'ee', 3, [1, 2]]
print(ap_(list_a, list_b))

# Задача №5

list_a = [4, 6, 'py', 'tell', 78]
list_b = [44, 'hello', 56, 'exept', 3]
list_a.extend(list_b)
print(list_a)
list_a.insert(3, 6)
print(list_a)
for i in list_a:
    if type(i) == str:
        list_a.remove(i)
print(list_a)
print(len(list_a))

# Д.з. №1

list_ = [15, 48, 'hello', 6, 19, 'world']
list_a = ['a', 'e', 'i', 'o', 'u']
letter_a_sum = 0
letter_b_sum = 0
for i in list_:
    if type(i) is int:
        if i % 2 == 0:
            print(i // 10 + i % 10)
        else:
            list_[list_.index(i)] = list_[0]
    elif type(i) is str:
        for letter_ in i:
            for letter_a in list_a:
                if letter_ == letter_a:
                    letter_a_sum += 1
            letter_b_sum += 1
letter_b_sum -= letter_a_sum
print(list_)
print(f"количество гласных букв: {letter_a_sum} "
      f"количество согласных букв: {letter_b_sum}")


# Д.з. Практика
# П.з. №1
def hep_(cat_1, cat_2):
    return math.hypot(cat_1, cat_2)


print(hep_(int(input()), int(input())))


# П.з. №2
def medium_number(num_1, num_2, num_3):
    if num_1 > num_2 > num_3:
        return num_2
    elif num_2 > num_1 > num_3:
        return num_1
    else:
        return num_3


print(medium_number(input(), input(), input()))


# П.з. №3
def number_():
    num_1 = random.choice(range(1, 100))
    num_2 = num_1 + 1
    if num_1 % 2 != 0:
        return f"Первое число нечетное: {num_1}"
    else:
        return f"Второе число нечетное: {num_2}"


print(number_())


# П.з. №4
def number_1(num):
    num = str(num)
    num_new = num[::-1]
    num_new = int(num_new)
    return num_new


print(number_1(int(input('Введите четырехзначное число: '))))


# П.з. №5
def rect_(sing_1, sing_2):
    print(f"{sing_1} " * 6,
          f'{sing_1}{sing_2 * 9}{sing_1}',
          f'{sing_1}{sing_2 * 9}{sing_1}',
          f"{sing_1} " * 6, sep='\n')


print(rect_("*", "-"))


# П.з. №7
def arr_1(start, stop, index_, num_):
    arr = []
    for i in range(start, stop):
        arr.append(i)
    arr.insert(index_, num_)
    return arr


print(arr_1(1, 9, 4, 5))


# П.з. №8

def word_():
    string_ = input("введите несколько слов через пробел: ")
    counter_ = 1
    for i in string_:
        if i == " ":
            counter_ += 1
    return counter_


print(word_())


# П.з. №9
def word_aW():
    string_ = input("введите строку с буквами разного регистра: ")
    new_sring = ""
    for i in string_:
        if i.islower():
            new_sring += i
    return new_sring


print(word_aW())


# П.з. №10
def num_7_():
    list_7 = []
    for i in range(1, 101):
        if i % 7 != 0:
            list_7.append(i)
    return list_7


print(num_7_())


# П.з. №11
def num_sum_():
    list_sum = []
    for i in range(1, 101):
        list_sum.append(i)
    return sum(list_sum)


print(num_sum_())


# П.з. №12
def factor_(n):
    n_1 = 1
    for i in range(1, 1 + n):
        n_1 *= i
    return n_1


print(factor_(15))

 # П.з. №6

list_a = []
sum___ = []
for i in range(2, 10000):
    for a in range(1, i):
        if i % a == 0:
            sum___.append(a)
    if sum(sum___) == i:
        list_a.append(i)
    sum___.clear()
print(list_a)
