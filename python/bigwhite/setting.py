import pymongo

mongo = pymongo.MongoClient("127.0.0.1", port=27017)
MONGO_DB = mongo["bigwhite"]

IMAGES_PATH = 'Images'
MUSICS_PATH = "Musics"

