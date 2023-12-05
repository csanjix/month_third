import requests
from parsel import Selector
from aiogram import types, Dispatcher
from config import Bot
class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            selector = Selector(response.text)

            news_headlines = selector.html('width=device-width')

            return news_headlines
        else:
            return f'Не удалось получить доступ к странице. Код состояния: {response.status_code}'

url_to_scrape = 'https://www.kinopoisk.ru/?utm_referrer=www.google.com'
scraper = Scraper(url=url_to_scrape)

result = scraper.scrape_data()
if isinstance(result, list):
    print('Результаты скрапинга (первые 5):')
    for index, data in enumerate(result[:5], start=1):
        print(f'{index}. {data}')
else:
    print(result)
