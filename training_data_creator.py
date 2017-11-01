#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import codecs
from bs4 import BeautifulSoup


URL = "http://www.iiitmk.ac.in/MalayalamPOSTagger/"
CORPUS = 'corpus/'
driver = webdriver.Chrome("/usr/bin/chromedriver_linux64/chromedriver")
driver.get(URL)
assert "Malayalam" in driver.title

dirList = [x[0] for x in os.walk("./Data")]    
dirList = dirList[2:]

for domains in dirList:
	if not os.path.exists(CORPUS):
		os.makedirs(CORPUS)
	with open(CORPUS+domains.split('/')[2], "wb") as f:
		s = ''
		for files in os.listdir(domains):
			file = codecs.open(domains+"/"+files,encoding='utf-8')
			print("printing file: "+domains+"/"+files)
			textArea = driver.find_element_by_id("mal_text")
			textArea.clear()
			for (i,line) in enumerate(file):
				if i < 8:
					continue
				textArea.send_keys(line)
			button = driver.find_element_by_xpath("//input[@value='Tag The Sentence']")
			button.click()
			page_source = driver.page_source
			soup = BeautifulSoup(page_source, 'html.parser') 
			for line in soup.find_all(attrs ={"size":"3"}):
				print(line.string)
				s+=line.string+'\n'
		f.write(s.encode("UTF-8"))
