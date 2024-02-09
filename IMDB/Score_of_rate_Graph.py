# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:50:42 2023

@author: C1
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_score_pie_chart(file_path, output_file='score_pie_chart.png'):
    df = pd.read_csv(file_path)
    if 'score' in df.columns:
        data_counts = df['score'].value_counts()
        plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Score')

        # 'C:\Users\Jin\Downloads\test\IMDB\static' フォルダ内に保存するためのパス
        static_path = os.path.join('C:\\Users\\Jin\\Downloads\\test\\IMDB\\static', output_file)

        # 画像を 'C:\Users\Jin\Downloads\test\IMDB\static' フォルダ内に保存
        plt.savefig(static_path)
    else:
        print("DataFrame does not contain 'score' column.")

if __name__ == '__main__':
    file_path = 'C:\\Users\\Jin\\Downloads\\test\\output.csv'
    output_file = 'score_of_rate.png'
    plot_score_pie_chart(file_path, output_file)






