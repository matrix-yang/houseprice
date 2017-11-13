import scrapy;
class DmozSpider(scrapy.Spider):
    name = "centanet"
    allowed_domains = ["centanet.com"]
    start_urls = [
        "http://gz.centanet.com/xinfang/"
    ]

    def parse(self, response):
        title=response.selector.xpath('/ html / body / div[6] / div / ul ').extract()
        for p in title:
            #print("============",p)
            location=p.xpath('/li/div/a/@title')
            print("------------------------------------------>",location)
