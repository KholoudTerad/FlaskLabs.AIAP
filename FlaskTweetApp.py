from flask import Flask, jsonify, request
from transformers import pipeline
import torch

# declare flask and define app using Flask
app = Flask("sentiment_analysis")

tweets = {"tweets": [
                    {'content': 'dont know what todo', 
                      'date': '17-02-2024', 
                      'id': '1'},
                    {'content': 'doing flask', 
                      'date': '16-03-2024', 
                      'id': '2'}
                    ]
        }
sentiment_pipe = pipeline("sentiment-analysis",
                              model="siebert/sentiment-roberta-large-english")
print(sentiment_pipe("this is a test"))

@app.route("/")
def hello():
    return "Hello!"

@app.route('/tweet', methods=['GET'])
def return_all_tweets():
    return jsonify(tweets)

#POST / http://192.168.100.2:5000/add_tweet
#INPUT: {"content": "kholoud","date":"18/3/2024", "id": "3"}
@app.route('/add_tweet', methods=['POST'])
def add_tweet():
    tweet = {
                "content": request.json["content"],
                "date": request.json["date"], 
                "id": request.json["id"]
            }
    tweets["tweets"].append(tweet)
    return jsonify(tweets)



# GET / http://192.168.100.2:5000/tweets_by_date?date=17-02-2024
@app.route('/tweets_by_date', methods=['GET', 'POST'])
def return_tweets_by_date():
    if request.method == 'GET':
        date = request.args.get('date')
    elif request.method == 'POST':
        date = request.json.get('date')

    filtered_tweets = [tweet for tweet in tweets['tweets'] if tweet['date'] == date]
    return jsonify({"tweets": filtered_tweets})



@app.route('/classify_tweet', methods=['POST'])
def classify_tweet():
    sentiment_pipe = pipeline("sentiment-analysis",
                              model="siebert/sentiment-roberta-large-english")
    return jsonify(sentiment_pipe(request.json["content"]))


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)




