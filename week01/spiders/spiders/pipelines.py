# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline(object):
    def process_item(self, item, spider):

        name = item['movieName']
        type = item['movieType']
        time = item['movieShowTime']

        output = "{} {} {}".format(name, type, time)

        with open('./movie2.csv', 'a+', encoding='utf8') as f:
            f.write(output)

        return item