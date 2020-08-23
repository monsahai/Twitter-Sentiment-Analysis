# Twitter Sentiment Aanalysis
 Twitter Sentiment Aanalysis
 
 Spark Streaming and Visualization
 
 I have used the following framework Apache Spark
 Streaming, Kafka (optional), Elastic, and Kibana. 
 The framework performs SENTIMENT analysis of particular hash tags in twitter data in real-time. 
 For example, we want to do the sentiment analysis for all the tweets for #trump, #coronavirus. 
 
 
 The above framework has the following components:
 
 1. Scrapper
 The scrapper will collect all tweets and sends them to Kafka for analytics.
 a. Collecting tweets in real-time with particular hash tags. For example, we
 will collect all tweets with #trump, #coronavirus.
 b. After filtering, send them to Kafka.
 c. Use Kafka API (producer) in your program
 (https://kafka.apache.org/090/documentation.html#producerapi)
 d. The scrapper program will run infinitely and takes hash tag as input parameter while running.
 
 2. Kafka
 Installed Kafka and ran Kafka Server with Zookeeper. Created a dedicated channel/topic for data transport
 
 3. Spark Streaming
 In Spark Streaming, created a Kafka consumer  and periodically collect filtered tweets from scrapper. For each hash tag, perform sentiment analysis
 using Sentiment Analyzing tool.
 
 3. Sentiment Analyzer
 Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It's also known as opinion mining, deriving the opinion or attitude of a speaker.
 For example,
 
 “President Donald Trump approaches his first big test this week from a
 position of unusual weakness.” - has positive sentiment.
 
 “Trump has the lowest standing in public opinion of any new president in
 modern history.” - has neutral sentiment.
 
 “Trump has displayed little interest in the policy itself, casting it as a
 thankless chore to be done before getting to tax-cut legislation he values
 more.” - has negative sentiment.
 
 The above examples are taken from CNBC news:
 http://www.cnbc.com/2017/03/22/trumps-first-big-test-comes-as-hes-in-an-
 unusual-position-of-weakness.html
 
 
 4. Elasticsearch
 Installed the Elasticsearch and ran it to store the tweets and their sentiment information for further visualization purpose.
 You can point http://localhost:9200 to check if it’s running.
 
 5. Kibana
 Kibana is a visualization tool that can explore the data stored in elasticsearch. Used the visualization tool to show your tweets sentiment classification result in a real-time manner. 

