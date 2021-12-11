from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

access_token = ""
access_token_secret =  ""
consumer_key =  ""
consumer_secret =  ""

class StdOutListener(Stream):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
l = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")
