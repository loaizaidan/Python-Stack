from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Champion')
def champion():
    return 'Champion!'

def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:count>/<string:word>')
def repeat_word(count, word):
    return (word + ' ') * count

@app.errorhandler(404)
def not_found(error):
    return "Sorry! No response. Try again.", 404


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.