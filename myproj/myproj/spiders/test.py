from scrapy.spiders import Spider
from scrapy.http import Request
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
            main_title = main.xpath('b/text()').extract()
            try:
                mainlist['title'] = main_title[0]
                sublist = []
                for subtitle in main.xpath('.//ul/li'):
                    asub = SubList()
                    sub_title = subtitle.xpath('a/text()').extract()
                    sub_url = subtitle.xpath('a/@href').extract()
                    try:
                        asub['title'] = sub_title[0]
                        try:
                            asub['url'] = 'http://www.manythings.org/vocabulary/lists/c/' + sub_url[0]
                        except:
                            asub['url'] = ''
                        sublist.append(asub)
                    except:
                        pass
                mainlist['sublist'] = sublist
                L.append(mainlist)
            except:
                pass
          
           
            
            #print(main.xpath('.//b/text()').extract())
            #print(len(subtitles))
            #print(main.xpath('//b/text()').extract())
            #L.append(subtitles)
            
        return L



class MySpider4(Spider):
    '''
    scrape the titles and the subtitles
    '''
    name = "manythings4"
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
            main_title = main.xpath('b/text()').extract()
            try:
                mainlist['title'] = main_title[0]
                sublist = []
                for subtitle in main.xpath('.//ul/li'):
                    asub = SubList()
                    sub_title = subtitle.xpath('a/text()').extract()
                    sub_url = subtitle.xpath('a/@href').extract()
                    try:
                        asub['title'] = sub_title[0]
                        try:
                            asub['url'] = 'http://www.manythings.org/vocabulary/lists/c/' + sub_url[0]
                            if asub['url'] is not None:
                                asub['wordlist'] = self.parseWords(asub['url'])
                        except:
                            asub['url'] = ''
                        sublist.append(asub)
                    except:
                        pass
                mainlist['sublist'] = sublist
                L.append(mainlist)
            except:
                pass         
        return L

    def parseWords(self, url):
        return ['foo']


class MySpider5(Spider):
    '''
    scrape the titles and the subtitles
    '''
    name = "wordlist"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/words.php?f=animals_farm']

    def parse(self, response):
        words = response.xpath('//div[contains(@class, "co")]/ul/li/text()')
        print(">>>> ITEMS")
        wordlist = []
        for w in words:
            wordlist.append(w)
        return wordlist



class MySpider5(Spider):
    '''
    scrape the titles and the subtitles
    '''
    name = "words1"
    allowed_domains = ['manythings.org']
    start_urls = ['http://www.manythings.org/vocabulary/lists/c/']

    def parse(self, response):
        #hxs = Selector(response)
        mains = response.xpath("//div//ul/li")
        print(">>> ITEM INFO")
        L = []
        for index, main in enumerate(mains):
            mainlist = {}
            main_title = main.xpath('b/text()').extract()
            try:
                mainlist['title'] = main_title[0]
                sublist = []
                for subtitle in main.xpath('.//ul/li'):
                    asub = {}
                    sub_title = subtitle.xpath('a/text()').extract()
                    sub_url = subtitle.xpath('a/@href').extract()
                    try:
                        asub['title'] = sub_title[0]
                        try:
                            asub['url'] = 'http://www.manythings.org/vocabulary/lists/c/' + sub_url[0]
                        except:
                            asub['url'] = ''
                        sublist.append(asub)
                    except:
                        pass
                mainlist['sublist'] = sublist
                L.append(mainlist)
            except:
                pass         
        for item in L:
            print(item)
        return L

    def parseWords(self, url):
        return ['foo']