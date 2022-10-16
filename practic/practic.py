# задача №5
# def float_(a, b):
#
#
#
# float_(12, 33)
def div_(a,b):
    division = a
    s = 0
    while division != 0:
        if a % division == 0 and b % division == 0:
            a = a/division
            b = b/division
            print(f'{a} /{b}')
            division = 0
        else:
            division -= 1

div_(12, 33)

