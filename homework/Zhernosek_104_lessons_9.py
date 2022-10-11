import random
from icecream import ic

# задание №1 проверить если в послндовательности дубликаты
list_ = [random.randint(1, 20) for i in range(10)]  # генератор случайного списка
new_set = set(list_)  # приводим список к типу множества
ic(new_set)
ic(list_)
if len(list_) > len(new_set):  # сравнение длинны списка с длинной множества
    print('Есть дубликаты в списке list_')  # если длинна списка больше значит
    # в списке есть дубли.
else:
    print('Дублей в списке list_ нет')  # если длинна списка и множества одинаковая

# задание №2
# 1. создать множество
# 2. создать неизменяемое множество
# 3. объединить множества
# 4. выполнить операцию пересечения созданных множеств
set_ = {1, 2, 3, 4, 5, 6}  # данное множество
list_ = ['камень', 'ножницы', 'бумага']  # список
set_f_ = frozenset(list_)  # приводим список к типу неизменяемого множества
print(set_.union(set_f_))  # объединение множества
print(set_.isdisjoint(set_f_))  # проверка пересекаются ли множества

# Д.з. 1. создайте кортеж от 0 до 9 подщитайте суму
tup_ = tuple([*range(10)])
ic(tup_)
print(sum(tup_))

# Д.з. 2. выведите статистику частности букв в картеже
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и',
             'и', 'и', 'т', 'т', 'а', 'и', 'и',
             'и', 'и', 'и', 'т', 'и')
print('Количество повторений буквы "т" -', long_word.count('т') / len(long_word) * 100,
      'Количество повторений буквы "а" -', long_word.count('а') / len(long_word) * 100,
      'Количество повторений буквы "и" -', long_word.count('и') / len(long_word) * 100)

# Д.з. 3. допишпте скрипт для расчета средней темепературы
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))

12646