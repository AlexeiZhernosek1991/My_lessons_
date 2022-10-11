import math
import random


# задание №3

def square(side):  # создание функции с одним аргументом
    perimeter = side * 4  # периметр квадрата
    sq_ = side ** 2  # плошадь квадрата
    diagonal = math.hypot(side, side)  # диагональ квадрата
    results = (perimeter, sq_, diagonal)  # картэж с данными
    return results


print(square(int(input('введите сторону куба: '))))  # вывод информации


# задание №4

def season(month):  # объявление функции и аргумента функции
    if 3 <= month <= 5:  # условие для весны
        return "Весна"
    elif 6 <= month <= 8:  # условие для лета
        return "Лето"
    elif 9 <= month <= 11:  # условие для осени
        return "Осень"
    else:  # условие для зимы
        return "Зима"


print(season(int(input('введите месяц: '))))


# заданеи №5

def is_prime(num_):
    num_2 = 2  # наименьшее простое число больше еденицы
    while num_ % num_2 != 0:  # цикл для проверки условий простого числа
        num_2 += 1
    return num_ == num_2  # возвращает True если число простое и Fales если число составное


print(is_prime(int(input('введите число: '))))


# задание 6

def arr_sum():  # объявление функции
    arr = []  # пустой массив
    while len(arr) != 10:  # цикл для формирования случайного массива
        a = random.randint(1, 100)
        arr.append(a)
    return sum(list(arr)) / 10  # вовращает среднее значение объектов массива


print(arr_sum())

def plus_(num_1, num_2):  # функйия сложения
    result = num_1 + num_2  # операция сложения для функции plus_
    return result  # возвращает результат опреации сложения


def minus_(num_1, num_2):  # функйия вычитания
    result = num_1 - num_2  # операция вычитания для функции minus_
    return result  # возвращает результат опреации вычитания


def divide_(num_1, num_2):  # функйия диления
    result = num_1 / num_2  # операция деления для функции divide_
    return result  # возвращает результат опреации деления


def x_(num_1, num_2):  # функйия умножения
    result = num_1 * num_2  # операция умножения  для функции x_
    return result  # возвращает результат опреации умножения


result_end = 1
while result_end != 0:  # условие безостановочной работы калькулятора
    num_1 = int(input('введите первое число: '))  # первый аргумент для функции
    operation = input('введите операцию: ')  # выбор операции дял исполнения нужной функции
    num_2 = int(input('введите второе число: '))  # второй аргумент для функции
    # условие для сложения
    if operation == "+":
        result_end = plus_(num_1, num_2)
        print(result_end)
    # условие для вычитания
    elif operation == "-":
        result_end = minus_(num_1, num_2)
        print(result_end)
    # условие для деления
    elif operation == "/":
        result_end = divide_(num_1, num_2)
        print(result_end)
    # условие для умножения
    elif operation == "*":
        result_end = x_(num_1, num_2)
        print(result_end)
print('Конец работы калькулятора')