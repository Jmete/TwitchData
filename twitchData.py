import requests


# Following functions gets clip data from Twitch API

def get_json():
    ''' Gets the json object of top ~100 clips '''

    url = 'https://api.twitch.tv/kraken/clips/top?limit=100&trending=true'
    # Add your Client-ID
    headers = {"Client-ID": "", "Accept": "application/vnd.twitchtv.v5+json"}
    r = requests.get(url, headers=headers).json()
    return r


def get_video_link(c):
    ''' Gets the actual mp4 link to hide embedded player UI '''

    # The mp4 link can be created by taking elements from the thumbnails.
    # Splits the thumbnail
    tn = c['thumbnails']['small'].split('.tv/')

    # Split it again and subtract the final character for formatting reasons.
    tn = tn[1].split('preview')[0][:-1]

    # Create the video link using standard template and dynamic info that we just got.
    videoLink = "https://clips-media-assets.twitch.tv/" + tn + ".mp4"
    return videoLink


def get_streamer_info(json_object):
    ''' Populates list with streamer info '''

    # Initialize a list to hold the info.
    streamerList = []

    # Loop through json objects and get the information we need. The video link we will get from get_video_link.
    for e in json_object['clips']:
        streamerList.append({"name": e['broadcaster']['display_name'], "linkz": get_video_link(e)})

    return streamerList

''' Tests '''


#print(get_streamer_info(get_json()))

'''
sList = get_streamer_info(get_json())
for e in sList:
    print(e[-1])
'''
