from flask import Flask, render_template, request
from imdb import IMDb
import random

app = Flask(__name__)

ia = IMDb()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/requestMovie", methods=["GET"])
def requestMovie():
    movies = ia.get_top250_movies()
    return movies.choice()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)