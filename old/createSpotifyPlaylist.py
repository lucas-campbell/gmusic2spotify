#!/usr/bin/env/python3

import sys
import spotipy
import spotipy.util as util
    
def main():
    #get username from command line args
    if len(sys.argv) > 2:
        username = sys.argv[1]
    else:
        print('Usage {} [your_username] [file_of_track_ids.txt]'.format(sys.argv[0]))
        sys.exit()
    scope = 'playlist-read-private playlist-modify-private playlist-modify-public'
    SPOTIFY_CLIENT_ID = 
    SPOTIFY_CLIENT_SECRET = 
    apiURL = 'https://api.spotify.com'
    SPOTIFY_REDIRECT_URI = 'http://localhost/gmusic_to_spotify/'
    
    #assume server has already been set up, is running on default 5000 port
    #get authorization token

    #oauth = spotipy.oauth2.SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, scope)
    #oauth.OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
    #oauth.OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    #oauth.
    
    token = util.prompt_for_user_token(username=username, scope=scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                        redirect_uri=SPOTIFY_REDIRECT_URI)
    
    if token:
        print('got toekennn obi kenobi!')
        spotify = spotipy.Spotify(auth=token)
        print('spotipy instantiated')
    
    else:
        print('Unable to retrieve authorization token for {}'.format(username))   
    
    
if __name__ == "__main__":
    main()
    
