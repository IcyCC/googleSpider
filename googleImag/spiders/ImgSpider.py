# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import  Request
from scrapy.selector import Selector
from googleImag.items import GoogleimagItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from selenium import webdriver
import scrapy
from scrapy.http import Response
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class ImgSpider(Spider):
    name = "ImgSpider"

    def __init__(self, num, key):
        self.Max_num = num
        self.Keyword = key
        self.start_urls = ["https://www.google.com.hk/search?q=%s&safe=strict&hl=zh-CN&biw=1920&bih=899&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj0t_DhxbLQAhXhq1QKHbnbBF8Q_AUIBigB"%(self.Keyword)]

    Img_id = 0

    #BAIDU CODE
    # def dir_parse(self,response):
    #     sites = response.xpath('//*[@id="imgid"]/ul/li')
    #     for x in sites:
    #         items = GoogleimagItem()
    #         items['keyword'] = 'TRAIN'
    #         items['image_urls'] = x.xpath('a/img/@src').extract()
    #         items['images'] = '111'
    #         yield items

    # def parse(self, response):
    #     print 'next page'
    #     d = webdriver.PhantomJS()
    #     d.get(response.url)
    #     d.find_element_by_xpath('//*[@id="page"]/a[10]').click()
    #     return Request(d.current_url, callback=self.dir_parse)
    #     d.close()
    def getNextPage(self,url):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)")
        driver = webdriver.PhantomJS()
        driver.get(url)
        driver.get_screenshot_as_file('01.png')
        driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr/td[12]/a/span[2]').click()
        time.sleep(2)
        driver.get_screenshot_as_file('02.png')
        target = driver.current_url
        driver.quit()
        return target


    def parse(self, response):
        sites = response.xpath('//*[@id="ires"]/table/tr')
        for li in sites:
            td = li.xpath('td')
            for x in td:
                items = GoogleimagItem()
                items['keyword'] = self.Keyword
                items['image_urls'] = x.xpath('a/img/@src').extract()
                tmp = x.xpath('a')
                items['describe'] = tmp.xpath('string(.)').extract()
                self.Img_id = self.Img_id + 1
                items['id'] = self.Img_id
                yield items
        if self.Img_id < self.Max_num:
            yield Request(url = self.getNextPage(response.url))
        else:
            yield None

