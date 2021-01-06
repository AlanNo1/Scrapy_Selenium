from scrapy import Request
from scrapy.spiders import Spider
from toutiao.items import ToutiaoItem
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import pandas as pd
from configparser import ConfigParser
class ToutiaoSpider(Spider):
    name = 'toutiao'
    pageurl = ''
    xpaths = ''
    df = pd.read_excel(r'C:\Users\19248\Desktop\汽车之家通用模块\toutiao\数据文件.xlsx',names=None)
    def __init__(self):
        option = ChromeOptions()
        #option.add_argument('--headless')
        #option.add_argument('--disable-gpu')
        #option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = Chrome(options=option)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    #获取初始Request
    def start_requests(self):
        for (self.pageurl,self.xpaths) in zip(self.df['PageUrl'],self.df['TitleXpath']):
            #生成请求对象，设置url
            yield Request(self.pageurl,meta={'urls':self.pageurl,'xpaths':self.xpaths})
            # 数
    def parse(self, response):
        item = ToutiaoItem()
        #获取爬取的URL
        item['PageUrl'] = response.meta['urls']
        #获取数据标题Xpath
        item['TitleXpath'] = response.meta['xpaths']
        #获取数据标题
        item['Title'] = response.xpath(response.meta['xpaths']).extract_first()
        yield item
    

