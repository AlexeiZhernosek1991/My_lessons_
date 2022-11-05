import requests
from bs4 import BeautifulSoup
import csv

url_av = 'https://cars.av.by/filter?brands[0][brand]' \
         '=989&brands[0][model]=2262&brands[0][generation]=2033&engine_type[0]=5&sort=2'
response = requests.get(url_av)
soup = BeautifulSoup(response.text, 'lxml')
cars_ = soup.find_all('div', class_='listing-item')
list_car = []
for car in cars_:
    list_car.append(
        {'age': car.find ('div', class_='listing-item__params').get_text(strip=True)}
    )



