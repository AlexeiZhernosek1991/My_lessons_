# class Car:
#     # статические поля (атрибуты класса)
#     color = 'Grey'
#     weight = 5000
#
#     def __init__(self):
#
#     def turn_on(self):
#         pass
#
#     def ride(self):
#         pass
# car_object = Car()

# class Example:
#     # статические поля (атрибуты класса)
#     val_1stat = 10
#     val_2stat = 50
#
#     def __init__(self, val_1, val_2):
#         self.val_1 = val_1
#         self.val_2 = val_2
#
#     def newval(self):
#         val_3 = 3
#         print(val_3)
#
#     def sum(self):
#         return Example.val_1stat + Example.val_2stat
#
#     def step(self):
#         return self.val_1 ** self.val_2
#
#
# a = Example(val_1=5, val_2=2)
# print(a.sum())
# print(a.step())
# print(a)


class Calculator:

    def __init__(self):
        self.val_1 = int(input())
        self.val_2 = int(input())

    def plus(self):
        return self.val_1 + self.val_2

    def minus(self):
        return self.val_1 - self.val_2

    def x_(self):
        return self.val_1 * self.val_2

    def division(self):
        return self.val_1 / self.val_2


val = Calculator()
print(val.minus())
