from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def rand_default(x):
    return render_template('index.html', x=x, y=8, color1='red', color2='blue')

@app.route('/<int:x>/<int:y>')
def user_choice(x, y):
    return render_template('index.html', x=x, y=y, color1='red', color2='black')

if __name__ == "__main__":
    app.run(debug=True)
