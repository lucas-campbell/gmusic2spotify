# Track.py -- defines track class

class Track:
    def __init__(self, title=None, artist=None, album=""):
        assert title is not None
        assert artist is not None
        self.title = title
        self.artist = artist
        self.album = album

    def songStr(self):
        #return self.title + " -- " + self.artist
        return str(self.__dict__)

    def spotify_query(self):
        query = 'track:"{}" artist:"{}"'.format(self.title, self.artist)
        if self.album != "":
            query += ' album:"{}"'.format(self.album)
        return query
    
    def spotify_query2(self):
        query = self.title
        return query