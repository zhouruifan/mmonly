# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


class MmonlyPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        img_split = request.url.split("/")
        filename = str(img_split[-5]) + "_" + str(img_split[-4]) + "_" + str(img_split[-3]) + "_" + str(img_split[-2]) + "_" + str(img_split[-1])
        return filename
