from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import json
import pandas as pd
import plotly
import plotly.express as px
from parser import file_parser

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = '/Users/mahip/Desktop/coding/PM-Dashboard/Parser'
#app.config["UPLOAD_FOLDER"] = '/Users/zmplu/Documents/PM-Dashboard/Parser'


@app.route('/')
def home():
    data = file_parser()
    print(data)
    df = pd.DataFrame(data)
    fig = px.line(df, x='time', y=[
        'PM10', 'PM1', 'PM2.5'], title='PM Data')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print('HI WORLD')
    return render_template('main.html', graphJSON=graphJSON)

    # return render_template('main.html', template_folder='template')


@app.route("/back_main", methods=["POST"])
def back_home():
    if request.method == "POST":
        data = file_parser()
        print(data)
        df = pd.DataFrame(data)
        fig = px.line(df, x='time', y=[
            'PM10', 'PM1', 'PM2.5'], title='PM Data')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        print('HI WORLD 2')
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
            return redirect(request.url)

    return render_template("upload_file.html")


@app.route("/dash", methods=["POST"])
def notdash():
    if request.method == "POST":
        data = file_parser()
        print(data)
        df = pd.DataFrame(data)
        fig = px.line(df, x='time', y=[
                      'PM10', 'PM1', 'PM2.5'], title='PM Data')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash_board.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run()
