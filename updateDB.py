from pymongo import MongoClient
import twitchData

if __name__ == "__main__":
    streamerList = twitchData.get_streamer_info(twitchData.get_json())

    con = MongoClient()

    db = con.streams

    streamlinks = db.streamtest

    streamlinks.drop()

    streamlinks.insert(streamerList)

    peeps = streamlinks.find()


