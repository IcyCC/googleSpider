# -*- coding:utf-8 -*
from scrapy import cmdline

#main
# num is the nummber of image
#ket is the key word of image
key = raw_input("enter key\n")
num = input("enter num\n")
cmdstr = 'scrapy crawl ImgSpider -a num=%d -a key=%s -o items.json -s IMAGES_STORE=Image/%s'%(num,key,key)
cmdline.execute(cmdstr.split())
