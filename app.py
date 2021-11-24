from flask import Flask, request, redirect, render_template, templating
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


def create_graph_data(data_point):
    dbcon = pymysql.connect("104.197.43.121", "root", "ece445", "PMDATA")
    df = pd.read_sql_query(
        '''select * from PM_Data''', dbcon)
    time = []
    print(data_point)
    flag = 0
    flag2 = 1
    for item in df['cur_time'].tolist():
        time.append(item.strip())
    label = time
    values = []
    if data_point == 'Temperature':
        values = df['temp'].tolist()
    elif data_point == 'Humidity':
        values = df['humidity'].tolist()
        flag2 = 2
    elif data_point == 'Wind Speed':
        values = df['wind_speed'].tolist()
        flag2 = 3
    elif data_point == 'Wind Direction':
        values = df['wind_convert'].tolist()
        flag = 1
        flag2 = 4
    value1 = df['pm_one'].tolist()
    value25 = df['pm_two'].tolist()
    value10 = df['pm_ten'].tolist()
    return label, values, value1, value25, value10, flag, flag2


@app.route('/')
def home():
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
    time = []

    for item in df['cur_time'].tolist():
        time.append(item.strip())
    label = time
    # print(time)
    value1 = df['pm_one'].tolist()
    value25 = df['pm_two'].tolist()
    value10 = df['pm_ten'].tolist()
    valuetemp = df['temp'].tolist()

    # label = [1, 2, 3, 4]

    return render_template('main.html', label=label, value1=value1, value25=value25, value10=value10, valuetemp=valuetemp, flag=0, flag2=1)

    # return render_template('main.html', template_folder='template')


@app.route("/data_submit", methods=['GET', "POST"])
def hello():
    if request.method == "POST":
        data_point = request.form.get("datapoints", None)
        print(data_point)
        label, values, value1, value25, value10, flag, flag2 = create_graph_data(
            data_point)
        return render_template('main.html', label=label, value1=value1, value25=value25, value10=value10, valuetemp=values, flag=flag, flag2=flag2)
    return render_template('main.html')


@app.route("/back_main", methods=["POST"])
def back_home():
    if request.method == "POST":
        dbcon = pymysql.connect("104.197.43.121", "root", "ece445", "PMDATA")
        df = pd.read_sql_query(
            '''select * from PM_Data''', dbcon)
        print(type(df))
        print(df)

        time = df['cur_time'].tolist()
        print(time)
        label = time

        value1 = df['pm_one'].tolist()
        value25 = df['pm_two'].tolist()
        value10 = df['pm_ten'].tolist()
        valuetemp = df['wind_convert'].tolist()

        # label = [1, 2, 3, 4]

        return render_template('main.html', label=label, value1=value1, value25=value25, value10=value10, valuetemp=valuetemp, flag=0, flag2=1)

    return render_template("upload_file.html")


@ app.route("/main", methods=["POST"])
def move_page():

    return render_template("upload_file.html")


@ app.route("/upload-file-", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            f = request.files["image"]

            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            file_parser()
            print("HI MAHIP")
            return redirect(request.url)

    return render_template("upload_file.html")


if __name__ == '__main__':
    app.run()
