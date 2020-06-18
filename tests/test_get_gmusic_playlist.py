import sys
sys.path.append('../')
import os
import gmusic
from gmusicapi import Mobileclient


def main():
    """A test main for getting playlist info from a \
    google music playlist."""
    try:
        gmusicapi = gmusic.login_to_gmusic_with_oauth()
    except:
        print("Error logging in to Google Music -- exiting", file=sys.stderr)
        exit(-1)

    all_playlists = gmusicapi.get_all_user_playlist_contents()

    while True:
        try:
            pl_name = input("Playlist name: ")
            desired_playlist = next((p for p in all_playlists \
                                  if p['name'] == pl_name), None)
            if desired_playlist:
                print("Found")
            else:
                print ("Bad PL name, not found")

        except EOFError:
            print("Ok all done")
            break

if __name__ == "__main__":
    main()
