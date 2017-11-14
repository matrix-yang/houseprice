import scrapy;

from houseprice.items import HousepriceItem


class DmozSpider(scrapy.Spider):
    name = "centanet"
    allowed_domains = ["centanet.com"]
    start_urls = [
        "http://gz.centanet.com/xinfang/"
    ]

    def parse(self, response):
        title = response.selector.xpath('/ html / body / div[6] / div / ul /li')
        for p in title:
            item = HousepriceItem()
            item['buildName'] = p.xpath('div/a/@title').extract()[0]
            item['type'] = p.xpath('div/h5/label/text()').extract()[0]
            item['avgPrice'] = p.xpath('p[1]/span/span/text()').extract()[0]
            item['structure'] = p.xpath('p[2]/a/text()').extract()[0]
            item['coveredArea'] = p.xpath('p[2]/span/text()').extract()[0]
            item['location'] = p.xpath('p[3]/@title').extract()[0]
            yield item
            #print("------------------------------------------>",item)

        next_page_url = response.selector.xpath('/ html / body / div[7] / div / div / div')
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
