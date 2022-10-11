# Задание №6 урока 4
a_ = int(input('введите число: '))
b_ = int(input('введите число: '))
c_ = a_ > b_  # булево выражеие результат которого дает либо True либо Fales
if c_:  # выполняется если a_ > b_ и соответственно с_ имеет знпчение True
    print('число a_ больше числа b_')
else:  # выполняется если a_ <= b_ и соответственно с_ имеет знпчение Fales
    print('условие не выполняется')

# Задание №8 урока 4
number_1 = float(input('введите первое число :'))
operation = input('ведите операцию: ')
number_2 = float(input('введите второе число :'))
if operation == '/':  # операция деления
    print(number_1 / number_2)
elif operation == '+':  # операция сложения
    print(number_1 + number_2)
elif operation == '-':  # операция вычитания
    print(number_1 - number_2)
elif operation == '*':  # операция умножения
    print(number_1 * number_2)
else:
    print('Проверте правильность ввода')  # обратить внимание на
    # коректность ввода

# Задание №7 урока 4
a_ = int(input('введите 1-ю сторону стреугольника: '))
b_ = int(input('введите 2-ю сторону стреугольника: '))
c_ = int(input('введите 3-ю сторону стреугольника: '))
if a_ + b_ > c_ and c_ + b_ > a_ and c_ + a_ > b_:  # условие выполнения задачи
    print('треульник существует')
else:  # если условие задачи не выполнения
    print('треульник не существует') # вывод результата

# Задание №9 урока 4
string_ = input('введите слово: ')  # присвоение переменной объекту
is_mister = (string_ == 'Mister')  # выражение спрашивает является ли объект словом МИСТЕР
print(is_mister)  # вывод результата булевого выражения

# Задание №10 урока 4
armor_ = input('введите один из цветов black, yellow или red : ')  # Цвет доспехов
shield_ = input('введите один из цветов black, yellow или red : ')  # Цвет щита
is_arms = (armor_ != 'red' and shield_ == 'black')  # условие выполнения булевого выражения
print(is_arms) # вывод результата булевого выражения

# Д.З. №1 Лотерея

import random

your_ticket_ = str(input('введите число от 1 до 9: '))  # введить ваш счастливый билет
random_ticket_ = str(random.randint(1, 9))  # генератор случайного номера билета
is_winner_string_ = (random_ticket_ == your_ticket_)  # выражение булевого значения
if is_winner_string_:  # условие при выгрыше
    print('Вы выграли')
else:  # уловие при проигрыше
    print('выграл билет №', random_ticket_)

# Д.З. №2 Знак зодиака

date_ = int(input('введите день рождения: '))  # дата рождения
month_ = int(input('введите месяц рождения: '))  # месяц рождения
if 23 <= date_ <= 31 and month_ == 12 or 1 <= date_ <= 20 and month_ == 1:  # булево выражения для знака Козерог
    print('Козерог')
elif 21 <= date_ <= 30 and month_ == 1 or 1 <= date_ <= 19 and month_ == 2:  # булево выражения для знака Водолей
    print('Водолей')
elif 20 <= date_ <= 28 and month_ == 2 or 1 <= date_ <= 20 and month_ == 3:  # булево выражения для знака Рыбы
    print('Рыбы')
elif 21 <= date_ <= 31 and month_ == 3 or 1 <= date_ <= 20 and month_ == 4:  # булево выражения для знака Овен
    print('Овен')
elif 21 <= date_ <= 30 and month_ == 4 or 1 <= date_ <= 21 and month_ == 5:  # булево выражения для знака Телец
    print('Телец')
elif 22 <= date_ <= 31 and month_ == 5 or 1 <= date_ <= 21 and month_ == 6:  # булево выражения для знака Близнецы
    print('Близнецы')
elif 22 <= date_ <= 30 and month_ == 6 or 1 <= date_ <= 22 and month_ == 7:  # булево выражения для знака Рак
    print('Рак')
elif 23 <= date_ <= 31 and month_ == 7 or 1 <= date_ <= 21 and month_ == 8:  # булево выражения для знака Лев
    print('Лев')
elif 22 <= date_ <= 31 and month_ == 8 or 1 <= date_ <= 23 and month_ == 9:  # булево выражения для знака Дева
    print('Дева')
elif 24 <= date_ <= 30 and month_ == 9 or 1 <= date_ <= 23 and month_ == 10:  # булево выражения для знака Весы
    print('Весы')
elif 24 <= date_ <= 31 and month_ == 10 or 1 <= date_ <= 22 and month_ == 11:  # булево выражения для знака Скорпион
    print('Скорпион')
elif 23 <= date_ <= 30 and month_ == 11 or 1 <= date_ <= 22 and month_ == 12:  # булево выражения для знака Стрелец
    print('Стрелец')
else:
    print('ошибка ввода данных')
