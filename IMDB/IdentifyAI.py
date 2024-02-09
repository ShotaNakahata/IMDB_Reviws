# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:25:48 2023

@author: C1
"""
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = 'positive'
    elif compound_score <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

def perform_sentiment_analysis(input_file, output_file):
    data = pd.read_csv(input_file)
    comments = data['review']

    results = []
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        results.append(sentiment)

    data['sentiment'] = results
    data.to_csv(output_file, index=False)
    



if __name__ == '__main__':
    input_file = 'imdb_reviews.csv'
    output_file = 'output.csv'
    perform_sentiment_analysis(input_file, output_file)
