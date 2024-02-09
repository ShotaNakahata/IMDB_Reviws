# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:52:44 2023

@author: Jin
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment_with_other(text, score):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = 'positive'
    elif compound_score <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    if score >= 6 and sentiment == 'positive':
        return 'A'
    elif score >= 6 and sentiment == 'negative':
        return 'B'
    elif score <= 5 and sentiment == 'positive':
        return 'C'
    elif score <= 5 and sentiment == 'negative':
        return 'D'
    else:
        return 'E'

def perform_sentiment_analysis_with_other(input_file, output_file):
    data = pd.read_csv(input_file)
    comments = data['review']
    scores = data['score']

    results = []
    for comment, score in zip(comments, scores):
        sentiment_other = analyze_sentiment_with_other(comment, score)
        results.append(sentiment_other)

    data['mutuality'] = results
    data.to_csv(output_file, index=False)

if __name__ == '__main__':
    input_file = 'output.csv'
    output_file = 'identify.csv'
    perform_sentiment_analysis_with_other(input_file, output_file)
