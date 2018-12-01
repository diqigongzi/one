from flask import Blueprint, send_file
import os
from setting import IMAGES_PATH
from setting import MUSICS_PATH

gs = Blueprint("get_something", __name__)


@gs.route("/get_image/<filename>")
def get_image(filename):
    file = os.path.join(IMAGES_PATH, filename)
    return send_file(file)


@gs.route("/get_music/<filename>")
def get_music(filename):
    file = os.path.join(MUSICS_PATH, filename)
    return send_file(file)
