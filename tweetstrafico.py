
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "3WhQ2LA3d2fXgZw31HbPu3Wlm"
csecret = "dw6nqXF9KgUO9JMPj64NBxo74m6staB3FN93KiWWMi0HD5tyBz"
atoken = "290182564-hEZTZtWaeL9U8xHrNS46JWQpZ6zCzpX6GPwaLt44"
asecret = "aWWlaYBugOT5QvdcY0qvrmli4zHw3A1HITkdQm5deQCXq"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True

    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('tweetstrafico2')
except:
    db = server['tweetstrafico2']
    
'''===============LOCATIONS=============='''

# Primer id es @WazeTrafficQUI y el segundo de @AMTQUITO

twitterStream.filter(follow=["3222418195","545416010"], track=['WazeTrafficQUI','AMTQuito'])  #QUITO locations=[-78.58,-0.34,-78.35,-0.01]
