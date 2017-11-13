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
            buildName=p.xpath('/li/div/a/@title')
            type=p.xpath('/li/div/h5/label').extract()
            avgPrice = p.xpath('/li/p[1]/span/span').extract()
            structure=p.xpath('/li/p[2]/a').extract()
            coveredArea=p.xpath('/li/p[2]/span').extract()
            location=p.xpath('/li/p[3]/@title')
            print("------------------------------------------>",location)
