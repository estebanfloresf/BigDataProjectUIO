# -*- coding: utf-8 -*-

import couchdb
import io
from lxml import html
import requests
import numpy as np
import json


class ArticleCrawler:
    def __init__(self,starting_url):
        self.starting_url= starting_url
        self.articles = []


    def crawl (self):
        article = self.getArticInfo(self.starting_url)
        return



    def getArticInfo(self,link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)


        articlestitle = self.cleanLists( tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/a[@class="title"]/text()'))
        articlescontent = self.cleanLists(tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/div[@class="epigraph"]/text()'))
        articlesdate = self.cleanLists(tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/div[@class="publishDate listing-time"]/text()'))
        articleslinks = self.cleanLists(tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/a[@class="title"]/@href'))
        articleemotion = []
        i = 0
        for e in articleslinks:
            articleemotion.append(self.getEmotionsfromLink(articleslinks[i]))
            i += 1


        j=0
        while j<=len(articlestitle)-1:
              try:
                    data = ({'titulo': articlestitle[j], 'contenido': articlescontent[j],
                            'fecha': articlesdate[j], 'emociones': articleemotion[j]})


                    articulo = json.loads(json.dumps(data))
                    doc = db.save(articulo)
                    print("File generated")
              except Exception as e:
                 print(e)
              j += 1






    def cleanLists(self,lista):
        lista = [x.strip() for x in lista]
        lista = [x.replace('\n', '') for x in lista]
        lista = [x.encode('utf8') for x in lista]
        lista = [x.decode('utf8') for x in lista]



        return lista



    def getEmotionsfromLink(self,link):

        url = "http://www.elcomercio.com/"+link
        print(url)
        start_page = requests.get(url)

        tree = html.fromstring(start_page.text)

        # Saco las emociones por cada articulo y limpio
        articlesemotions = self.cleanLists( tree.xpath('//div[@class="two-cols-article"]//*/div[@class="score"]/span/text()'))

        # Transformo la lista a dict
        i = iter(articlesemotions)
        emotions = dict(zip(i, i))

        # Devuelvo las emociones de ese articulo
        return emotions


'''=========CouchDB'=========='''
server = couchdb.Server('http://localhost:5984/')  # ('http://115.146.93.184:5984/')
try:
    db = server.create('articulos')
except:
    db = server['articulos']

crawler = ArticleCrawler("http://www.elcomercio.com/tag/accidentes-de-transito")

crawler.crawl()

for app in crawler.articles:
    print(app)











