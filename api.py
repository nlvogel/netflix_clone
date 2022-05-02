from flask import jsonify, render_template
from app import app, db
with app.app_context():
    from model import *


@app.route('/api')
def api():
    pass
