import json

import requests
from bs4 import BeautifulSoup
import csv
import time

url_ = 'https://cars.av.by/filter?brands[0][brand]=1155&brands[0][model]=1167&'
# URL- адрес интересуемого автомобиля
head_ = 'https://cars.av.by'  # Начальная страница

response1 = requests.get(url_)
soup = BeautifulSoup(response1.text, 'lxml')
print(soup)
