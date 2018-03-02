from scrapy.spiders import Spider
#from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector

class MySpider(Spider):
    name = "manythings"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/']

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        hxs = Selector(response)
        titles = hxs.xpath("//ul/li/b/text()")
        print(">>> Number of titles")
        print(len(titles))
        for titles in titles:
            title = titles.extract()
            print(title)

