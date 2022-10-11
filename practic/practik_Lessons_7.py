# def give_sum_(a, b):
#     c = a + b
#     return c
def give_minus_(a, b):
    c = a - b
    return c
#
#
# def give_umn_(a, b):
#     print(a * b)
#
#
# def give_degree_(a, b):
#     print(a / b)
#
# a = 1
# b = 2
# print(give_sum_(a, b))
#
# a = give_sum_(a, b)
# a1 = give_minus_(a, b)

# def sum_massiv(a):
    print(sum(a))
#
#
# sum_massiv([1,2,3,4,5])

# def sum_massiv():
#     a = [1, 2, 3, 4]
#     e = 0
#     for i in a:
#        e +=i
#     print(e)
#
# sum_massiv()

# a = 'hrllo World'
# print(a.replace('hrllo', 'gudby'))

def is_year_leap(a):
    if a % 4 == 0 or a % 100 == 0 or a % 400 == 0:
        return "True"
    else:
        return False


is_year_leap(1233)

def give_minus_(a, b):
    c = a - b
    print(c)

give_minus_(1, 2)