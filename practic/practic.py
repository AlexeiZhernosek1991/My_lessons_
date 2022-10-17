def data(day, month, age):
    if day == 31 and month == 12:
        print(f'{1},{1},{age + 1}')
    elif month == 2 and day == 28 and age % 4 == 0:
        print(f'{29},{2},{age}')
    elif month == 2 and day == 28 and age % 100 == 0 and age % 400:
        print(f'{29},{2},{age}')
    elif month == 2 and day == 28:
        print(f'{1},{3},{age}')
    elif month in [4, 9, 11, 6] and day == 30:
        print(f'{1}, {month + 1}, {age}')
    elif day == 31:
        print(f'{1}, {month + 1}, {age}')
    elif 0 < day < 31:
        print(f'{day + 1}, {month}, {age}')


data(28, 2, 1993)
