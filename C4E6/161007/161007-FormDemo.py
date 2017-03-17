#mongodb://<dbuser>:<dbpassword>
# @ds053196.mlab.com:53196/c4edemo

from flask import *
from mongoengine import *

class User(Document):
    user_name = StringField()
    password = StringField() #IntField() kieu so

db_name = "c4edemo"
host = "ds053196.mlab.com"
port = 53196
user_name = "admin"
password = "admin"

connect(
    db_name,
    host=host,
    port=port,
    username=user_name,
    password=password)

user = User(user_name="Phanh", password= "hani")
user.save()

app = Flask(__name__)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


new_user = []


@app.route('/profile')
def profile():
    return "PROFILE, :>"


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def do_register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        #1 create variable
        username = request.form["username"]
        password = request.form["password"]

        #2 Import data
        user = User(username,password)

        #3 Adding value
        new_user.append(user)
        print(new_user)
#        print(request.form)
#        print(request.form["username"])
#        print(request.form["password"])
        return redirect(url_for("profile"))



if __name__ == '__main__':
    app.run()
