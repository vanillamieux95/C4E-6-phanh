from flask import *

# from flask import redirect
app = Flask(__name__)


class Person:  # class
    def __init__(self, name, cake):  # constructor
        self.name = name
        self.cake = cake


mocha = Person(
    "Mocha",
    "http://uwyoextension.org/uwnutrition/wp-content/uploads/2013/02/red-velvet-cake.bmp"
)  # object
# mocha.name = "Mocha"
# mocha.cake = "http://uwyoextension.org/uwnutrition/wp-content/uploads/2013/02/red-velvet-cake.bmp"


billgates = Person(
    "Bill Gates",
    "https://pbs.twimg.com/profile_images/558109954561679360/j1f9DiJi.jpeg"
)


# billgates = Person()
# billgates.name = "Bill Gates"
# billgates.cake = "https://pbs.twimg.com/profile_images/558109954561679360/j1f9DiJi.jpeg"

@app.route('/')
@app.route('/index')
def index():
    return '<h>Welcome to C4E!</h>'


@app.route('/new')
def new():
    return redirect(url_for('techkids'))


@app.route('/school')
def techkids():
    return redirect('http://techkids.vn')


@app.route('/<name>')
def hello(name):
    return 'Hello {0}'.format(name)


@app.route('/redvelvetcake')
def redvelvet():
    return render_template("redvelvetcake.html", person=mocha)


@app.route('/billgates')
def bill_gates():
    return render_template("redvelvetcake.html", person=billgates)


@app.route('/school')
def techkid():
    return redirect('http://techkids.vn')


# Cach 1
person_list = [billgates, mocha]


@app.route('/rm/<int:index>')
def view_role_model(index):
    return render_template("redvelvetcake.html", person=person_list[index])


# Cach 2:
person_dict = {
    "mocha": mocha,
    "billgates": billgates
}


@app.route('/rm/<name>')
def view_role_model2(name):
    return render_template("redvelvetcake.html", person=person_dict[name])


# Open many profile at once:
@app.route('/rm')
def view_role_models():
    return render_template("redvelvetcakes.html", person_list=person_list)


if __name__ == '__main__':
    app.run()
