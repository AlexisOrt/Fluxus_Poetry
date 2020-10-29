#add code for flask app object
from flask import Flask, render_template

app = Flask(__name__)

# dependencies
from bs4 import BeautifulSoup
import requests
import re

@app.route('/')

def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run()
