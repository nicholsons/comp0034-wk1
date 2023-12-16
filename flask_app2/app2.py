# Import the Flask class from the Flask library
from flask import Flask, render_template

# Create an instance of a Flask application
# The first argument is the name of the application’s module or package. __name__ is a convenient shortcut.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


# The route for the 'home' or 'index' page
# Use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    # The function renders a Jinja2 template that generates the home page using HTML and bootstrap CSS
    return render_template('index.html')

