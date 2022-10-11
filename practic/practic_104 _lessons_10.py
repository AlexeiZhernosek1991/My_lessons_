dict_1 = {1: 3, 2: 5}
dict_2 = dict([(1, 2), (2, 6)])
dict_3 = dict.fromkeys(['a', 'b'], 200)
dict_4 = {a: a**2 for a in range(7)}
print(dict_1, dict_2, dict_3, dict_4)
# dict_5 = {'sss': 'ddd', 'sss1': 'ddf'}
# print(dict_5['sss'])

#
# print(Salary)
# del Salary['Secretary']
# print(Salary)
# Salary = {'Director': 120800.0,
# #           'Secretary': 101150.25,
# #           'Locksmith': 188200.00}
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)
#
# key2 = 5
# if key2 in Salary:
#     del Salary[key2]
# Salary = {'Director': 120800.0,
#           'Secretary': 101150.25,
#           'Locksmith': 188200.00}
# for key in Salary:
#     print(key, Salary[key])
# for item in Salary.items():
#     print(item)

# person = {'name': 'Alex', 'age': '30', 'city': 'city'}
# print(person['age'])
# cars_ = {'BMW': ['5sires', '7sires', '3sires'],
#          'Tesla': ['modelS', 'modelX', 'model3']}
# print(cars_['BMW'][0::2], cars_['Tesla'][0::2])
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(d1["b"] == d2["b"])
# dict_digit = {1: 1, 2: 2, 3: 3}
# d = 1
# for i in dict_digit.items():
#     d *= i[1]
# print(d)
# list_1 = ['a', 'b', 'c']
# list_2 = [1, 2, 3]
# dict_new = dict(zip(list_1, list_2))
# print(dict_new)