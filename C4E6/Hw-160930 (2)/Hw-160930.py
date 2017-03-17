from flask import *
from mongoengine import *
import os
from werkzeug.utils import secure_filename


APP_ROOT = os.path.dirname(os.path.abspath(__file__))            #curent path file
UPLOAD_FOLDER = os.path.join(APP_ROOT, "static", "collection")   #leading to a inner file from path

print(UPLOAD_FOLDER)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER           #save file to this path


connect()
app = Flask(__name__)


class Film:
    def __init__(self, name, link, img, video):
        self.name = name
        self.link = link
        self.img = img
        self.video = video

another = Film(
    "Another",
    "http://kissanime.to/Anime/Another",
    "https://myanimelist.cdn-dena.com/images/anime/4/75509l.jpg",
    "https://www.youtube.com/embed/xmkZvxWD67E"
)

charlotte = Film(
    "Charlotte",
    "http://kissanime.to/Anime/Charlotte",
    "https://upload.wikimedia.org/wikipedia/en/3/32/Charlotte_key.jpg",
    "https://www.youtube.com/embed/gB5qUxR6ch4"
)

fantasy = Film(
    "Fantasy",
    "http://kissanime.to/Anime/Fantasy",
    "https://i.ytimg.com/vi/BJ02JNk8c-o/maxresdefault.jpg",
    "https://www.youtube.com/embed/8mJpR5L16xc"
)

hyouka = Film(
    "Hyouka",
    "http://kissanime.to/Anime/Hyouka",
    "https://s-media-cache-ak0.pinimg.com/originals/c1/72/7c/c1727c4694c1074d5271a4b48f6af9e0.jpg",
    "https://www.youtube.com/embed/3iQhH-qjIUE"
)

kuroshitsuji = Film(
    "Kuroshitsuji",
    "http://kissanime.to/Anime/Kuroshitsuji",
    "http://vignette4.wikia.nocookie.net/kuroshitsuji/images/1/14/MK_v1_04.png/revision/latest?cb=20110919215448",
    "https://www.youtube.com/embed/SclcqFo9KDE"
)

_11eyes = Film(
    "11eyes",
    "http://kissanime.to/Anime/11eyes",
    "http://vignette3.wikia.nocookie.net/11eyes/images/3/3f/02.jpg/revision/latest/scale-to-width-down/590?cb=20110415155724",
    "https://www.youtube.com/embed/_Gy_P9nEuFg"
)

film_list = [another, charlotte, fantasy, hyouka, kuroshitsuji, _11eyes]


@app.route('/', methods=['GET', 'POST'])
def film():
    if request.method == 'GET':
        return render_template("Hw-160930.html", film_list=film_list)
    elif request.method == 'POST':
        name = request.form['name']
        img = request.form['img']
        link = request.form['link']
        video = request.form['video']
        film = Film(name, link, img, video)
        film_list.append(film)
        return redirect(url_for("film"))


if __name__ == '__main__':
    app.run()
