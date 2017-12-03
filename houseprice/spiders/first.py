# -*- coding: utf-8 -*-
import scrapy;

from houseprice.items import HousepriceItem
from houseprice.testredis import r


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
            try:
                item['avgPrice'] = p.xpath('p[1]/span/span/text()').extract()[0]
            except Exception as e:
                print("avgPrice is null")
                item['avgPrice'] =-1;
            item['structure'] = p.xpath('p[2]/a/text()').extract()[0]
            item['coveredArea'] = p.xpath('p[2]/span/text()').extract()[0]
            item['location'] = p.xpath('p[3]/@title').extract()[0]
            yield item
        div_page_url = response.selector.xpath('/html/body/div[7]/div/div/div')
        hrefs = div_page_url.xpath('a[not(@class)]/@href').extract()
        for u in hrefs:
            u = 'http://gz.centanet.com' + u
            print('we find----->',u)
            if not r.sismember("preurl", u):
                print('nexturl add ----->', u)
                r.sadd("nexturl", u)

        while r.scard('nexturl'):
            nexturl = r.spop("nexturl")
            print("nexturl-->", nexturl)
            r.sadd("preurl", nexturl)
            # next_page = response.urljoin(next_page)   相对连接转绝对连接
            # yield scrapy.Request(next_page, callback=self.parse)
            yield scrapy.Request(nexturl, callback=self.parse)
