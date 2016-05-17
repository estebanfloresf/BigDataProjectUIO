#Ejemplo de Diego

from lxml import html
import couchdb

import json

import requests

page = requests.get('http://www.elcomercio.com/tendencias/meridianaecuador-exposicion-centroculturalmetropolitano-misiongeodesica.html')
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//p[@id="m67-1-68"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
print 'Texto: ', buyers
#print 'Prices: ', pricess


