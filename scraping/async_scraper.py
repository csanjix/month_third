import httpx
from parsel import Selector
import asyncio


class AsyncScraper:
    headers = {
        'authority': 'jut.su',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://jut.su/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    main_url = 'https://jut.su/oneepiece/'
    link_xpath = '//div[@class="logo_b wrapper"]/a/@href'
    plus_url = 'https://jut.su/'
    xpath = '//div[@class="slicknav_menu"]/a/@href'
    template_contains_xpath = '//a[contains(@id, "app-show-episode-title")]'

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def async_generator(self, limit):
        pass

    async def get_url(self, client, url):
        pass

    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            async for page in self.async_generator(limit=3):
                url = self.main_url.format(page=page)
                result = await self.get_url(client=client, url=url)
                print(f'Result for page {page}: {result}')

    async def get_url(self, client, url):
        response = await client.get(url=url)
        print("response: ", response)
        await self.scrape_responses(response)

    async def scrape_responses(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.link_xpath).extract()
        for link in links:
            print("plus_url: ", self.plus_url + link)


if __name__ == "__main__":
    scraper = AsyncScraper()
    scraper.parse_pages()