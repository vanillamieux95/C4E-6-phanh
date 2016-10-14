from flask import *
import os
from werkzeug.utils import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))               #curent path file
UPLOAD_FOLDER = os.path.join(APP_ROOT, "static", "uploads")         #leading to a inner file from path

print(UPLOAD_FOLDER)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER                         #save file to this path after uploading


@app.route('/')
def hello_world():
    return render_template("upload.html")


@app.route('/image/<name>')
def get_image(name):
    return render_template("image.html", image_name=name)


@app.route('/upload', methods=["post"])
def upload_image():
    uploaded_file = request.files["image"]
    if uploaded_file is not None: #is not None is not compulsory included
        filename = secure_filename(uploaded_file.filename)
        print(uploaded_file.filename)

        save_file_name = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        print(save_file_name)

        uploaded_file.save(save_file_name)
        return redirect(url_for("get_image", name = filename)) #name from <name> above, for saving it even after shutdown
    return "Empty"


if __name__ == '__main__':
    app.run()
