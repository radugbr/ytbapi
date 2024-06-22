from youtubesearchpython import VideosSearch, Video, ResultMode
from flask import Flask

app = Flask(__name__)

@app.route('/app/id/<video_id>')
def infoPage(video_id):
    try:
        data = Video.getInfo(f'https://youtu.be/{video_id}', mode = ResultMode.json)
        return data
    except:
        return {'error':'something went wrong please try again later'}

@app.route('/app/search/<query>')
def searchPage(query):
    try:
        videosSearch = VideosSearch(query, limit = 10)
        return videosSearch.result()
    except:
        return {'error':'something went wrong please try again later'}
        
