import tweepy
from kafka import KafkaProducer

bearer_token = ""

client = tweepy.Client(bearer_token=bearer_token)

query = 'navidad -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], user_fields=['profile_image_url'], expansions='author_id', max_results=100)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
counter = 0
print("Tamanho: " + str(len(tweets.data)))

for tweet in tweets.data:
    counter = counter + 1
    text = "\n 3." + str(counter) + " ------------\n" + str(tweet)
    print(text)
    producer.send("navidad2", text.encode())
