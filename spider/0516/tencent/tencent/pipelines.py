# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class TencentPipeline(object):
    def __init__(self):
        self.file = open('链接.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_text = dict(item)
        textd = json.dumps(dict_text, ensure_ascii=False) + '\n'
        self.file.write(textd)
        return item

    def close_spider(self, spider):
        print('over')
        self.file.close()
