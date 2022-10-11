from urllib.request import urlopen
from bs4 import BeautifulSoup

from os import system

from time import sleep

from consts import *


soup = BeautifulSoup(urlopen(NEWS_SITE), 'html.parser')

prev_news_raw = soup.find_all('h2', {'class': 'home-title'})

first_time = True

while True:
    try:
        news_raw = soup.find_all('h2', {'class': 'home-title'})

        if not first_time:
            if len(news_raw) > len(prev_news_raw):
                system('cls')

                news = []

                for raw_news in news_raw:
                    news.append(str(raw_news).replace('<h2 class="home-title">', '').replace('</h2>', '') + '.')

                print('\n'.join(news))

        else:
            system('cls')

            news = []

            for raw_news in news_raw:
                news.append(str(raw_news).replace('<h2 class="home-title">', '').replace('</h2>', '') + '.')

            print('\n'.join(news))

            first_time = False

        sleep(DELAY)
    except KeyboardInterrupt:
        exit(0)
