
#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import pickle
import json
from bs4 import BeautifulSoup, SoupStrainer


class MakriSpider(scrapy.Spider):
    name = "makri_spider"
    urls = [
        'http://www.deshabhimani.com/news/national',
    ]

    def start_requests(self):
        # with open("test.txt", "rb") as fp:
        #     urls = pickle.load(fp)
        # print(urls)
        for url in self.urls[:1]:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body,"lxml")
        links1 = soup.findAll("div", {"class": "lead-news"})
        links2 = soup.findAll("div", {"class": "db-bx"})
        print(links2)