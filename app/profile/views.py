from flask import render_template
from app.main.urls import profile

# Homepage View
@profile.route('/my-profile')
def profile():

    return render_template('profile/profile.html')