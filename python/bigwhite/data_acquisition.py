import requests
import os
import time
from uuid import uuid4
from setting import MONGO_DB
from setting import IMAGES_PATH
from setting import MUSICS_PATH

xmly_url = "http://m.ximalaya.com/tracks/%s.json"
music_url_list = ["/ertong/424529/7713577", "/ertong/424529/7713660",
                  "/ertong/424529/7013212", "/ertong/424529/7713154",
                  "h/ertong/424529/7713571", "/ertong/424529/7713553"]
def get_content(music_id):
    res = requests.get(xmly_url % (music_id))
    music_info = res.json()
    music_dict = {
        "title": music_info.get("title"),
        "nickname": music_info.get("nickname"),
        "intro": music_info.get("intro"),
        "cover": "",
        "music": "",
        "create_time": time.time()
    }

    filename=uuid4()
    cover_url=music_info.get("cover_url")
    music_url=music_info.get("play_path")

    cover=requests.get(cover_url)
    music=requests.get(music_url)

    cover_file_path=os.path.join(IMAGES_PATH,f"{filename}.jpg")
    music_file_path=os.path.join(MUSICS_PATH,f"{filename}.mp3")


    with open(cover_file_path,"wb") as f:
        f.write(cover.content)

    with open(music_file_path,"wb") as f:
        f.write(music.content)

    music_dict["cover"]=f"{filename}.jpg"
    music_dict["music"]=f"{filename}.mp3"

    MONGO_DB.childrensong.insert_one(music_dict)

for music_url in music_url_list:
    music_id=music_url.rsplit("/",1)[-1]
    get_content(music_id)