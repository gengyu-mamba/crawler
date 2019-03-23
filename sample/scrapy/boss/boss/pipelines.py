# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import openpyxl

class BossPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司', '职位', '薪资', '地点-经验-学位', '职位描述'])


    def process_item(self, item, spider):
        line = [item['company'], item['job_title'], item['job_salary'], item['job_info'], item['job_description']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('boss.xlsx')
        self.wb.close()
