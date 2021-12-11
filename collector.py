from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

access_token = "2959043404-U8CpMLNo0AeKSRuh7U6j1Z4EIdF3j1sbOhsNNcX"
access_token_secret =  "28KrXujhu4bhBWr8AswbkrpRctQBufpwQGSbGDo6r5Pdg"
consumer_key =  "kEJJ0fmzlRojbxhiIaUAx7yf7"
consumer_secret =  "CubNyDlkN2tfaeUGU84iw3vXbYuIq4HuzQAhpUkxYIgijue966"

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
