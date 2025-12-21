import requests
from bs4 import BeautifulSoup as bs
import csv
import time


class Bot:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://https://www.avito.ru/moskva/doma_dachi_kottedzhi"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
            return response



def main():
    bot = Bot()
    html = bot.get_html()
    print(html)

if __name__ == '__main__':
    main()