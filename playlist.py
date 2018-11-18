# playlist_type.py -- defines class of playlist type

class playlist_type:
    def __init__(self):
        self.title=''
        self.numTracks=0
        self.tracks={}

    def readFromGMusic(self, gmusicPL):
        self.title = gmusicPL['name']
        for t in gmusicPL['tracks']:
            if (t['source'] == 
            self.tracks[t




