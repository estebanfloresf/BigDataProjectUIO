import couchdb

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json



class listener(StreamListener):
    
    def on_data(self, data):

        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print('SAVED' + str(doc))

        except:
            print ("Already exists")
            pass
        return True

    def procesaTweet(tweet):
        for row in tweet:
            # trim y minusculas
            evalTweet = row.strip.lower()
            if "accidente" in evalTweet:
                return True
            else:
                return False

    
    def on_error(self, status):
        print (status)


'''========TWITTER API'=========='''

ckey = "3WhQ2LA3d2fXgZw31HbPu3Wlm"
csecret = "dw6nqXF9KgUO9JMPj64NBxo74m6staB3FN93KiWWMi0HD5tyBz"
atoken = "290182564-hEZTZtWaeL9U8xHrNS46JWQpZ6zCzpX6GPwaLt44"
asecret = "aWWlaYBugOT5QvdcY0qvrmli4zHw3A1HITkdQm5deQCXq"


'''=========CouchDB'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tweet')
except:
    db = server['tweet']
    

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


'''============= ESPECIFICA QUE CUENTAS SEGUIR EN TWITTER============='''


# En caso de requerir por ubicacion
# QUITO-> locations=[-78.58,-0.34,-78.35,-0.01]
#
# Primer id es @WazeTrafficQUI, el segundo de @AMTQUITO,tercero @traficouio y cuarto @ECU911Quito
twitterStream.filter(follow=["3222418195","545416010","201162979","1071624907"], track=['WazeTrafficQUI','AMTQuito',"traficouio","ECU911Quito"])


