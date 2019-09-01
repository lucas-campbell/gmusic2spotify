# playlist_type.py -- defines class of playlist type.
# Has a title and list of track objects (see tracks.py)

class playlist_type:
    def __init__(self, x='', y={}):
        self.title  = x
        self.tracks = y

    def readFromGMusic(self, gmusicPL):
        self.title = gmusicPL['name']
        for t in gmusicPL['tracks']:
            #some sort of check for if track is hosted on gmusic
            if (t['source'] == 
            self.tracks[t
