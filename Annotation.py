import numpy as np
import os
import pandas as pd
import re

from collections import defaultdict


class Result(object):

    def __init__(self, w='', s=0.0):
        self.word = w
        self.score = s

    def __lt__(self, other):
        return self.score > other.score

    def toJSON(self):
        return {"Result": {'score': self.score,
                 'word': self.word}}


class Annotation(object):

    def __init__(self):
        self.tweets = None
        self.stop_words = None
        self.anntate_words = []
        self.patterns = ''

    def initialize_data(self,  tweets_file, stop_words_file):
        print('Initializing data...')
        if not os.path.isfile(tweets_file):
            print('File %s not exists, read tweets.csv' % tweets_file)
            data = pd.read_csv('../data/tweets.csv', encoding='ISO-8859-1')
            # idx = data['Latitude'] <= 42
            # idx &= data['Latitude'] >= 38
            # idx &= data['Longitude'] <= -72
            # idx &= data['Longitude'] >= -76
            # data = data[idx]
            data = data.set_index('Tweet Id', inplace=False, drop=True)
            data.to_csv(tweets_file, encoding='utf8')
        self.tweets = pd.read_csv(tweets_file)
        f = open(stop_words_file, 'r')
        line = f.readline()
        self.stop_words = line.split(', ')
        for index, word in enumerate(self.stop_words):
            self.patterns += word
            if index != len(self.stop_words) - 1:
                self.patterns += '|'
        print('Initialize finished')
        print('Tweets num = %d' % self.tweets.shape[0])
        print('Stop words num = %d' % len(self.stop_words))

    def word_filter(self, words):
        words_filted = set()
        for w in words:
            if re.match(self.patterns, w) is not None:
                continue
            w = re.sub('#|!|,', '', w)
            if len(w) == 0:
                continue
            words_filted.add(w.lower())
        return words_filted

    def anntation(self, latitude, longitude, date):
        print('Start annotation...')
        words = self.kde(latitude, longitude, date)
        self.anntate_words = words
        for index, w in enumerate(words):
            if index > 100:
                break
            print(index, w.score, w.word)
        print('Anntation ended...')
        return self.anntate_words

    def kde(self, latitude, longitude, date):
        print('Using kernel density estimation...')
        select = self.tweets[self.tweets['Date'] == date]
        print('select tweets num = %s' % select.shape[0])
        word_list = defaultdict(list)
        for index, row in select.iterrows():
            words = set(row['Tweet content'].split())
            for w in self.word_filter(words):
                word_list[w].append((row['Latitude'], row['Longitude']))
        result = []
        for key, values in word_list.items():
            r = self.score(key, values, latitude, longitude)
            result.append(r)
        result.sort()
        return result

    def score(self, word, values, latitude, longitude):
        s = 0
        bw = 1e-4
        for value in values:
            s += self.kernel(value[0] - float(latitude),
                             value[1] - float(longitude), h=bw)
        s /= len(values)
        return Result(word, s)

    def kernel(self, x, y, h):
        x = np.array([x, y])
        e = np.exp(-1 / (2 * h) * x.dot(x.T))
        return 1 / (2 * np.pi * h) * e


# if __name__ == '__main__':
#
#     # fsq_file = '../data/processed_madison.csv'
#     tweets_file = '../data/tweets_processed.csv'
#     stop_words_file = '../data/stop-word-list.csv'
#     ann = Annotation()
#     ann.initialize_data(tweets_file, stop_words_file)
#     annotation_doc = ann.anntation()

