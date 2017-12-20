# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline
from houseprice.testmysql import *
from houseprice.testredis import *


class HousepricePipeline(object):
    def process_item(self, item, spider):
        print("HousepricePipeline-------->",item)
        saveItem(item)
        return item

    def open_spider(self, spider):
        print("open_spider------------------->",spider)
        clearAll()
        r.sadd("preurl",  "http://gz.centanet.com/xinfang/g1/")
        r.sadd("spreurl", "https://gz.fang.anjuke.com/loupan/all/")

    def close_spider(self, spider):
        print("close_spider------------------->",spider)
