# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:24:39 2023

@author: C1
"""
# SentimentGraph.py

import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_rate_pie_chart(file_path, output_file='pie_chart.png'):
    df = pd.read_csv(file_path)
    data = df.iloc[:, 3]  
    data_counts = data.value_counts()   
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Rate')    

    # 'C:\Users\Jin\Downloads\test\IMDB\static' フォルダ内に保存するためのパス
    static_path = os.path.join('C:\\Users\\Jin\\Downloads\\test\\IMDB\\static', output_file)

    # 画像を 'C:\Users\Jin\Downloads\test\IMDB\static' フォルダ内に保存
    plt.savefig(static_path)

if __name__ == '__main__':
    file_path = 'C:\\Users\\Jin\\Downloads\\test\\output.csv'
    output_file = 'sentiment_of_rate.png'
    plot_rate_pie_chart(file_path, output_file)


