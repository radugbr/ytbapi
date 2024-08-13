from youtubesearchpython.__future__ import VideosSearch, Video, ResultMode
from flask import Flask

app = Flask(__name__)

@app.route('/id/<video_id>')
def infoPage(video_id):
    try:
        data = await Video.getFormats(video_id)
        return data
    except:
        return {'error':'something went wrong please try again later'}

@app.route('/search/<query>')
def searchPage(query):
    try:
        videosSearch = VideosSearch(query, limit = 10)
        return videosSearch.result()
    except:
        return {'error':'something went wrong please try again later'}
        
