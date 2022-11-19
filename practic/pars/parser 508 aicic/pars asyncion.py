import requests
from bs4 import BeautifulSoup
import csv
import time
import asyncio
import aiohttp

list_car = []


async def get_list(session, page):  # Функция выполняющая зосновную задачк парсинга
    url_ = f'https://cars.av.by/filter?brands[0][brand]' \
           f'=989&brands[0][model]=2262&brands[0][generation]=2033&page={page}'  # URL-адрес для парсинга
    head = 'https://cars.av.by'  # Начальная строницв
    async with session.get(url=url_) as response:  # Передаем сессию-запрос в переменную response
        response_text = await response.text()  # Передаем в переменную текст HTML страницы
        soup = BeautifulSoup(response_text, 'lxml')  # Создаем объект BeautifulSoup из текста HTML страницы
        cars_ = soup.find_all('div', class_='listing-item')  # Ищем все блоки кода которые содержат
        # информацию по каждой машине
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


async def gather_tasks(pages):  # Функция для создания списка задач
    async with aiohttp.ClientSession() as session:
        tasks = []  # Пустой список для задач
        for page in range(1, pages + 1):  # Цикл для добавление задач в список в соответствии с числом страниц парсинга
            print(f'Парсинг {page} страницы')  # Вывод информации о парсинге страницы
            task = asyncio.create_task(get_list(session, page))  # Передаем щадачку в переменную task
            tasks.append(task)  # Добавляем задачу в список
        await asyncio.gather(*tasks)


def main():
    pages = int(input('введите количество страниц >>>'))  # Вводится количество страниц
    start_time = time.time()  # Начало работы программы
    asyncio.run(gather_tasks(pages))  # Пуск списка задач
    with open('pars.csv', 'w', encoding='cp1251', newline='') as file:  # Запись в CSV файл заголовков столбцов
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Коробка передач', 'Объем двигателя', 'Тип топлива', 'Тип кузова',
                         'Цена в рублях', 'Цена в доларах', 'Место расположения', 'Ссылка'])  # Список столбцов

        for car in list_car:  # Цикл для записи каждой машины
            writer.writerow([car['transmission'], car['engine volume'], car['fuel'], car['type'],
                             car['price'], car['price_usd'], car['location'], car['http']])
            # Записывает в CSV файл информацию о автомобилях
    print(f'Парсинг завершен. За время >>> {time.time() - start_time}')
    # Сообщение о завершении парсинга и времени работы программы


if __name__ == "__main__":
    main()
