# a = int(input())
# b = int(input())
# c = int(input())
#
# for i in range(a, b, c):
#     print(i)

# a = input()
# b = input()
# s = ''
# for i in a:
#     if i != b:
#         s += i
# print(s)

# for i in range(54, 9184):
#     if i % 5 == 0:
#         print(i)

# a = input()
# food = ['сало', 'сыр', 'хлеб', 'квас']
# for i in food:
#     if i == a:
#         print('я не ем ', i)

# a = [1, 3, 4, 6, 7]
# d = 0
# f = 1
# for i in a:
#     d += i
#     f *= i
#     print(d)
#     print(f)
# w = 1*
# for i in range(1, 10):
#     for s in range(1, 10):
#         print(i*s, end=' ')

# таблица умножения
for i in range(1, 10):  # переменная i проводит итерацию с объектами функции рандж - это первый множитель
    for w in range(1, 10):  # переменная w проводит итерацию с объектами функции рандж - это второй множитель
        a = (i * w)  # операция перемножения
        y = (f"{w}*{i}={a}")  # формирование строки из переменных
        print('{0: <8}'.format(y), end=' ') # форматирование и вывод строки
    print()
