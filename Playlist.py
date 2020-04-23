# Playlist.py -- defines Playlist class, a list of Tracks

from Track import Track

class Playlist:
    def __init__(self, tracks=[], plTitle = ""):
        self.title = plTitle
        self.length = len(tracks)
        self.entries = []
        if tracks:
            self.add_tracks(tracks)
    
    def add_track(self, t):
        assert isinstance(t, Track), "Playlist entry must be a Track object"
        self.entries.append(t)

    def add_tracks(self, tracks):
        for t in tracks:
            self.add_track(t)