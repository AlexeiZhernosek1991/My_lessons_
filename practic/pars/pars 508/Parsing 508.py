import requests
from bs4 import BeautifulSoup
import csv
import time

url_ = 'https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=2262&brands[0][generation]=2033&page='
# URL- адрес интересуемого автомобиля
head_ = 'https://cars.av.by'  # Начальная страница


def get_html(url):  # Функция которая отправляет запрос на сайт
    response = requests.get(url)  # В переменную response передаем ответ от запроса на сайт
    return response


def pars(response, head):  # Функция осуществляет обработку полученного ответа с сайта
    soup = BeautifulSoup(response.text, 'lxml')  # Создаем объект BeautifulSoup из текста HTML страницы
    cars_ = soup.find_all('div', class_='listing-item')  # Ищем все блоки кода которые содержат
    # информацию по каждой машине
    list_car = []  # Пустой сптисок
    for car in cars_:  # Проходимся циклом по списку с блоками кода каждого автомобиля
        list_car.append(
            {'transmission': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[0],
             # Парсим информацию о коробке передач
             'engine volume': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')
             [1].replace('\xa0', ' '),  # Парсим информацию о объеме двигателя
             'fuel': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[2],
             # Парсим информацию о типе используемого топлива
             'type': car.find('div', class_='listing-item__params').find_all('div')[1].text.split(',')[3],
             # Парсим информацию о типе кузова
             'price': car.find('div', class_='listing-item__price').text.encode('ascii', errors='ignore')
             .decode('UTF-8').replace('.', ''),  # Парсим информацию о цене в рублях
             'price_usd': car.find('div', class_='listing-item__priceusd').text.encode('ascii', errors='ignore')
             .decode('UTF-8').replace('$', ''),  # Парсим информацию о цене в доларах
             'location': car.find('div', class_='listing-item__location').text,
             # Парсим информацию месте расположения автомобиля
             'http': head + car.find('a', class_='listing-item__link').get('href')
             # Парсим информацию ссылку на объявление
             }

        )
    return list_car  # Список с информацией по каждому автомобиль (переданная в словарь)


def writer_(list_car, writer):  # Функция для записи информации в CSV файл
    for car in list_car:  # Проходимся циклом по списку с автомобилями и предаем из словаря каждой машины значения
        writer.writerow([car['transmission'], car['engine volume'], car['fuel'], car['type'],
                         car['price'], car['price_usd'], car['location'], car['http']])


def main(url, head):  # Основная функция принимает значения URL-адреса интересуемого автомобиляб и начальную стораницу
    pages = int(input('введите количество страниц >>>'))  # Вводим количество страниц для парсинга
    start_time = time.time()  # Начало парсинга
    with open('pars.csv', 'w', encoding='cp1251', newline='') as file:  # Запись в CSV файл заголовков столбцов
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Коробка передач', 'Объем двигателя', 'Тип топлива', 'Тип кузова',
                         'Цена в рублях', 'Цена в доларах', 'Место расположения', 'Ссылка'])  # Список столбцов
        for page in range(1, pages + 1):  # Цикл парсинга каждой страницы с автомобилями
            print(f'Парсинг {page} страницы')
            response = get_html(url + str(page))  # Передаем в переменную результата работы функции get_html
            list_car = pars(response, head)  # Передаем в переменную результата работы функции list_car
            if not list_car:  # Проверяет если списо с машинами пустой прекращает парсинг
                print(f"Страницы закончились. Всего {page-1} страниц")
                break
            writer_(list_car, writer)  # Записывает в CSV файл информацию о автомобилях
    print(f'Парсинг завершен, за время {time.time()-start_time}')
    # Сообщение о завершении парсинга и времени работы программы


if __name__ == "__main__":
    main(url_, head_)
