from scrapy.spiders import Spider
#from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from myproj.items import  MainList, SubList

class MySpider(Spider):
    '''
    scrape the titles
    '''
    name = "manythings"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/']

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//ul/li/b/text()")
        print(">>> Number of titles")
        print(len(titles))
        for titles in titles:
            title = titles.extract()
            print(title)


class MySpider2(Spider):
    '''
    scrape the titles and the subtitles
    '''
    name = "manythings2"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/']

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//ul/li/b/text()")
        print(">>> Number of titles")
        L = []
        for titles in titles:
            mainlist = MainList()
            mainlist['title'] = titles.extract()
            L.append(mainlist)
        return L



class MySpider3(Spider):
    '''
    scrape the titles and the subtitles
    '''
    name = "manythings3"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/']

    def parse(self, response):
        #hxs = Selector(response)
        mains = response.xpath("//div//ul/li")
        print(">>> ITEM INFO")
        print(mains[0].xpath('b').extract())
        print(mains[0].xpath('.//ul/li').extract())
        print(mains[0].xpath('.//ul/li')[0].extract())
        L = []
        for index, main in enumerate(mains):
            mainlist = MainList()
            mainlist['title'] = main.xpath('b').extract()
            sublist = []
            for subtitle in main.xpath('.//ul/li'):
                asub = SubList()
                sub_title = subtitle.xpath('a/text()').extract()
                sub_url = subtitle.xpath('a/@href').extract()
                asub['title'] = sub_title
                try:
                    asub['url'] = 'http://www.manythings.org/vocabulary/lists/c/' + sub_url[0]
                except:
                    asub['url'] = ''
                sublist.append(asub)
            mainlist['sublist'] = sublist
            L.append(mainlist)
            #print(main.xpath('.//b/text()').extract())
            #print(len(subtitles))
            #print(main.xpath('//b/text()').extract())
            #L.append(subtitles)
            
        return L