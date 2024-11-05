from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def three_boxes():
    return render_template('index.html', x = 3,backg_color='#59a9ff')

@app.route('/play/<int:x>')
def three_boxe_x(x):
    return render_template('index.html', x=x,backg_color='#59a9ff')

@app.route('/play/<int:x>/<color>')
def three_boxe_x_color(x,color):
    return render_template('index.html', x=x,backg_color=color)



if __name__=="__main__":
    app.run(debug=True)