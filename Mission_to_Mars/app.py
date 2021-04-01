from flask import Flask, render_template, redirect
from flask_pymongo import flask_pymongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] =  "mongodb://localhost:27017/mars.app"


@app.route("/")
def echo():
    return render_template("index.html, text")


@app.route("/scrape")
def scraper():



if __name__ == "__main__":
    app.run(debug=True)