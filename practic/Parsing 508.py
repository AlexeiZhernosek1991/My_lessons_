import requests
from bs4 import BeautifulSoup
import csv

url_ = 'https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=2262&brands[0][generation]=2033&page='
head_ = 'https://cars.av.by'


def get_html(url):
    response = requests.get(url)
    return response


def pars(response, head):
    soup = BeautifulSoup(response.text, 'lxml')
    cars_ = soup.find_all('div', class_='listing-item')
    list_car = []
    for car in cars_:
        list_car.append(
            {'transmission': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[0],
             'engine volume': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')
             [1].replace('\xa0', ' '),
             'fuel': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[2],
             'type': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[3],
             'price': car.find('div', class_='listing-item__price').text.encode('ascii', errors='ignore')
             .decode('UTF-8').replace('.', ''),
             'price_usd': car.find('div', class_='listing-item__priceusd').text.encode('ascii', errors='ignore')
             .decode('UTF-8').replace('$', ''),
             'location': car.find('div', class_='listing-item__location').text,
             'http': head + car.find('a', class_='listing-item__link').get('href')
             }

        )
    return list_car


def writer_(list_car, writer):
    for car in list_car:
        writer.writerow([car['transmission'], car['engine volume'], car['fuel'], car['type'],
                         car['price'], car['price_usd'], car['location'], car['http']])


def main(url, head):
    with open('pars.csv', 'w', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Коробка передач', 'Объем двигателя', 'Тип топлива', 'Тип кузова',
                         'Цена в рублях', 'Цена в доларах', 'Место расположения', 'Ссылка'])
        pages = int(input('введите количество страниц >>>'))
        for page in range(1, pages + 1):
            print(f'Парсинг {page} страницы')
            response = get_html(url + str(page))
            list_car = pars(response, head)
            if not list_car:
                print(f"Страницы закончились. Всего {page-1} страниц")
                break
            writer_(list_car, writer)
    print('Парсинг завершен')


if __name__ == "__main__":
    main(url_, head_)
