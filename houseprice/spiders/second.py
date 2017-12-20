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
            print(mixinfo)
            for mi in mixinfo:
                print(mi)
                print(mi.index(u'：'))
                if (mi.__contains__(u'：')):
                    print(mi)
                    print(mi.index('：'))
                    tArea=mi[mi.index('：')+1:]
                else:
                    tstructure=tstructure+mi+'/'
            try:
                item['type'] = p.xpath('div/a[4]/div/i[2]/text()').extract()[0]
            except Exception as e:
                print("avgPrice is null")
                item['type'] = 'unkonw';
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
        try:
            href = response.xpath('//a[@class="next-page next-link"]/@href').extract()[0]
            print('we find----->', href)
            if not r.sismember("spreurl", href):
                print('snexturl add ----->', href)
                r.sadd("snexturl", href)
            while r.scard('snexturl'):
                snexturl = r.spop("snexturl")
                print("snexturl-->", snexturl)
                r.sadd("spreurl", snexturl)
                # next_page = response.urljoin(next_page)   相对连接转绝对连接
                # yield scrapy.Request(next_page, callback=self.parse)
                yield scrapy.Request(snexturl, callback=self.parse)
        except Exception as e:
            print('href----->null')
