# track.py -- defines track class

class track:
    def __init__(self, x=None, y=None):
        self.title = x
        self.artist = y
    def songStr(self):
        return self.title + " -- " + self.artist
