# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:25:11 2023

@author: C1
"""
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.imdb.com/title/tt9603212/reviews?ref_=tt_urv'

def get_reviews(url, num_reviews=25):
    reviews = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews.extend(soup.find_all('div', {'class': 'review-container'})[:num_reviews])

    return reviews

def write_to_csv(reviews):
    with open('imdb_reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'score', 'review']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for review in reviews:
            title = review.find('a', {'class': 'title'}).text.strip()
            rating_element = review.find('span', {'class': 'rating-other-user-rating'})
            rating = rating_element.find('span').text.strip() if rating_element else 'N/A'
            review_text = review.find('div', {'class': 'text'}).text.strip()

            writer.writerow({'title': title, 'score': rating, 'review': review_text})

if __name__ == '__main__':
    num_reviews = 25
    reviews = get_reviews(url, num_reviews)
    write_to_csv(reviews)
