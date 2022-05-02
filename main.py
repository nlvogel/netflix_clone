from flask import render_template, url_for, redirect, jsonify
from flask_bootstrap import Bootstrap
from app import app, db
from api import *
with app.app_context():
    from model import *

Bootstrap(app)  # adds initial styling to make life easier

# Home page, this will show all the titles sorted by category, "new picks" will be at the top
@app.route('/')
def home():
    return render_template('index.html')

# runs code
if '__main__' == __name__:
    app.run(host='0.0.0.0', debug=True)