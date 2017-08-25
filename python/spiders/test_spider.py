#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector

class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码