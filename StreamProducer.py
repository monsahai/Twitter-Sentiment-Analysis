import kafka
from kafka import KafkaProducer
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# TWITTER API CONFIGURATIONScd
consumer_key = "hc8VcrP0FhSbs5h7K7otfc3RR"
consumer_secret = "o235lAM9vCKvVdGJB62TfXdGe357hs4UsBvb26cOFaLcwUffLj"
access_token = "137097962-oKB5TwVJh9Az5V9bhEbCiF0YzrgIeL6GriSc1ea9"
access_secret = "m8a1lyLXg0PRrwKhWRohGWJoHIHNn15QyL923XNxqb3Ck"

# TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Get Producer that has topic name is Twitter
    # self.producer = self.client.topics[bytes("twitter")].get_producer()

    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("twitter", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True


# Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

# Produce Data that has trump hashtag (Tweets)
twitter_stream.filter(track=['#coronavirus'])
# twitter_stream.filter(track=['#trump'])