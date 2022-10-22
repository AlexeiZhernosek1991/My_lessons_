# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
#
# print(k)
#
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict["d"]
# except KeyError:
#     print("Ключа не существует!")
#
# my_list = [1, 2, 3, 4, 5]
#
# try:
#     my_list[6]
# except IndexError:
#     print("Этого индекса нет в списке!")
#
# my_dict_1 = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict_1["d"]
# except IndexError
#     print("Такого индекса не существует!")
# except KeyError:
#     print("Этого ключа не в словаре!")
# except:
# #     print("Произошла другая ошибка!")
#
#
# # my_dict_1 = {"a": 1, "b": 2, "c": 3}
# #
# # try:
# #     value = my_dict_1["d"]
# # except KeyError:
# #     print("Произошла ошибка KeyError!")
# # finally:
# #     print("Оператор finally выполнен!")
#
# # my_dict_1 = {"a": 1, "b": 2, "c": 3}
# # try:
# #     value = my_dict_1["a"]
# # except KeyError:
# #     print("Произошла ошибка KeyError!")
# # else:
# #     print("Ошибок нет!")
# # finally:
# #     print("Оператор finally выполнен!")
#
# def calculator(num1, num2, operat)
#     number_1 = float(input('введите первое число :'))
#     operation = input('ведите операцию: ')
#     number_2 = float(input('введите второе число :'))
#     if operation == '/':  # операция деления
#         try:
#             result = number_1 / number_2  # деление первой переменной на вторую
#         except ZeroDivisionError:
#             print("на ноль делить нельзя")
#         finally:
#             print("dfdf")
#         print(result)  # вывод результата деления
#     elif operation == '+':  # операция сложения
#         print(number_1 + number_2)  # вывод результата сложения
#     elif operation == '-':  # операция вычитания
#         print(number_1 - number_2)  # вывод результата вычитания
#     elif operation == '*':  # операция умножения
#         result = number_1 * number_2  # умноженние первой переменной на вторую
#         print(result)  # вывод результата умножения
#     print('Хотите продолжить "да" или "нет"')
#     start_ = input('введите "да" или "нет": ')  # условие продолжение работы калькулятора
#
def minus(a, b):
    return a - b


def plus(a, b):
    return a + b


def divis(a, b):
    return a / b


def um(a, b):
    return a * b


def cal(num1, num2, oper):
    if oper == "/":
        try:
            return divis(num1, num2) ** 2
        except ZeroDivisionError:
            print("Ошибка но ноль делить нельзя")
            print("result 0")
        finally:
            print("Оператор finally выполнен!")
    elif oper == "*":
        print(um(num1, num2))
    elif oper == "-":
        print(minus(num1, num2))
    elif oper == "+":
        print(plus(num1, num2))


cal(int(input()), int(input()), input())
