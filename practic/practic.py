import random


def rand(a, s):
    r = [random.randint(a, s) for i in range(0, 10)]
    print(r)


rand(int(input()), int(input()))