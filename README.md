# Makri - Malayalam Knowledge Ripper

A highly efficient data scraper with over 80,000 lines of malayalam data, 
which are POS tagged using a SVM algorithm for the creation of database of 
POS tagged lines for the use in Malayalam research and for Scholars.

Feel free to use the POS tagged data in the above files in anyway which doesn't 
violate copyright.


## Technical Details.

The scrapper is build using Scrapy-Python. The `makri-links.py` can be used to collect
links of malayalam articles and `makri-sentences.py` can be used to get malayalam text from
websites and write into files which are divided by category.

The classification algorithm is made using nltk module in python\

A project by Adarsh S and Jithin James under the supervision of ICFOSS under the supervision of Dr. Rajeev RR