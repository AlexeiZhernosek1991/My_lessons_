import os

# f = open('example.txt', 'r')
#
# print(f.read(9))

# x = open('test.txt', 'r')
#
# print(x.read())
# print(x.readline())
# print(x.readlines())

# os.rename("D:\Пайтон\pyproject\\v\www.txt", "D:\Пайтон\pyproject\\v\wwr.txt")

# os.mkdir("folder")

# print('текущая дериктория:', os.getcwd())

#
# f = open('test.txt', 'r')
# x = f.readline()
# print(x)
# sum_i = 0
# for i in x:
#     if i.isdigit():
#         sum_i += int(i)
# print(sum_i)

# # д.з.
# """Исходный список"""
# list_ = [1, 'my', 'school', 5, 3]
# """Создаем строку с отсортированными цифрами по возростанию"""
# string_1 = ' '.join(sorted([str(i) for i in list_ if isinstance(i, int)]))
# """Создаем строку с отсортированными строками по длинне строки"""
# string_a = ' '.join(sorted([i for i in list_ if isinstance(i, str)]))
# with open('test.txt', 'w') as file_test:  # открыть указаный файл для редоктирования
#     file_test.write(string_a + ' ' + string_1)  # вписываем строку в файл
