import sys
import os
import spotipy
import spotipy.util as util
import Playlist
import pprint

def login_to_spotify(username=None):
    """ 
    NOTE: prefer use of login2spotify() instead.

    Params:
        username: probably the email used to log in to spotify
    Returns: 
        The spotify api object created after retrieving oauth token
    """
    if username is None:
        username = os.getenv('SPOTIFY_USERNAME')
    
    scope = 'playlist-read-private ' \
            'playlist-modify-private ' \
            'playlist-modify-public'
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

def login2spotify(u=None):
    """ 
    Alternative way to authenticate, using oauth2 object. Does same thing as
    regular login method, just here for reference.
    Params:
        username: probably the email used to log in to spotify
    Returns: 
        The spotify api object created after retrieving oauth token
    """

    scope = 'user-read-private user-library-read ' \
            'playlist-read-private ' \
            'playlist-modify-private ' \
            'playlist-modify-public'

    #SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    #SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    #SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    # Get authorization token:
    # should redirect to a login page for spotify
    try:
        oauth = spotipy.oauth2.SpotifyOAuth(scope=scope, username=u,
                                            cache_path='./.tokens.cred')
        #oauth = spotipy.oauth2.SpotifyOAuth(scope=scope, username=u, show_dialog=True)
        #oauth = spotipy.oauth2.SpotifyOAuth(SPOTIFY_CLIENT_ID,
        #            SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI,
        #            #scope=scope, username=username)
        #            scope=scope)
        sp = spotipy.Spotify(auth_manager=oauth)

        print('spotipy instantiated')
        return sp

    except spotipy.oauth2.SpotifyOauthError as e:
        print('Unable to retrieve authorization token: ', e)
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

    # name new playlist the same title as given Playlist
    user_dict = sp.me()
    user_id = user_dict['id']
    new_pl_dict = sp.user_playlist_create(user_id, playlist.title, playlist.is_public)
    new_pl_id = new_pl_dict['id']

    to_add = playlist.entries
    song_ids = []
    count = 0
    for t in to_add:
        # create custom search string of artist, track
        search = t.spotify_query()
        results = sp.search(search)
        # then, for each track:
        # look through results['tracks'], and (for now) just use the first
        # result with exact matching artist and track name. Else report error
        # and move on
        if len(results['tracks']['items']) != 0:
            song_id_to_add = results['tracks']['items'][0]['id']
            song_ids.append(song_id_to_add)
            count += 1
        else:
            #TODO error reporting
            pass

    sp.user_playlist_add_tracks(user_id, new_pl_id, song_ids)

    # TODO some kind of confirmation? plus report of errors/not found tracks
    print('Sucessfully added ', count, ' songs to spotify playlist')

def convert_playlist(title):
    """
    TODO later on, if want to send playlist frm Spotify --> elsewhere
    param [title] the title of a playlist
    returns a dictionary of the tracks of that playlist
    """
    pass
