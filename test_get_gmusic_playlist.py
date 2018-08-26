# import requests
#from gmusicapi.utils import utils
import os
from gmusic_login import login_to_gmusic

def main():
        """A test main for getting playlist info from a \
        google music playlist."""
        #should make these env vars later
        gusername = os.getenv('GMUSIC_USERNAME')
        gpw = os.getenv('GMUSIC_PW')
 #       print(utils.log_filepath)
        gmusicapi = login_to_gmusic(gusername, gpw)

        all_playlists = gmusicapi.get_all_user_playlist_contents()
        for p in all_playlists:
                print(p.name)

if __name__ == "__main__":
        main()
