# digit = int(input('Введите число: '))
# if digit % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# nunmber_finger = int(input('Введите номер пальца: '))
# if nunmber_finger == 1:
#     print('большой палец')
# elif nunmber_finger == 2:
#     print('большой палец')
# elif nunmber_finger == 3:
#     print('средний палец')
# elif nunmber_finger == 4:
#     print('безымянный палец')
# elif nunmber_finger == 5:
#     print('безымянный палец')

# number_month = int(input('Введите номер месяца: '))
# if 2 < number_month < 6:
#     print('весна')
# elif 5 < number_month < 9:
#     print('лето')
# elif 8 < number_month < 12:
#     print('осень')
# elif 0 < number_month < 3:
#     print('зима')
# elif number_month == 12:
#     print('зима')

# number_1 = int(input('введите число'))
# number_2 = int(input('введите число'))
# number_3 = int(input('введите число'))
# if number_1 > number_2 and number_1 > number_3:
#     print(number_1)
# elif number_2 > number_1 and number_2 > number_3:
#     print(number_2)
# elif number_3 > number_1 and number_3 > number_2:
#     print(number_3)
import random

# komp_ = random.randint(1, 3)
# # введите число от 1 до 3, 1-камень, 2-ножницы, 3 бумага
# user_ = int(input())
# if komp_ == 1 and user_ == 2:
#     print('проиграл')
# elif komp_ == 1 and user_ == 3:
#     print('выграл')
# elif komp_ == 2 and user_ == 3:
#     print('проиграл')
# elif komp_ == 2 and user_ == 1:
#     print('выграл')
# elif komp_ == 3 and user_ == 1:
#     print('проиграл')
# elif komp_ == 3 and user_ == 2:
#     print('выграл')
# elif komp_ == user_:
#     print('ничия')
#

# a_ = int(input('введите число: '))
# b_ = int(input('введите число: '))
# c_ = a_ > b_
# if c_:
#     print('a_ > b_')
# else:
#     print('условие не выполняется')

number_1 = float(input('введите первое число :'))
resul = input('ведите операцию: ')
number_2 = float(input('введите второе число :'))
if resul == '/':
   print(number_1 / number_2)
elif resul == '+':
   print(number_1 + number_2)
elif resul == '-':
   print(number_1 - number_2)
elif resul == '*':
   print(number_1 + number_2)
else:
    print('Проверте правильность ввода')

# a_ = int(input('введите сторону стреугольника: '))
# b_ = int(input('введите 2-ю сторону стреугольника: '))
# c_ = int(input('введите 3-ю сторону стреугольника: '))
# if a_ + b_ > c_ and c_ + b_ > a_ and c_ + a_ > b_:
#     print('треульник существует')
# else:
#     print('треульник не существует')

