from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    # return '<p>Welcome to my website</p>'
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # return '<p>Hello, world</p>'
    return render_template('hello.html', name=name)


@app.route('/say/<string:name>')
def hello_name(name):
    return f"<p>Hello, world! Hello, your name is {escape(name)}</p>"


@app.route('/say/<int:age>')
def hello_age(age):
    return f"<p>Hello, world! Hello, your age is {escape(age)}</p>"


@app.route('/login', methods=['GET', 'POST'])
# coba di CMD : curl -d 'username=saya' localhost:5000/login
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login()

def do_the_login():
    return 'Do the login..'

def show_the_login():
    return 'Display login form..'


if __name__ == '__main__':
    app.run(debug=True)