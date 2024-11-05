from flask import Flask, render_template, request, redirect
app = Flask(__name__)
#GET request HTTP
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html', phrase = "hello", times = 5)

@app.route('/login', methods=['GET'])
def axsos_platform_login():
    future_dev_list=[
        { "firstname": "Ali", "lastname": "Yahya" },
        { "firstname": "Loai", "lastname": "Zaidan" },
        { "firstname": "Ameed", "lastname": "Sawafta" },
        { "firstname": "Anas", "lastname": "Zughayyer" }
    ]
    return render_template('login.html', mylist = future_dev_list)
####################################################################

#POST request HTTP
@app.route('/userlogin', methods= ['POST'])
def user_login():
    username = request.form['username']
    password = request.form['password']

    if (username == "MohammadAbuMukh" and password == "123456789"):
        return redirect('/profile')
    else:
        return render_template('login.html')


@app.route('/profile')
def news_feed():
    return render_template('main.html')
if __name__ == "__main__":
    app.run(debug=True)