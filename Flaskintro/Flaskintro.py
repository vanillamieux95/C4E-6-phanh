from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return "Welcome to C4E6!"

@app.route('/ellie')
def hello_ellie():
    return 'Hello Ellie'

@app.route('/<name>')
def hello(name):
    return 'Hello ' + name

@app.route('/<x>/<y>')
def add_up(x, y):
    x = int(x)
    y = int(y)
    z = str(x +y)
    return z

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return "{0}".format(x + y)


if __name__ == '__main__':
    app.run()
