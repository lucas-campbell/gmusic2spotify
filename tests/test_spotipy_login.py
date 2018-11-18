import os
import spotipy
import spotipy.util as util
from spotify import *

def main():
    spUsername = os.getenv('SPOTIFY_USERNAME')
    spotipy = login_to_spotify(spUsername)
    
if __name__ == "__main__":
    main()
