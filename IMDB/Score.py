#Score.py

import pandas as pd

def sort_by_score(input_file, output_file):
    data = pd.read_csv(input_file)
    data['score'] = pd.to_numeric(data['score'], errors='coerce')
    data = data.sort_values(by='score', ascending=False)
    data.to_csv(output_file, index=False)
if __name__ == '__main__':
    input_file = 'imdb_reviews.csv'
    output_file = 'sorted_score.csv'
    sort_by_score(input_file, output_file)

    