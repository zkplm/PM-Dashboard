from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import json
import pandas as pd
import pymysql
import plotly
import plotly.express as px
from datetime import datetime
from parser import file_parser

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = '/Users/mahip/Desktop/coding/PM-Dashboard/Parser'
# app.config["UPLOAD_FOLDER"] = '/Users/zmplu/Documents/PM-Dashboard/Parser'


@app.route('/')
def home():
    # data = file_parser()
    # print(data)
    # df = pd.DataFrame(data)
    # fig = px.line(df, x='time', y=[
    #     'PM10', 'PM1', 'PM2.5'], title='PM Data')
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # print('HI WORLD')
    dbcon = pymysql.connect("104.197.43.121", "root", "ece445", "PMDATA")
    df = pd.read_sql_query(
        '''select * from PM_Data''', dbcon)
    print(type(df))
    print(df)
    for i in range(0, len(df['cur_time'])):
        print(df['cur_time'][i])
        df['cur_time'][i] = datetime.strptime(
            df['cur_time'][i], '%H%M%S').time()
    fig = px.line(df, x='cur_time', y=[
        'pm_ten', 'pm_one', 'pm_two'], title='PM Data')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('main.html', graphJSON=graphJSON)

    # return render_template('main.html', template_folder='template')


@app.route("/back_main", methods=["POST"])
def back_home():
    if request.method == "POST":
        dbcon = pymysql.connect("104.197.43.121", "root", "ece445", "PMDATA")
        df = pd.read_sql_query(
            '''select * from PM_Data''', dbcon)
        print(type(df))
        print(df)
        for i in range(0, len(df['cur_time'])):
            print(df['cur_time'][i])
            df['cur_time'][i] = datetime.strptime(
                df['cur_time'][i], '%H%M%S').time()
        fig = px.line(df, x='cur_time', y=[
            'pm_ten', 'pm_one', 'pm_two'], title='PM Data')

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('main.html', graphJSON=graphJSON)
    return render_template("upload_file.html")


@app.route("/main", methods=["POST"])
def move_page():

    return render_template("upload_file.html")


@app.route("/upload-file-", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            f = request.files["image"]

            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            file_parser()
            return redirect(request.url)

    return render_template("upload_file.html")


@app.route("/dash", methods=["POST"])
def notdash():
    if request.method == "POST":
        # data = file_parser()
        # print(data)
        # df = pd.DataFrame(data)
        dbcon = pymysql.connect("104.197.43.121", "root", "ece445", "PMDATA")
        df = pd.read_sql_query(
            '''select * from PM_Data''', dbcon)
        print(type(df))
        print(df)
        for i in range(0, len(df['cur_time'])):
            print(df['cur_time'][i])
            df['cur_time'][i] = datetime.strptime(
                df['cur_time'][i], '%H%M%S').time()
        fig = px.line(df, x='cur_time', y=[
            'pm_ten', 'pm_one', 'pm_two'], title='PM Data')

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash_board.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run()
