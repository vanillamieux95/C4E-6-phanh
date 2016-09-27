from flask import *

app = Flask(__name__)


class Information:
    def __init__(self, name, description, img, link):
        self.name = name,
        self.description = description,
        self.img = img,
        self.link = link


hagiang = Information(
    "Ha Giang",
    "September, a perfect timing to come to Ha Giang and feel the glorious blooming of Buckwheat",
    "http://dulichhagiang.vn/upimgbk/anhhagiang/hoatamgiacmach3.jpg",
    "http://dulich.vnexpress.net/photo/anh-video/ha-giang-ruc-ro-mua-hoa-tam-giac-mach-3299782.html"
)

sapa = Information(
    "Sapa",
    "Late september is when all the Terraced fields here in Lao Cai is covered with the coat of golden Wheat.",
    "http://namuhotel.vn/FileUpload/Images/ruong_bac_thang_mua_lua_chin_3.jpg",
    "http://news.zing.vn/thang-canh-ngoan-muc-tren-cung-sa-pa-y-ty-mua-lua-chin-post574802.html"
)


# places_dict = {
#     "ha-giang" : hagiang,
#     "sapa" : sapa
# }


places_list = [hagiang, sapa]


@app.route('/')
@app.route('/index')
def index():
    return render_template('Hw-Flask160923-page1.html')


@app.route('/fav')
def favorite():
    return render_template('Hw-Flask160923-page2.html', info = places_list)


@app.route('/<int:index>')
def info_place(index):
    if index not in places_list:
        return "Result not found"
    else:
        return render_template('Hw-Flask160923-page2.html', info = places_list[index])


if __name__ == '__main__':
    app.run()
