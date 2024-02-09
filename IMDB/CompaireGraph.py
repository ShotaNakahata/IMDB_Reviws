import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_chart(file_path, output_file='pie_chart.png'):
    # CSVファイルからデータを読み込む
    data = pd.read_csv(file_path)
    
    data_counts = data['mutuality'].value_counts()
    
    data_counts = data_counts.reindex(index=['A', 'B', 'C', 'D', 'E'])
    
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False)
    plt.axis('equal') 
    plt.title('Rating scores and comment identification by AI')

    static_path = os.path.join('C:\\Users\\Jin\\Downloads\\test\\IMDB\\static', output_file)

    plt.savefig(static_path)

if __name__ == '__main__':
    input_file = 'C:\\Users\\Jin\\Downloads\\test\\identify.csv'
    output_file = 'mutuality_pie_chart.png'
    plot_pie_chart(input_file, output_file)
