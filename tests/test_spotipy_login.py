import sys
sys.path.append('../')
import os
import spotipy
import spotipy.util as util
import spotify

def main():
    spUsername = os.getenv('SPOTIFY_USERNAME')
    # sl = spotify.login_to_spotify(spUsername)
    sl = spotify.login2spotify(spUsername)
    
if __name__ == "__main__":
    main()
