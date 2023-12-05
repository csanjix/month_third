from scraping.scraper import Scraper
from aiogram import types
import requests

async def get_gata(message: types.Message):
    url_to_scrape = 'https://www.kinopoisk.ru/?utm_referrer=www.google.com'
    scraper = Scraper(url=url_to_scrape)
    data = scraper.scraper_data()

    try:
        for index, data in enumerate('result'[:5], start=1):
            await message.answer(f'Результат скрапинга {index}. {data}')

    except (TypeError, IndexError):
        print('Результаты скрапинга:')
        print('result')

    except Exception as e:
        print(f"Ошибка: {e}")
