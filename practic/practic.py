# def letter_(string_: str):
#     letter_a = 0
#     letter_b = 0
#     list_1 = ['а', 'о', 'у', 'э', 'ы', 'я', 'е', 'ё', 'ю', 'и']
#     for letter in string_.lower():
#         if letter in list_1:
#             letter_a +=1
#         else:
#             letter_b +=1
#     print(f'гласных букв {letter_a}, согласных букв {letter_b}')
#
# letter_(input('введите текст >>>'))
# def sum_num_(num_):   # объявленеие функции  и парамметров
#     sum_num = num_ + num_**2 + num_**3   # слажение введенного числа с возведением его в степени
#     print(sum_num)  # ввывод значения
#
#
# sum_num_(int(input('введите число >>>')))  # вызов функции

# def func_y(x):
#     y = 0
#     if -5 <= x <= 5:
#         y = x ** 2
#     elif x < -5:
#         y = 2 * abs(x) - 1
#     elif x > 5:
#         y = 2 * x
#     return y
#
#
# for x in range(-10, 11):
#     print(func_y(x))

def list_tuple(x):
    sum_word = 0  # щетчик для слов
    sum_letter = 0  # щетчик для букв
    sum_num = 0  # щетчик для нечетных цифр
    if type(x) is tuple:  # проверка на тип кортеж
        for word in x:  # цикл для извлечения объектов кортежа
            if type(word) is str and word.isalpha():  # проверка на тип строка которая ссостоит из букв
                sum_word += 1  # щетчик объектов слова
        return sum_word  # возврат количества слов в кортеже
    elif type(x) is list:  # проверка на тип список
        for string_ in x:  # цик для извлечения объектов списка
            if type(string_) is str and string_.isalpha():  # проверка на тип строка которая состоит из букв
                sum_letter += len(string_)  # щетчик для всех букв
            elif type(string_) is int or \
                    type(string_) is str and string_.isdigit():  # проверка на тип число или строка состоящая из чисел
                for num_ in str(string_):  # цикл для переборки строки с цифрами
                    if int(num_) % 2 != 0:  # выбор нечетных цифр
                        sum_num += 1  # подсчет нечетных цифр
        return sum_letter, sum_num  # возврат количества букв, количество нечетных цифр


tuple_1 = ('age', 1991, 'month', 5, 'day', '30')  # заданный кортеж
list_1 = ['age', 1991, 'month', 5, 'day', '30']  # заданный список

print(type(tuple_1), list_tuple(tuple_1))  # проверка с кортежем
print(type(list_1), list_tuple(list_1))  # проверка с списком


