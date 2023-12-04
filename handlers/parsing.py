from scraping.scraper import Scraper
from aiogram import types

async def get_gata(message: types.Message):
    url_to_scrape = 'https://www.kinopoisk.ru/?utm_referrer=www.google.com'
    scraper = Scraper(url=url_to_scrape)
    data = scraper.scraper_data()
