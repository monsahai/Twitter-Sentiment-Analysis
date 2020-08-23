from kafka import KafkaConsumer
import json
import elasticsearch
from elasticsearch import Elasticsearch
from textblob import TextBlob
es = Elasticsearch()

def main():
    '''
    main function initiates a kafka consumer, initialize the tweetdata database.
    Consumer consumes tweets from producer extracts features, cleanses the tweet text,
    calculates sentiments and loads the data into postgres database
    '''
    # set-up a Kafka consumer
    consumer = KafkaConsumer("twitter")
    for msg in consumer:

        dict_data = json.loads(msg.value)
        tweet = TextBlob(dict_data["text"])
        print(tweet)
        if tweet.sentiment.polarity > 0:
            senti= 'positive'
        elif tweet.sentiment.polarity == 0:
            senti='neutral'
        else:
            senti= 'negative'
        # add text and sentiment info to elasticsearch
        es.index(index="tweet1",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "sentiment": senti})
        # es.index(index="tweet",
        #          doc_type="test-type",
        #          body={"author": dict_data["user"]["screen_name"],
        #                "date": dict_data["created_at"],
        #                "message": dict_data["text"],
        #                "sentiment": senti})
        print('\n')

if __name__ == "__main__":
    main()