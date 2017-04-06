#!/usr/bin/env
# coding:utf-8
"""
Created on 17/4/1 下午2:34

base Info
"""
__author__ = 'xiaochenwang94'
__version__ = '1.0'

import json
from flask import Flask, render_template, request
from Annotation import Annotation
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        latitude = request.form.get("latitude", "null")
        longitude = request.form.get("longitude", "null")
        date = request.form.get("date","null")
        date = date.split(' ')
        da = date[2]
        tweets_file = './data/tweets_processed.csv'
        stop_words_file = './data/stop-word-list.csv'
        ann = Annotation()
        ann.initialize_data(tweets_file, stop_words_file)
        print('2016-04-'+da)
        result = ann.anntation(latitude, longitude, '2016-04-'+da)
        result = result[0:21]
        jsonstr = json.dumps([r.toJSON() for r in result])
        return jsonstr
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
