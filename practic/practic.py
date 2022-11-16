import requests
from bs4 import BeautifulSoup
import csv
import string


def wriner_(list_):
    with open('pars.csv', 'w', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(list_)


def main(url, head):
    with open('pars.csv', 'w', encoding='utf8', newline='') as file:
        writer_ = csv.writer(file, delimiter=';')
        writer_.writerow(['transmission', 'engine volume', 'fuel', 'price', 'price_usd', 'type', 'location', 'http'])
    pages = int(input('введите количество страниц >>>'))
    for page in range(1, pages + 1):
        response = get_html(url + page)
        pars(response, head)


with open('pars.csv', 'w', encoding='utf8', newline='') as file:
    writer_ = csv.writer(file, delimiter=';')
    writer_.writerow(['num', 'transmission', 'engine volume', 'fuel', 'price', 'price_usd', 'type', 'location', 'http'])

url_ = 'https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=2262&brands[0][generation]=2033&page='
head_ = 'https://cars.av.by'

response = requests.get(url_)
soup = BeautifulSoup(response.text, 'lxml')
cars_ = soup.find_all('div', class_='listing-item')
list_car = []
for car in cars_:
    list_car.append(
        {'transmission': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[0],
         'engine volume': car.find('div', class_='listing-item__params') .find_all('div')[1].text.split(',')[1],
         'fuel': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[2],
         'type': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[3],
         'price': car.find('div', class_='listing-item__price').text,
         'price_usd': car.find('div', class_='listing-item__priceusd').text,
         'location': car.find('div', class_='listing-item__location').text,
         'http': head_ + car.find('a', class_='listing-item__link').get('href')
         }

    )
print(list_car)
list_new = []
for car in list_car:
    list_new.append([car['transmission'], car['engine volume'], car['fuel'], car['type'],
                     car['price'], car['price_usd'], car['location'], car['http']])
print(list_new)
print(list_new[2][1])
#
# with open('pars.csv', 'w', encoding='utf8', newline='') as file:
#     writer_ = csv.writer(file, delimiter=';')
#     for car in list_car:
#         writer_.writerow([car['transmission'], car['engine volume'], car['fuel'], car['type'],
#                           car['price'], car['price_usd'], car['location'], car['http']])


# with open('pars.csv', 'r', encoding='utf8', newline='') as file:
#     reader_ = csv.reader(file, delimiter=';')
#     lit_11 = list(reader_)
#     a = lit_11[0][4]
#     print(lit_11)
#
