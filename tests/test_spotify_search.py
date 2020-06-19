#!/usr/bin/env python3
import sys
sys.path.append('../')
import spotify
from Track import Track
from Playlist import Playlist
import pprint

def main():
    sp_api = spotify.login2spotify()
    #sp_api = spotify.login_to_spotify()

    #t1 = Track("Far Away Truths", "Albert Hammond Jr")
    #t2 = Track("Reptilia", "The Strokes")
    #t3 = Track("Bodys", "Car Seat Headrest")
    #ts = [t1, t2, t3]
    #pl = Playlist(ts, "toost")

    #spotify.new_playlist(sp_api, pl)
    results = sp_api.search('track: Walk on the Wild Side')
    pprint.pprint(results)


if __name__ == "__main__":
    main()
