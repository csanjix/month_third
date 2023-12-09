from parsel import Selector
import requests

class NewsScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    main_url = "https://24.kg/"
    link_xpath = '//div[@class="title"]/a/@href'
    img_xpath = '//div[@class="Dashboard-Content-Card--image"]/img/@src'

    def parse_data(self):
        html = requests.get(url=self.main_url, headers=self.headers).text
        tree = Selector(text=html)
        links = tree.xpath(self.link_xpath).extract()
        for link in links:
            print(link)
        return links

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()