from flask import render_template
from app.main.urls import home

# Homepage View
@home.route('/')
def index():

    return render_template('home/index.html')

