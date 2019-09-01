import sys
sys.path.append('../')
import os
import gmusic
from gmusicapi import Mobileclient


def main():
    """A test main for getting playlist info from a \
    google music playlist."""
    gmusicapi = gmusic.login_to_gmusic_with_oauth()

    all_playlists = gmusicapi.get_all_user_playlist_contents()
    for p in all_playlists:
            print(p['name'])

if __name__ == "__main__":
    main()
