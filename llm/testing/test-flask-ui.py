from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()