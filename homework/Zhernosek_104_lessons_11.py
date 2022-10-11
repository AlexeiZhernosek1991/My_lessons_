
# Задание №5 урока
list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]
dict_new = dict(zip(list_1, list_2))
print(dict_new)

# Задание №6 урока
string_1 = 'pythonist'
x = 0
dict_1 = {letter: string_1.count(letter) for letter in string_1}
print(dict_1)

# Д.З. магазин
dikt_product = {'cheese': [10, 10],
                'sausage': [5, 12],
                'bread': [2, 15]}


def my_basket(my_product, quantity):
    my_basket_ = dikt_product[my_product][0] * quantity
    return f'с вас {my_basket_} руб.'


def all_product_(product, quantity):
    dikt_product[product][1] = dikt_product[product][1] - quantity
    all_product = 0
    for product_d, price_d in dikt_product.items():
        all_product += price_d[1]
    return f'всего продуктов {all_product} штук'


work = "y"
while work == "y":
    for product_, price in dikt_product.items():
        print(product_, price[0], price[1], sep="-")
    Your_product = input('введите название товара >>>')
    Your_quantity = int(input('введите количество товара >>>'))
    print(my_basket(Your_product, Your_quantity))
    for product_, price in dikt_product.items():
        print(product_, price[0], price[1], sep="-")
    print(all_product_(Your_product, Your_quantity))
    work = input('если хотите выбрать что еще наберите "y" >>>')



