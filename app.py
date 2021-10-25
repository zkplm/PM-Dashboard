from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

# app.config["UPLOAD_FOLDER"] = '/Users/mahip/Desktop/coding/PM-Dashboard/data'
app.config["UPLOAD_FOLDER"] = '/Users/zmplu/Documents/PM-Dashboard/data'


@app.route('/')
def home():
    return render_template('main.html', template_folder='template')


@app.route("/main", methods=["POST"])
def move_page():
    return render_template("upload_file.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            f = request.files["image"]

            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            print(f)

            return redirect(request.url)

    return render_template("upload_file.html")


if __name__ == '__main__':
    app.run()
