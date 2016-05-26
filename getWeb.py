
from lxml import html
import requests
import numpy as np


class AppCrawler:
    def __init__(self,starting_url,depth):
            self.starting_url= starting_url
            self.depth = depth
            self.articles = []

    def crawl (self):
        self.getAppfromLink(self.starting_url)
        return

    def getAppfromLink(self,link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        #Aqui saco los articulos de la pagina de El Comercio - Accidentes

        articlestitle = tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/a[@class="title"]/text()')
        articlescontent = tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/div[@class="epigraph"]/text()')
        articleslink = tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/a[@class="title"]/@href')
        articlesdate = tree.xpath('//div[@class="col-md-8 col-sm-12-col-xs-12 col-responsive"]//*/div[@class="publishDate listing-time"]/@text()')


#       articleslen = np.arange(len(articlestitle))
        for content in articlesdate:
            print(content)




class App:
    def __init__(self,articlename, description, date, links):
        self.name = articlename
        self.description =description
        self.date=date
        self.links=links

    def __str__(self):
        return ("Articulo: "+ self.name.encode('UTF-8') +
                "\r\n Descripcion: "+ self.description.encode('UTF-8')+
                "\r\n Fecha: " + self.date.encode('UTF-8')+ "\r\n")



crawler = AppCrawler("http://www.elcomercio.com/tag/accidentes-de-transito",2)
crawler.crawl()

for app in crawler.articles:
        print(app)











