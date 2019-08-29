# track.py -- defines track class

class track:
    def __init__(self, title="", artist=""):
        self.title = title
        self.artist = artist
    def songStr(self):
        return self.title + " -- " + self.artist
