# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FsmnSpider(CrawlSpider):
    name = 'fsmn'
    allowed_domains = ['mmonly.cc']
    start_urls = ['http://www.mmonly.cc/tag/fsmn/']
    image_urls = []
    rules = (
        Rule(LinkExtractor(allow=r'http://www.mmonly.cc/.*/.*/\d{1,6}.html',
                           deny=r'http://www.mmonly.cc/.*/.*/.*\[_\].*.html'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 取最大页数，只取数字
        page_num = re.sub("\D", "", response.xpath("//div[@class='pages']/ul/li[1]/a/text()").extract_first())
        for num in range(1, int(page_num)):
            img_url = str(response.url[:-5]) + "_" + str(num) + ".html"
            yield Request(img_url, callback=self.parse_img)
        yield {"image_urls": self.image_urls}

    def parse_img(self, response):
        img_urls = response.xpath("//div[@id='big-pic']/descendant::img/@src").extract()
        for url in img_urls:
            self.image_urls.append(url)
