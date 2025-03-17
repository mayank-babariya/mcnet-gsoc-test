from flask import render_template
from base import app

@app.route('/', methods=['GET'])
def login():
    return render_template('mcnet.html')

@app.route('/aboutme', methods=['GET', 'POST'])
def about():
    return render_template('home.html')