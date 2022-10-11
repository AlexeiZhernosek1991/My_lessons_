# практика задание №13
def n_(num_):
    degree = 1
    list_ = []
    while 2 ** degree < num_:
        list_.append(2 ** degree)
        degree += 1
    return list_


num_ = int(input('>>> '))
print(n_(num_))

# практика задание №12

num_12 = num_
start = 1
counter_1 = 0
counter_2 = 1
while start <= num_12:
    print(start, end=' ')
    start += 1
    counter_1 += 1
    if counter_1 == counter_2:
        print()
        counter_2 += 1
        counter_1 = 0

print()
# практика задание №12 второй вариант
nums = [str(i) for i in range(1, (num_12) + 1)]
counter_3 = 0
while nums:
    print(' '.join(nums[:counter_3 + 1]))
    counter_3 += 1
    nums = nums[counter_3:]