import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/page-"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

listd = []
for page in range(1,3):
    req = requests.get(url+str(page)+".html", headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    data_book = soup.findAll('article','product_pod')

    number_map = {
        'One':1,
        'Two':2,
        'Three':3,
        "Four":4,
        "Five":5
    }

    for i in data_book:
        scrapping_image = i.find('div','image_container').find('img')['src']
        scrapping_judul = i.find('h3').a.get('title')
        scrapping_price = i.find('p','price_color').text
        star = i.find('p','star-rating')
        scrap_star = star.attrs.get('class')[1]
        scrapping_star = number_map.get(scrap_star)
        listd.append([scrapping_judul,scrapping_price,scrapping_star,scrapping_image])
    

column = ['Judul Buku','Harga Buku','Rating','Gambar buku']
file = csv.writer(open('latihan/scraping_book.csv', 'w', newline='', encoding='UTF-8'))

file.writerow(column)
for i in listd:
    file.writerow(i)

for i in listd:
    print(i)