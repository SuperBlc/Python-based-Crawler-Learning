# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0]+'post', method='POST')

    def parse(self, response):
        print('Status Code:', response.status)
        print(response.text)
