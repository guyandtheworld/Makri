
#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import pickle
import json
from bs4 import BeautifulSoup


class MakriSpider(scrapy.Spider):
    name = "makri_spider"
    urls = [
        'http://www.manoramaonline.com/news.html',
        'http://www.manoramaonline.com/movies.html',
        'http://www.manoramaonline.com/technology.html',
        'http://www.manoramaonline.com/sports.html',
        'http://www.manoramaonline.com/style.html',
        'http://www.manoramaonline.com/astrology.html',
        'http://www.manoramaonline.com/health.html',
        'http://www.manoramaonline.com/fasttrack.html',
        'http://www.manoramaonline.com/music.html',
        'http://www.manoramaonline.com/women.html',
        'http://www.manoramaonline.com/homestyle.html',
        'http://www.manoramaonline.com/environment.html',
        'http://www.manoramaonline.com/travel.html',
        'http://www.manoramaonline.com/children.html',
        'http://www.manoramaonline.com/literature.html',
        'http://www.manoramaonline.com/education.html',
        'http://www.manoramaonline.com/karshakasree.html',
    ]

    def start_requests(self):
        # with open("test.txt", "rb") as fp:
        #     urls = pickle.load(fp)
        # print(urls)
        for url in self.urls[:1]:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        print(soup)