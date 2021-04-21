import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint

CSV = 'doma.csv'
HOST = 'https://www.avito.ru/'
URL = 'https://www.avito.ru/moskva/doma_dachi_kottedzhi?cd=1'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}

# решил исп. функциональный стиль
# получаю html
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# одну страницу просматриваем
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='iva-item-content-m2FiN')
    doma = []
    # добавляем элементы в список
    for item in items:
        doma.append(
            {
                'title':item.find('div', class_='iva-item-titleStep-2bjuh').get_text(strip=True),
                'link': HOST + item.find('div', class_='iva-item-titleStep-2bjuh').find('a').get('href'),
                'cost': item.find('div', class_='iva-item-priceStep-2qRpg').get_text(strip=True)
                #'img': HOST + item.find('div', class_='photo-slider-image-1fpZZ').find('img').get('src')
                # тут не работает с картинками, по всем итемам ошибку выдает
            }
        )
    return doma

# сохр. в файл
def save_doc(items, path):
   with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Объявление', ' Ссылка на предложение', 'Цена'])
        for item in items:
           writer.writerow( [item['title'], item['link'], item['cost']])

# все страницы проходим
def parser():
    # запрашиваем сколько страниц просматривать
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    # проверяем на работу
    if html.status_code == 200:
        doma = []
        # проходимся циклом по страницам p- это page
        for p in range(1, PAGENATION):
            pprint(f'Loading...{p}')
            html = get_html(URL, params={'p': p})
            doma.extend(get_content(html.text))
            # Все ломается здесь!!!
            save_doc(doma, CSV)
    else:
        print('Error')

parser()
