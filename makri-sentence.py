#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import os
import pickle
import re
import scrapy

"""
    Write each article onto a separate file on the category folder.
"""


class MakriSpider(scrapy.Spider):
    name = "makri_spider"

    DIRECTORY = 'Data/{}/'

    def article_category(self):
        div = self.soup.findAll("div", {"class": "col-md-2 col-sm-2 col-xs-12"})[0]
        a = div.findAll("a")[0].text
        return a

    def check_directory(self):
        folder = self.DIRECTORY.format(self.category)
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def article_body(self):
        return self.soup.select(".articleBody")[0]

    def start_requests(self):
        urls = []
        with open("test.txt", "rb") as fp:
            urls = pickle.load(fp)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.soup = BeautifulSoup(response.body, "lxml")
        div = self.article_body()
        self.category = self.article_category()
        DIR = self.check_directory()
        data_str = div.text.encode('utf-8')
        sentences = re.split('[?.!]', data_str)

        number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        DIR = DIR+str(number+1)+".txt"
        open(DIR, 'w+')

        prefix = """\
                    \n-----------------------------------\
                    \n\nDomain: {}\
                    \n\nPaper: {}\
                    \n\n-----------------------------------\
                 """.format(self.category, "Mathrubhumi")

        with open(DIR, "a") as fp:
            fp.write(prefix)
            post = ""
            for i, sentence in enumerate(sentences):
                if sentences[i+1][0] == " ":
                    fp.write(sentence+" .\n\n")
                else:
                    fp.write(sentence+" .")
