import random


def func_1(r):  # функция для подсчета площади окружности
    return 3.14 * r ** 2


def func_2(a, c):  # функция для подсчета площади прямоугольника
    return a * c


def func_3(b, h):  # функция для подсчета площади треугольника
    return 0.5 * b * h


func = int(input())  # функция для выбора необходимого подсчета
if func == 1:  # условие вызова функции для подсчета площади окружности
    print(func_1(int(input())))
elif func == 2:  # условие вызова функции для подсчета площади опрямоугольника
    print(func_2(int(input()), int(input())))
elif func == 3:  # условие вызова функции для подсчета площади треугольника
    print(func_3(int(input()), int(input())))


def rand(a, s):  # функция для заполнения списка
    r = [random.randint(a, s) for i in range(0, 10)]  # генератор списка из 10 значений
    print(r)  # вывод списка


rand(int(input()), int(input()))  # вызов функции
