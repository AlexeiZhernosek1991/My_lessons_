def sss(n):
    n = str(n)
    return len(n)


print(sss(input()))


def sek_(s):
    m = s / 60
    h = m / 60
    d = h / 24
    return f'дней: {d}, часов: {h}, минут: {m}, секунд: {s}'


print(sek_(1000000))
