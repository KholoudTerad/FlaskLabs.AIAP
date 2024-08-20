# FlaskLabs.AIAP
Lab 5

to get "Hello John!":
http://127.0.0.1:5000/hello/John 

to get "blog NO. 121!":
http://127.0.0.1:5000/hello/121 


FlaskTweetApp using postman

Accepts a tweet from the user:
POST / http://192.168.100.2:5000/add_tweet
INPUT: {"content": "kholoud","date":"18/3/2024", "id": "3"}

Returns tweets that have a specific date given as a parameter:
GET / http://192.168.100.2:5000/tweets_by_date?date=17-02-2024

Accepts a tweet from the user:
POST / http://192.168.100.2:5000/add_tweet
INPUT: {"content": "kholoud","date":"18/3/2024", "id": "3"}

Accepts a tweet from the user and classifies it using the HuggingFace model:
POST / http://192.168.100.2:5000/classify_tweet
INPUT: {"content": "i am happy"}
