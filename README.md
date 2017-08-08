# Twitch Data - StreamGuess

Python scripts to query Twitch API for streamer data. Used to provide data for StreamGuess back-end.

View the app at: www.jamesmete.com/streamguess

# How It Works

The actual streamer data is being collected by Python scripts running as a CronTab job query the Twitch API to gather the streamer data and construct urls that lead to the .mp4 files of the clips in order to hide any information that could give away the answer. The API stores info on AWS using MongoDB.

Note: Make sure to input your Client-ID from the Twitch API.

# Author

James Mete
www.jamesmete.com
