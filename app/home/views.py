from app.main.urls import home


# Homepage View
@home.route('/')
def index():

    return "Hello World -- Home Page"
