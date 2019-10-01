# Flask
**Sentiment analysis of Twitter messages** .  
This repository provides the necessary files to run a Flask application that classify tweets into 3 labels: 
0 - hate speech 
1 - offensive language 
2 - neither hateful nor offensive

**Step 1:** in your project folder, clone this repository on your machine

```
$ git init
$ git clone https://github.com/ghorbelasma/Flask.git
```
Executing this last line of code might take a moment as the model is training for the first time. A .pkl is created containing the trained model.

**Step 2:** build your docker image (here named "tweet_flask") and run processes in the isolated container. Copy and paste the following command in your terminal:

```
$ docker build --tag=tweet_flask .          
$ docker run -p  12345:12345 tweet_flask
```

**Step 3:** copy the address http://0.0.0.0:12345/ and paste it in your browser

**Step 4:** enter your tweet, click on predict, get the result!
