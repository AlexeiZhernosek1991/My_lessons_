def sss(n):
    n = str(n)
    return len(n)


print(sss(input()))




def day_(d):
    h = d * 24
    m = h * 60
    s = m * 60
    return f'дней: {d}, часов: {h}, минут: {m}, секунд: {s}'
print(day_(10))