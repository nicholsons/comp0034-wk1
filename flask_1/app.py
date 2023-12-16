# Import the Flask library
from flask import Flask

# Create an instance of a Flask application
app = Flask(__name__)

# Add a route for the 'home'page
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# Run the app
if __name__ == '__main__':
    app.run()
