import json
# Д.з.
"""Создаем пустой словарь"""
dict_product = {}
"""Цикл для записывания продуктов и стоймости"""
while True:
    """Название продукта"""
    a = input('введите название продукта, если закончили покупки введите "stop" >>>')
    """Условие выхода из цикла"""
    if a == 'stop':
        break
    """Стоймость продукта"""
    b = input('введите стоймость продукта >>>')
    """Добавляем в словарь ключ-продукт, значение-стоймость"""
    dict_product.setdefault(a, b)

# """Открываем файл data.json в режиме записи"""
# with open('data1.json', 'w', encoding='UTF-8') as file1:
#     """Записываем наш словарь в файл data.json"""
#     json.dumps(dict_product, file1, ensure_ascii=False)

"""Открываем файл data.json в режиме записи"""
with open('data.json', 'w', encoding='UTF-8') as file:
    """Записываем наш словарь в файл data.json"""
    json.dump(dict_product, file, ensure_ascii=False)

"""Открываем файл data.json в режиме чтения"""
with open('data.json', 'r', encoding='UTF-8') as fp:
    """Передаем считаную информацию из файла data.json в переменную data"""
    data = json.load(fp)
    """Вывод информации в консоль"""
    print(data)

