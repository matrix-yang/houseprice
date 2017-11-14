# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline

from houseprice.testredis import r

class HousepricePipeline(object):
    def process_item(self, item, spider):
        print("HousepricePipeline-------->",item)
        return item
    def open_spider(self, spider):
        print(r.get('gender'))
        print("open_spider------------------->",spider)
    def close_spider(self, spider):
        print("close_spider------------------->",spider)