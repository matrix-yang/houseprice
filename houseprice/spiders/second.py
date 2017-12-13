# -*- coding: utf-8 -*-
import scrapy;

from houseprice.items import HousepriceItem
from houseprice.testredis import r


class DmozSpider(scrapy.Spider):
    name = "second"
    allowed_domains = ["anjuke.com"]
    start_urls = [
        "https://gz.fang.anjuke.com/loupan/all/"
    ]

    def parse(self, response):
        listinfo = response.selector.xpath('//div[@class="key-list"]')
        infos = listinfo.xpath('div[@class="item-mod"]')
        for p in infos:
            item = HousepriceItem()
            item['buildName'] = p.xpath('div/a[1]/h3/span/text()').extract()[0]

            mixinfo=p.xpath('div/a[3]/span/text()').extract()
            tstructure=''
            tArea=''
            for mi in mixinfo:
                if (mi.__contains__('：')):
                    tArea=mi[mi.index('：')+1:]
                else:
                    tstructure=tstructure+mi+'/'

            item['type'] = p.xpath('div/a[4]/div/i[2]/text()').extract()[0]
            try:
                item['avgPrice'] = p.xpath('a[2]/p[1]/span/text()').extract()[0]
            except Exception as e:
                print("avgPrice is null")
                item['avgPrice'] = -1;
            item['structure'] = tstructure[:-1]
            item['coveredArea'] = tArea[:-1]
            tlocation=p.xpath('div/a[2]/span/text()').extract()[0]
            item['location'] =''.join(tlocation.split('\xa0'))
            yield item
            print("second--------------------->", item);

