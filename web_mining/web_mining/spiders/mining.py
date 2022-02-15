import json
import scrapy
from scrapy.crawler import CrawlerProcess
from web_mining.web_mining.items import FirstItem
from web_mining.web_mining.web_links import load_first_website, load_second_website, load_third_website, \
    load_fourth_website


class FirstSpider(scrapy.Spider):
    """
        This class handle the first spider with the first link
    """
    name = 'first'

    def start_requests(self):
        """"
        This function load the first link, and use it here as a URL
        """
        first_link = load_first_website()
        yield scrapy.Request(url=first_link)

    def parse(self, response):
        """"
        This function extract the data using the xpath selectors
        """
        for row in response.xpath('//*[@id="ratesDateTable"]//tbody/tr'):
            item = FirstItem()
            item['currency'] = row.xpath('td[1]//text()').get()
            item['rate'] = row.xpath('td[2]//text()').get()
            yield item


class SecondSpider(scrapy.Spider):
    """
    This class handle the second spider with the second link
    """
    name = 'second'

    headers = {
        "Accepts": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en;q=0.5",
        "Referer": "https://www.cbn.gov.ng/rates/exchratebycurrency.asp",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        "X-Requested-with": "XMLHttpRequest",
    }

    def start_requests(self):
        """"
        This function load the second link, and use it here as a URL, the header dictionary is also added,
        because the data is json data
        """
        second_link = load_second_website()
        yield scrapy.Request(url=second_link, callback=self.parse, headers=self.headers)

    def parse(self, response):
        """
        The scraped data is loaded and return the json data.
        """
        raw_data = response.body
        data = json.loads(raw_data)
        yield data


class ThirdSpider(scrapy.Spider):
    """
    This class handle the third spider with the third link from the csv file
    """
    name = 'third'

    headers = {
        "Accepts": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en;q=0.5",
        "Referer": "https://ngxgroup.com",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        "X-Requested-with": "XMLHttpRequest",
    }

    def start_requests(self):
        """"
        This function load the third link, and use it here as a URL, the header dictionary is also added,
        because the data is json data
        """
        third_link = load_third_website()
        yield scrapy.Request(url=third_link, callback=self.parse, headers=self.headers)

    def parse(self, response):
        """
        The scraped data is loaded and return the json data.
        """
        raw_data = response.body
        data = json.loads(raw_data)
        return data


class FourthSpider(scrapy.Spider):
    """
        This class handle the fourth spider with the fourth link from the csv file
    """
    name = 'fourth'

    headers = {
        "Accepts": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en;q=0.5",
        "Referer": "https://www.adx.ae/english/Pages/marketwatch.aspx?isdlg=1",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
        "X-Requested-with": "XMLHttpRequest",
    }

    def start_requests(self):
        """"
        This function load the fourth link, and use it here as a URL, the header dictionary is also added,
        because the data is json data
        """
        fourth_link = load_fourth_website()
        yield scrapy.Request(url=fourth_link, callback=self.parse, headers=self.headers)

    def parse(self, response):
        """
        The scraped data is loaded and return the json data.
        """
        raw_data = response.body
        data = json.loads(raw_data)
        return data


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(FirstSpider)
    process.crawl(SecondSpider)
    process.crawl(ThirdSpider)
    process.crawl(FourthSpider)
    process.start()