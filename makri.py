#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import pickle
import json
from bs4 import BeautifulSoup


class MakriSpider(scrapy.Spider):
    name = "makri_spider"

    start_urls = ['http://www.mathrubhumi.com/technology/science/electron-microscope-detection-of-virus-microscope-1.2044131']


    # def start_requests(self):
    #     urls = []
        # with open("test.txt", "rb") as fp:
        #     urls = pickle.load(fp)
        # print(urls)
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = {}
        with open("ml-dict.json", "r") as fp:
            data = json.load(fp)
        soup = BeautifulSoup(response.body, "lxml")
        div = soup.select(".articleBody")[0]
        data_str = div.text.encode('utf-8')
        words = data_str.split(" ")
        for word in words:
            if word.isupper() or word.islower():
                pass
            elif " " in word:
                pass
            else:
                word = word.replace("(","")
                word = word.replace(")","")
                word = word.replace(".","")
                word = word.replace("\"","")
                word = word.replace("'","")
                word = word.replace(" ","")
                word = word.replace("\n", "")
                data[unicode(word, "utf-8")] = 1
        my_dict = json.dumps(data, ensure_ascii=False).encode('utf8')
        print(my_dict)
        with open("ml-dict.json", "w") as fp:
            json.dump(my_dict, fp, ensure_ascii=False).encode('utf8')
