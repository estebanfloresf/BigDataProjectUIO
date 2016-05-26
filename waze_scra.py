from lxml import html
import couchdb
import json
import requests
import urllib2


url = "http://localhost:8080/waze/traffic-notifications?lonLeft=-78.614044&lonRight=-78.321533&latTop=-0.35362&latBottom=-0.054245"
data = json.load(urllib2.urlopen(url))
#print 'Texto: ', data
server = couchdb.Server('http://localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('waze')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['waze']
db.save(data) #Aqui se guarda  en la base de couchDB           
#Setear la URL del servidor de couchDB