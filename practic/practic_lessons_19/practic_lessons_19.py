from datetime import datetime


# def count_the_time(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now() - start)
#         return result
#
#     return wrapper
#
#
# @count_the_time
# def create_list():
#     list_ = []
#     for _ in range(10 ** 5):
#         if _ % 2 == 0:  # целевой код
#             list_.append(_)  # целевой код
#     return list_


#
#
# @count_the_time
# def create_list_gen():
#     list_ = [i for i in range(10 ** 5) if i % 2 == 0]  # целевой код
#     return list_
#
#
# create_list()


# create_list_gen()


