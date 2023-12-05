import aiohttp
import asyncio
from parsel import Selector

class AsyncScraper:
    def __init__(self, url):
        self.url = url

    async def scrape_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    content = await response.text()
                    selector = Selector(text=content)

                    data = selector.html('d-none d-lg-block mb-4 w-100 mm-slideout affix show down').getall()

                    return data
                else:
                    return f'Не удалось получить доступ к странице. Код состояния: {response.status}'
