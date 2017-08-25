#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from python.items import PythonItem

class TestSpider(Spider):
    name = "test"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;szzf;pn50;ddesc;qsd20160825;qed20170825;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//table[@id="dbtable"]')
        items = []

        for site in sites:
            item = PythonItem()

            code = site.xpath('td/text()').extract()
            name = site.xpath('a/@href').extract()
            date = site.xpath('a/@title').extract()

            item['code'] = [t.encode('utf-8') for t in code]
            item['name'] = [l.encode('utf-8') for l in name]
            item['date'] = [d.encode('utf-8') for d in date]
            items.append(item)

        return items