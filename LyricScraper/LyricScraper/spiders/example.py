from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
class QuotesSpiderSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.lyrics.com/genres.php?genre=Rock&p=1']
    i=1

    def parse(self, response):
        print('Processing..' + response.url)
        self.i=self.i+1

        links = response.xpath("//p[@class='lyric-meta-title']/a/@href")
        for link in links:
            yield {'link': 'https://www.lyrics.com/'+link.extract()}

        next_page_url = 'https://www.lyrics.com/genres.php?genre=Rock&p='+str(self.i)
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)