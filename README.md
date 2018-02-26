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

# Web App
A Django based web app is built to distribute the service.
The development server can be accessed via
<code>python2 manage.py runserver</code>

The web app has an input text option for live data tagging, an upload file option to tag text files.

The sevice also has a web end-point to use in other applications.

<code>curl -G -v  "http://127.0.0.1:8000/" --data-urlencode "q=input" </code> will return the tagged data for the given input.

# Team Members

@isht3, @jjmachan -- creators of the project
@abinmn -- deployable web app creator
