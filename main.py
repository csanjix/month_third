import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils import exceptions
from aiogram import types
from scraping.async_scraper import AsyncScraper
from config import dp
from handlers import start, profile

async_scraper= AsyncScraper(url='https://animego.org/')

async def on_async_scraper_command(message: types.Message):
    try:
        result = await async_scraper.scrape_data()

        if isinstance(result, list):
            response_text = 'Результаты скрапинга (первые 5):\n'
            for index, data in enumerate(result[:5], start=1):
                response_text += f'{index}. {data}\n'
        else:
            response_text = result

        await message.answer(response_text)

    except exceptions.MessageTextIsEmpty:
        await message.answer("Пустой запрос, попробуйте еще раз.")

dp.register_message_handler(on_async_scraper_command, commands=['async_scraper'])
start.register_start_handlers(dp)
profile.register_profile_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
