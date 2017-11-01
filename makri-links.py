
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
        'http://www.deshabhimani.com/news/kerala',
        'http://www.deshabhimani.com/news/national',
        'http://www.deshabhimani.com/news/world',
        'http://www.deshabhimani.com/editorial',
        'http://www.deshabhimani.com/articles',
        'http://www.deshabhimani.com/columns',
        'http://www.deshabhimani.com/news/sports',
        'http://www.deshabhimani.com/cinema',
        'http://www.deshabhimani.com/from-the-net',
        'http://www.deshabhimani.com/art-stage',
        'http://www.deshabhimani.com/epaper/',
        'http://www.deshabhimani.com/news/pravasi',
        'http://www.deshabhimani.com/education',
        'http://www.deshabhimani.com/health',
        'http://www.deshabhimani.com/news/vehicle',
        'http://www.deshabhimani.com/books',
        'http://www.deshabhimani.com/news/technology',
        'http://www.deshabhimani.com/music',
        'http://www.deshabhimani.com/travel',
        'http://www.deshabhimani.com/women',
        'http://www.deshabhimani.com/life-style',
        'http://www.deshabhimani.com/news/business',
        'http://www.deshabhimani.com/agriculture',
        'http://www.deshabhimani.com/cartoon',
        'http://www.deshabhimani.com/news/career',
    ]

    def start_requests(self):
        with open("test1.txt", "wb") as fp:
            pickle.dump([], fp)
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = []
        with open("test1.txt", "rb") as fp:
            links = pickle.load(fp)
        soup = BeautifulSoup(response.body, "lxml")
        links1 = soup.findAll("div", {"class": "lead-news"})
        links2 = soup.find("div", {"class": "db-bx"}).findAll("li")
        for link in links1:
        	links.append(link.find("a").attrs['href'])
        for i, link in enumerate(links2):
        	if i<10:
        		links.append(link.find("a").attrs['href'])
        print(links)
        with open("test1.txt", "wb") as fp:
            pickle.dump(links, fp)