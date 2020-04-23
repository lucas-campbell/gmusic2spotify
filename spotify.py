import os
import spotipy
import spotipy.util as util
import Playlist
import pprint

def login_to_spotify(username=None):
    """ 
    Params:
        username: probably the email used to log in to spotify
    Returns: 
        The spotify api object created after retrieving oauth token
    """
    if username is None:
        username = os.getenv('SPOTIFY_USERNAME')
    
    scope = 'playlist-read-private ' \
             'playlist-modify-private playlist-modify-public'
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    # Get authorization token:
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
            return None

def login2(username=None):
    """ 
    Alternative way to authenticate, using oauth2 object. Does same thing as
    regular login method, just here for reference.
    Params:
        username: probably the email used to log in to spotify
    Returns: 
        The spotify api object created after retrieving oauth token
    """
    if username is None:
        username = os.getenv('SPOTIFY_USERNAME')
    
    scope = 'playlist-read-private ' \
             'playlist-modify-private playlist-modify-public'
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    # Get authorization token:
    # should redirect to a login page for spotify
    try:
        oauth = spotipy.oauth2.SpotifyOAuth(SPOTIFY_CLIENT_ID,
                    SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI,
                    scope=scope, username=username)
        sp = spotipy.Spotify(auth_manager=oauth)
        print('spotipy instantiated')
        return sp

    except spotipy.oauth2.SpotifyOauthError:
        print('Unable to retrieve authorization token ' \
                                        'for {}'.format(username))
        return None

def new_playlist(sp, playlist):
    """
    Given a Playlist object and authenticated spotipy api, finds the
    corresponding tracks on spotify and creates a new playlist for that user
    Params:
        sp: authenticated spotipy.Spotify api object (as returned by
            login_to_spotify)
        playlist: a Playlist object
    Returns:
        None
    """
    ### Skeleton pseudocode ###

    # name playlist the same thing as given (need to create Playlist class
    # tbh, so can have title, # of tracks, private/public, etc)
    to_add = playlist.entries
    for t in to_add:
        search = t.spotify_query2()
        print("search: %s" % (search))
        results = sp.search(search)
        pprint.pprint(results)
        #print("First result: %s by %s on %s"%(results[]))
        break

    # then, for each track:
        # create custom search string of artist, track
        # results = search()
        # look through results['tracks'], and (for now) just use the first
        # result with exact matching artist and track name. Else report error
        # and move on

    # some kind of confirmation? plus report of errors/not found tracks

    ### End skeleton pseudocode ###

def convert_playlist(title):
    """
    TODO later on, if want to send playlist frm Spotify --> elsewhere
    param [title] the title of a playlist
    returns a dictionary of the tracks of that playlist
    """
    pass
