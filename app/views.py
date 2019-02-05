from flask import render_template
from app import app

# Create the mappings from URLs
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')