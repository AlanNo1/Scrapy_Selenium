# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
class ToutiaoPipeline(object):
    def open_spider(self,spider):
        self.df_list = []

    def process_item(self, item, spider):
        self.df_list.append(dict(item))
        return item

    def close_spider(self,spider):
        df_new = pd.concat([pd.DataFrame(self.df_list),pd.read_excel(r'C:\Users\19248\Desktop\汽车之家通用模块\toutiao\数据文件.xlsx')],ignore_index=True).\
        drop_duplicates(subset=['PageUrl','TitleXpath'],keep='first',inplace=False).to_excel(r'C:\Users\19248\Desktop\汽车之家通用模块\toutiao\数据文件.xlsx',index=False)
        spider.driver.close()


