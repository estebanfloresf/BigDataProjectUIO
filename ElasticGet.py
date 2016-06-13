# -*- coding: utf-8 -*-

import elasticsearch
import csv
import random
import pandas as pd
import json

# replace with the IP address of your Elasticsearch node
es = elasticsearch.Elasticsearch(["http://localhost:9200"])

# Replace the following Query with your own Elastic Search Query
res = es.search(index="finalindex", body=
{"query":
    {
        "bool": {
            "must": [
                {"match": {
                    "text": "accidente, transito, congestion vehicular,choque, atropellado, colision, trafico, transito, accidentes, choques, atropellados, vehiculos, peaton, peatones"}}

                 , {"range": { "created_at": {"gte":"2016-01-01", "lte":"2016-06-10" }}},


            ]
        }
    }
},
                size=2000)  # this is the number of rows to return from the query... to get all queries, run script, see total number of hits, then set euqual to number >= total hits

random.seed(1)
sample = res['hits']['hits']
# comment previous line, and un-comment next line for a random sample instead
# randomsample = random.sample(res['hits']['hits'], 5);  #change int to RANDOMLY SAMPLE a certain number of rows from your query

print("Got %d Hits" % res['hits']['total'])

ind = []
texto = []
place = []
coord = []
created=[]
name=[]
for hit in sample:
    ind.append(hit['_id'])
    texto.append(hit["_source"]["text"].encode('utf-8'))
    created.append(hit["_source"]["created_at"])
    name.append(hit["_source"]["user"]["name"].encode('utf-8'))
    coord.append(hit["_source"]["place"])


fcoor = []
for c in coord:
    try:


        fcoor.append(c["bounding_box"]["coordinates"])

    except: fcoor.append("0,0,0,0")




df = pd.DataFrame({'id':ind ,'text':texto,'created_at':created,'name':name,'coordinates':fcoor})
try:
    df.to_csv('Documents/tweets.csv')
    short_list = df.to_json('Documents/tweets.json',orient="records") #Agregar la linea   { "docs": [ todo el documento aqui ] }"
    print("Archivo generado")
except Exception as e:\
    print(e)




