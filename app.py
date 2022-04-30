from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

# URLs / Redirection
# avoid route end with '/' to make the url unique
@app.route('/user/<username>')
def hello_user(username):
    return f'Hello {username}'


"""
Converter types
- string: (default) accepts any text without a slash
- int: accepts positive integers
- float: accepts positive floating point values
- path: like string but also accepts slashes
- uuid: accepts UUID strings
"""
# Attention: no space after int:
@app.route('/number/<int:number>')
def num_int(number):
    return f'{number}**2 is {number**2}'


@app.route('/number/<float:number>')
def num_float(number):
    return f'{number}*2 is {number*2}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)