from flask import render_template
from app.main.urls import favorites

@favorites.route('/my-favorites')
def favorites():

    return render_template('favorites/favorites.html')