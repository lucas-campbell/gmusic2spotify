import os
import spotipy
import spotipy.util as util

def login_to_spotify(username):
    """ 
    param: username is probably the email used to log in to spotify
    returns: the spotify object created after retrieving oauth token
    """
    
    scope = 'playlist-read-private ' \
             'playlist-modify-private playlist-modify-public'
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    #get authorization token

    # should redirect to a login page for spotify
    token = util.prompt_for_user_token(
            username=username, scope=scope, client_id=SPOTIFY_CLIENT_ID, \
            client_secret=SPOTIFY_CLIENT_SECRET, \
                    redirect_uri=SPOTIFY_REDIRECT_URI)

    if token: #received oath token
            print('received oath token')
            spotify = spotipy.Spotify(auth=token)
            print('spotipy instantiated')
            return spotify

    else: #couldn't get oauth token
            print('Unable to retrieve authorization token ' \
                                            'for {}'.format(username))
def convert_playlist(title):
    """
    param [title] the title of a playlist
    returns a dictionary of the tracks of that playlist
    """
