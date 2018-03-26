# Makri - Malayalam Knowledge Ripper

Makri is a POSTagger built with [RDRPOSTagger](https://github.com/datquocnguyen/RDRPOSTagger) which was trained with over 80,000 lines of POS Tagged Silver Corpus.

## Details.

The scrapper is build using Scrapy-Python. The `makri-links.py` can be used to collect
links of malayalam articles and `makri-sentences.py` can be used to get malayalam text from
websites and write into files which are divided by category.

A project by Adarsh S and Jithin James under the supervision of ICFOSS under the supervision of Dr. Rajeev RR

## FOSSASIA Talk

[Tamil NLP creator and talk mentor Ashok R](https://github.com/AshokR/)

[Slides](https://docs.google.com/presentation/d/1A1n1HqGkXPgyarPUB91tb208IGt2KuKqj5umgUCw5Uw/edit?usp=sharing)

[BLARK Ideology](http://www.elsnet.org/dox/krauwer-specom2003.pdf)

[Language Resource Classification](http://ixa.si.ehu.es/sites/default/files/dokumentuak/3855/LEIPZIG_2014_Sarasola.pdf)

[Language Statistics Data](https://economictimes.indiatimes.com/tech/internet/how-online-vernacular-market-is-becoming-the-big-battle-ground-for-tech-cos/articleshow/63248994.cms)

## Web App

A Django based web app is built to distribute the service.
The development server can be accessed via
<code>python2 manage.py runserver</code>

The web app has an input text option for live data tagging, an upload file option to tag text files.

The sevice also has a web end-point to use in other applications.

<code>curl -G -v  "http://127.0.0.1:8000/" --data-urlencode "q=input" </code> will return the tagged data for the given input.

## Team Members

@isht3, @jjmachan -- creators of the project
@abinmn -- deployable web app creator
