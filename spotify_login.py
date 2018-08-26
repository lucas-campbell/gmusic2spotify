#!/usr/bin/env/python3
#above statement is used to set the right python interpreter

import sys
import spotipy
import spotipy.util as util

def login_to_spotify(username):
        """ param: username is probably the email used to log in to spotify
            returns: the spotify object created after retrieving oauth token"""
        
        scope = 'playlist-read-private ' \
                 'playlist-modify-private playlist-modify-public'
        SPOTIFY_CLIENT_ID = 
        SPOTIFY_CLIENT_SECRET = 
        apiURL = 'https://api.spotify.com'
        SPOTIFY_REDIRECT_URI = 'http://localhost/gmusic_to_spotify/'

        #get authorization token

        token = util.prompt_for_user_token(
                username=username, scope=scope, client_id=SPOTIFY_CLIENT_ID, \ 
                client_secret=SPOTIFY_CLIENT_SECRET, \
                redirect_uri=SPOTIFY_REDIRECT_URI)

        if token: #got it boii
                print('got toekennn obi kenobi!')
                spotify = spotipy.Spotify(auth=token)
                print('spotipy instantiated')
                return spotify

        else: #couldn't get oauth token
                print('Unable to retrieve authorization token ' \
                                                'for {}'.format(username))
