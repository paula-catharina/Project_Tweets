#!/usr/bin/python
# -*- coding: utf-8 -*-


from nltk.tokenize import TweetTokenizer
from collections import Counter, OrderedDict
import re
import pandas as pd
import statistics
import matplotlib.pyplot as plt

# Words to ignore
ignore_words = ['rt', '#']


# Procedure to get unique words
# Return Counter collection with words and frequency
def generate_unique_words(text):
    # remove url
    step1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
    # remove punctuation
    step2 = re.sub(r'[^\w#@\s]', '', step1)

    tokenizer = TweetTokenizer(preserve_case=False)

    step3 = tokenizer.tokenize(step2)
    step4 = [x for x in step3 if not x.isdigit()]
    step5 = [x for x in step4 if x not in ignore_words]
    step6 = [x for x in step5 if not x.startswith('#')]
    step7 = [x for x in step6 if not x.startswith('@')]
    words = Counter(step7)
    return words


def write_csv(file_path, data, data_name):
    s = pd.Series(data, name=data_name)
    s.to_csv(file_path)


def main():
    # Read tweets dataset
    with open('tweets.txt', 'r', encoding='UTF-8') as dataset_file:
        dataset_text = dataset_file.read()

    # output 1
    unique_words = generate_unique_words(dataset_text)
    ordered_unique_words = OrderedDict(unique_words.most_common())
    write_csv('output1.csv', ordered_unique_words, 'word_count')
    # horizontal bar
    mostcommon = unique_words.most_common(30)
    plt.barh(range(len(mostcommon)), [val[1] for val in mostcommon], align='center')
    plt.yticks(range(len(mostcommon)), [val[0] for val in mostcommon])
    plt.title('Most Common Words Frequency')
    plt.savefig('words_frequency.png')

    # output 2
    tweets = dataset_text.split('\n')
    lst_num_words = []
    for tweet in tweets:
        unique_words = generate_unique_words(tweet)
        lst_num_words.append(len(unique_words))

    data = {'Median': statistics.median(lst_num_words)}
    write_csv('output2.csv', data, 'median')

    # unique word count plot
    fig, ax = plt.subplots()
    ax.plot(lst_num_words)
    ax.set(xlabel='tweet', ylabel='unique words', title='Count of unique words per tweet')
    ax.grid()
    plt.savefig("unique_words.png")

    # boxplot
    fig2, bp = plt.subplots()
    bp.boxplot(lst_num_words)
    plt.title('Count of unique words per tweet boxplot')
    plt.savefig("unique_words_count_boxplot.png")


if __name__ == "__main__": 
    main()
