import requests
from bs4 import BeautifulSoup

response = requests.get(
    'https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=2262&brands[0][generation]=2033'
)
print
soup = BeautifulSoup(response.text, 'html.parser')
cars_ = soup.find_all("div", class_="listing-item_params")
print(cars_)
