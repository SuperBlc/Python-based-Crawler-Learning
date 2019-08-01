# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                          'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                          'Chrome/75.0.3770.142 Safari/537.36'
        }
    }

    def __init__(self, category=None, *args, **kwargs):
        super(BaiduSpider, self).__init__(*args, **kwargs)
        self.category = category
        self.logger.info(self.category)

    def parse(self, response):
        self.logger.info(self.category)
