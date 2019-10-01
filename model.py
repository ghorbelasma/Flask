import pandas as pd
import numpy as np
import nltk
import re
import pickle

nltk.download('wordnet')
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
from nltk.corpus import stopwords

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier



df = pd.read_csv("tweet_data.csv")

df['tweet_lemm'] = [''.join([WordNetLemmatizer().lemmatize(text.lower()) for text in lis]) for lis in df['tweet']]



def preprocess(text_string):
    #space_pattern = '\s+'
    giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
        '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    mention_regex = '@[\w\-]+'
    parsed_text = re.sub(giant_url_regex, '', text_string)
    parsed_text = re.sub(mention_regex, '', parsed_text)
    parsed_text = re.sub('[:"$-_@.&#]+', '', parsed_text)
    parsed_text = re.sub('[0-9]+', '', parsed_text)
    parsed_text = re.sub('(?:&|@)\w*', '', parsed_text)
    return parsed_text


df['tweet_lemm']=df['tweet_lemm'].apply(preprocess)
X=df['tweet_lemm']
Y=df['class']
Y=np.asarray(Y)


pipline=Pipeline(steps=[('TfidfVect', TfidfVectorizer(stop_words="english")),('RF',RandomForestClassifier(n_estimators=20))])
model = pipline.fit(X, Y)
#serializing our model 
pickle.dump(model, open('classifier.pkl','wb'))


