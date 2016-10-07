from flask import *

app = Flask(__name__)

class Film:
    def __init__(self, name, link, img):
        self.name = name
        self.link = link
        self.img = img

another = Film(
    "Another",
    "http://kissanime.to/Anime/Another",
    "https://myanimelist.cdn-dena.com/images/anime/4/75509l.jpg"
)

charlotte = Film(
    "Charlotte",
    "http://kissanime.to/Anime/Charlotte",
    "https://upload.wikimedia.org/wikipedia/en/3/32/Charlotte_key.jpg"
)

fantasy = Film(
    "Fantasy",
    "http://kissanime.to/Anime/Fantasy",
    "https://i.ytimg.com/vi/BJ02JNk8c-o/maxresdefault.jpg"
)

hyouka = Film(
    "Hyouka",
    "http://kissanime.to/Anime/Hyouka",
    "https://s-media-cache-ak0.pinimg.com/originals/c1/72/7c/c1727c4694c1074d5271a4b48f6af9e0.jpg"
)

kuroshitsuji = Film(
    "Kuroshitsuji",
    "http://kissanime.to/Anime/Kuroshitsuji",
    "http://vignette4.wikia.nocookie.net/kuroshitsuji/images/1/14/MK_v1_04.png/revision/latest?cb=20110919215448"
)

_11eyes = Film(
    "11eyes",
    "http://kissanime.to/Anime/11eyes",
    "http://vignette3.wikia.nocookie.net/11eyes/images/3/3f/02.jpg/revision/latest/scale-to-width-down/590?cb=20110415155724"
)

film_list = [another, charlotte, fantasy, hyouka, kuroshitsuji, _11eyes]


@app.route('/')
def film():
    return render_template("Hw-160930.html", film_list=film_list)

if __name__ == '__main__':
    app.run()
