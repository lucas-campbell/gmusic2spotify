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

def new_playlist(sp, playlist, interactive=False):
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

    to_add = playlist.entries
    song_ids = []
    # list of indices in song_ids list that will hold search queries for songs
    # that failed
    missing = [] 
    missing_indices = []
    count = 0
    i = 0
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
            missing_indices.append(i)
            missing.append(t)
            # placeholder value, to be filled in or deleted later
            if interactive:
                song_ids.append(None)
        i += 1

    fixed = 0
    if len(missing) > 0:
        if interactive:
            # replace each 'None' in song_ids list with a user-selected id, or
            # delete it
            fixed = resolve_pl_errors(sp, song_ids, missing, missing_indices,
                                playlist.title)
        else:
            # just write errors to file, no interaction
            with open(playlist.title+'_missing.txt', 'w') as f:
                for j in range(len(missing)):
                    f.write(missing[j].spotify_query() + '\n');

    # Create the playlist
    new_pl_dict = sp.user_playlist_create(user_id, playlist.title, playlist.is_public)
    new_pl_id = new_pl_dict['id']
    num_tracks = count + fixed
    # number of full, 100-track batches to add
    batches = num_tracks // 100
    len_final_batch = num_tracks % 100
    if num_tracks % 100 == 0:
        len_final_batch = 100
    if batches > 1:
        for i in range(batches):
            sp.user_playlist_add_tracks(user_id,
                                        new_pl_id,
                                        song_ids[(i*100):((i+1)*100)])

    # last batch, leftovers after modding by 100
    sp.user_playlist_add_tracks(user_id, new_pl_id,
                    song_ids[((batches)*100):])
    print("Successfully transfered {} songs to new playlist '{}'.".format(
            str(count + fixed), playlist.title))
    if len(missing)-fixed > 0:
        print('Errors were written to {}_missing.txt.'.format(playlist.title))


def resolve_pl_errors(sp, song_ids, missing, missing_indices, title):
    """
    sp: alread-authenticated spotify api

    song_ids: list of Spotify song IDs to be added to a playlist, with a
              placeholder value of None where restrictive search did not work

    missing: list of Track objects whose searches failed

    missing_indices: list of indices that correspond to the slots in the
                     song_ids list that hold None
    """
    failed = []
    found = 0
    # Go backwards so that deleting from song_ids doesn't mess up indexing
    for i in range(len(missing)-1, -1, -1): 
        # search again, but without the quotes
        results = sp.search(missing[i].spotify_query2())
        # couldn't find anything
        if len(results['tracks']['items']) == 0:
            print('Nothing found for {}. Try again with fewer restrictions? (y/n)'.format(missing[i].spotify_query2()))
            ans = input()
            while ans != 'y' and ans != 'n':
                ans = input('Please enter y or n: ')
            if ans == 'n':
                failed.append(missing[i])
                assert(song_ids[missing_indices[i]] is None)
                del song_ids[missing_indices[i]]
                continue
            else: # ans == 'y'
                results = sp.search(missing[i].spotify_query3())
                if len(results['tracks']['items']) == 0:
                    print('Still nothing. Recording failure...')
                    failed.append(missing[i])
                    assert(song_ids[missing_indices[i]] is None)
                    del song_ids[missing_indices[i]]
                    continue

        # present options to user
        options = []
        num_results = len(results['tracks']['items'])
        print("Please choose from the following options (0-{}, "\
              "or n for none of them):".format(9 if num_results > 10 else
                                                num_results-1))
        # create list of possible selections (e.g. 0-9, n)
        items = results['tracks']['items'] # shorthand
        poss_len = 10 if num_results > 10 else num_results
        possible_selections = []
        for j in range(poss_len):
            possible_selections.append(str(j))
        possible_selections.append('n')

        # print search results
        for j in range(poss_len):
            res = items[j]
            m = res['duration_ms'] // 60000 # minutes
            s = round((res['duration_ms'] % 60000) / 1000) # seconds
            print('{}\t{}\t{}\t{}:{}'.format(res['name'],
                                             res['artists'][0]['name'],
                                             res['album']['name'],
                                             m, s))
        # get selection
        sel = input('Selection: ')
        while (sel not in possible_selections):
            print('Invalid option, please choose a number from 0 to {} or'\
                    ' n to skip this song and write the error to a '\
                    'file.'.format(poss_len-1))
            sel = input('Selection: ')
        # record failed search,
        if sel == 'n':
            failed.append(missing[i])
            assert(song_ids[missing_indices[i]] is None)
            del song_ids[missing_indices[i]]
        # or, add user's selected song's id to song_ids list
        else:
            sel = int(sel)
            song_ids[missing_indices[i]] = items[sel]['id']
            found += 1
    
    print('Added back {} of {} missing'.format(found, len(missing)))
    # write failures to file
    if len(failed) > 0:
        with open(title+'_missing.txt', 'w') as f:
            # reverse again, so write erros in correct order
            for i in range(len(failed)-1, -1, -1):
                f.write(failed[i].spotify_query2() + '\n');
    return found

def convert_playlist(title):
    """
    TODO later on, if want to send playlist from Spotify --> elsewhere
    param [title] the title of a playlist
    returns a dictionary of the tracks of that playlist
    """
    pass
