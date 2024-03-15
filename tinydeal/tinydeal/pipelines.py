# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class TinydealPipeline:
    def process_item(self, item, spider):
        for key in item:
            if isinstance(item[key], str):
                item[key] = re.sub(r'\s+', ' ', item[key].replace(u'\xa0', ' '))
        return item
