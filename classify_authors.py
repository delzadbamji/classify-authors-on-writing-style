import os
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from tqdm import tqdm
import csv
import pandas as pd


# nltk.download('stopwords')


def get_stop_words(all_mapper, stops):
    length = len(all_mapper)
    # print(length)
    for i in all_mapper:
        for key in tqdm(list(all_mapper[i])):
            if key not in stops:
                del all_mapper[i][key]
    # print(all_mapper)
    return all_mapper


def preprocess(files, stops):
    all_mapper = {}
    for file in files:
        opening = "data\\" + file
        with open(opening) as f:
            i = file
            all_mapper[i] = {}
            for line in tqdm(f):
                line = line.split(' ')

                for word in line:
                    # word=word.replace('[]','')
                    word = re.sub('[\n.\"$\s\[\]]', '', word)
                    if word != '':
                        if word in all_mapper[i]:
                            all_mapper[i][word] += 1
                        else:
                            all_mapper[i][word] = 1
        f.close()
        # print(all_mapper.keys())
    return get_stop_words(all_mapper, stops)


def visualize_mapper(mapper, files):
    plt.figure(figsize=(10, 6))
    # print(mapper[files[0]]['up'],mapper[files[0]]['and'])
    plt.scatter(mapper[files[0]]['up'], mapper[files[0]]['and'], color="blue")
    plt.scatter(mapper[files[1]]['up'], mapper[files[1]]['and'], label="dan", color="green")
    plt.scatter(mapper[files[2]]['up'], mapper[files[2]]['and'],  color="green")
    plt.scatter(mapper[files[3]]['up'], mapper[files[3]]['and'],  color="green")
    plt.scatter(mapper[files[4]]['up'], mapper[files[4]]['and'], label="henry", color="blue")
    plt.scatter(mapper[files[5]]['up'], mapper[files[5]]['and'], color="blue")
    plt.scatter(mapper[files[6]]['up'], mapper[files[6]]['and'], label="punch", color="red")
    plt.scatter(mapper[files[7]]['up'], mapper[files[7]]['and'], color="red")
    plt.scatter(mapper[files[8]]['up'], mapper[files[8]]['and'], color="red")
    plt.xlabel('up')
    plt.ylabel('and')
    plt.title('up vs and')
    plt.legend()
    plt.show()


def main():
    stops = stopwords.words('english')
    files = os.listdir("data")
    mapper = preprocess(files, stops)
    visualize_mapper(mapper, files)
    df = pd.DataFrame.from_dict(mapper)
    # print(df)
    df.to_csv("Results.csv", index=True, header=True, na_rep=0)


main()
