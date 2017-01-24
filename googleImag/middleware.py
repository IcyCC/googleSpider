from scrapy.utils.project import get_project_settings
import random
from selenium import webdriver
from scrapy.http import Response
from scrapy.http import HtmlResponse
import time
settings = get_project_settings()

class ProcessHeaderMidware(object):
    """process request add request info"""

    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        spider.logger.info(msg='now entring download midware')
        if ua:
            request.headers['User-Agent'] = ua
            # Add desired logging message here.
            spider.logger.info(
                u'User-Agent is : {} {}'.format(request.headers.get('User-Agent'), request)
            )
        pass

class JavaScriptMiddleware(object):

    def process_request(self, request, spider):
        print "P is starting..."
        driver = webdriver.PhantomJS()
        #driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(3)
        body = driver.page_source
        spider.logger.info(
             'JavaScriptMiddleware  Runs'
         )
        #driver.close()
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8')


