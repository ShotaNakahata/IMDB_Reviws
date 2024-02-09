import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from WriteIMDB import get_reviews, write_to_csv
from IdentifyAI import perform_sentiment_analysis
from compare import perform_sentiment_analysis_with_other
from Score import sort_by_score
from SentimentGraph import plot_rate_pie_chart
from Score_of_rate_Graph import plot_score_pie_chart
from CompaireGraph import plot_pie_chart
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__)

def save_pie_chart(data, output_file, title):
    static_path = os.path.join('static', output_file)

    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, counterclock=False)
    plt.axis('equal')
    plt.title(title)  # Set the title based on the provided parameter

    plt.savefig(static_path)
    plt.close()

def run_scraping():
    try:
        # WriteIMDB.pyの実行
        url = 'https://www.imdb.com/title/tt21328106/reviews?ref_=tt_urv'
        reviews = get_reviews(url)
        write_to_csv(reviews)

        # IdentifyAI.pyの実行
        perform_sentiment_analysis('imdb_reviews.csv', 'output.csv')

        # compare.pyの実行
        perform_sentiment_analysis_with_other('output.csv', 'identify.csv')

        # Score.pyの実行
        sort_by_score('output.csv', 'sorted_score.csv')

        # SentimentGraph と core_of_rate_Graph の生成
        # SentimentGraph と core_of_rate_Graph の生成
        file_path = 'output.csv'
        output_file = 'SentimentGraph.png'
        data = pd.read_csv(file_path).iloc[:, 3].value_counts().sort_index()
        save_pie_chart(data, output_file, 'SentimentGraph')  # Set title here

        file_path2 = 'output.csv'
        output_file2 = 'score_of_rate.png'
        data2 = pd.read_csv(file_path2)['score'].value_counts().sort_index()
        save_pie_chart(data2, output_file2, 'ScoreGraph')  # Set title here

        # CompaireGraph の実行
        file_path3 = 'identify.csv'
        output_file3 = 'mutuality_pie_chart.png'
        data3 = pd.read_csv(file_path3)['mutuality'].value_counts().sort_index()
        save_pie_chart(data3, output_file3, 'MutualityGraph')  # Set title here

        # リダイレクト
        return redirect(url_for('scraping_result'))
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_scraping', methods=['POST'])
def run_scraping_route():
    return run_scraping()

@app.route('/scraping_result')
def scraping_result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)


