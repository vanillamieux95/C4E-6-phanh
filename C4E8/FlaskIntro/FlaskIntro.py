from flask import *
from datetime import *

app = Flask(__name__)

pistols = [
{
    "src"   : "http://assets.academy.com/mgen/85/10106785.jpg",
    "title" : "Beretta U22 Neos .22 LR Semiautomatic Single-Action Pistol",
    "pricetag"  : "$278.00"
    },

{
    "src"   : "http://assets.academy.com/mgen/60/10115060.jpg",
    "title" : "Bersa Thunder .380 ACP Pistol",
    "pricetag"  : "$289.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/94/10106794.jpg",
    "title" : "GLOCK 17 9mm Safe-Action Pistol",
    "pricetag"  : "$499.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/74/10108274.jpg",
    "title" : "Beretta 92FS 9 mm Semiautomatic Pistol",
    "pricetag"  : "$598.00"
    },

]


phanh = [{
    "avatar"    : "http://hotshotsnm.com/gallery2/gallery/d/415804-5/dxdustballangle.jpg",
    "fullname"  : "Phuong Anh, NGUYEN PHAM",
    "quote" : "- 不愉快です！-",
    "dob"   : "23.11.1995",
    "phone" : "0122.385.5472",
    "email" : "ph.anh.nguyenpham.l1221@gmail.com",
    "location"  : "Hanoi, Vietnam",
    "education" : "BA in French and International Business",
    "workexp"   : "volunteering, "
}]


@app.route('/')
def hello_world():
    return redirect(url_for("login"))


number_of_visitor = 0


@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time_on_ser = str(datetime.now())
    return render_template(
        "login.html",
        current_time=current_time_on_ser,
        number_of_visitor=number_of_visitor * 100
    )


@app.route('/guns')
def guns():
    return render_template("guns.html", pistols_list = pistols)


@app.route('/contact')
def gun():
    return render_template("contact.html", person = phanh)


if __name__ == '__main__':
    app.run()
