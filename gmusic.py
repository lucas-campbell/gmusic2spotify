# GMusic_modules.py -- interactions with gmusicapi

import sys
import os
from gmusicapi import Mobileclient
import oauth2client # exception handling purposes
import Track

def onetime_perform_oauth(path, open_browser=False):
    """
    params: path to store oauth credentials, after a call to this you should
    only need to call gm_api.oauth_login()
    returns authenticated api
    """
    gm_api = Mobileclient()
    try:
        gm_api.perform_oauth(path, open_browser)
    except oauth2client.client.FlowExchangeError:
        print('\nError obtaining OAuth credentials, aborting\n',
                file=sys.stderr)
    else:
        print('\n\nOK, OAuth credentials stored at: ', path, '\n\n')
        return gm_api # not authenticated yet!

def login_to_gmusic_with_oauth():
    gm_api = Mobileclient()
    creds = os.getenv('OAUTH_CREDS_PATH')
    device_id = os.getenv('ANDROID_ID')
    if gm_api.oauth_login(device_id, oauth_credentials=creds, locale=u'en_US'):
        return gm_api
    else:
        sys.stderr.write('error logging in, exiting program')
        sys.exit()

def login_to_gmusic(username, password):
    """
    DEPRECATED, use login_to_gmusic_with_oauth() instead
    params: username & password for your gmusic account
    returns the authenticated gmusic api object
    """
    gm_api = Mobileclient()
    gm_api.login(email=username, password=password, \
              android_id=gm_api.FROM_MAC_ADDRESS, locale=u'es_ES')
    if gm_api.is_authenticated():
            print('Logged in to Google Music')
            return gm_api
    else:
            sys.stderr.write('error logging in, exiting program')
            sys.exit()

def convert_playlist(title, gm_api):
    """
    Params:
        title: the title of a playlist
        gm_api: an authenticated gmusic api object
    Returns:
        A dictionary of the tracks of that playlist
    """
    if not (gm_api.is_authenticated):
        sys.stderr.write('Error: api not authenticated')
        return None
    allPLs = gm_api.get_all_user_playlist_contents()

    wanted = next((p for p in allPLs if p['name'] == title), None)
    if wanted == None:
        sys.stderr.write('Error: could not find desired playlist')
        return None
    return tracksDict(wanted) # convert found pl into tracksDict format

def tracksDict(pl, gm_api):
    """
    Takes in a google music playlist dictionary and an authenticated
    MobileClient api. The playlist dictionary contains the field
    'tracks'; itself a list of "properly ordered playlist entry dicts".

    Params:
        pl: google music playlist dict
        gm_api: authenticated Mobileclient object

    Returns: 
        playlist: A list of Track objects, in the order they appear in the
                  given playlist. Returned list may be incomplete if not all
                  tracks are hosted on GMusic.
        notFound: A list of trackIDs foor which metadata could not be found.
    """
    playlist = []
    notFound = []
    # song metadata used as cross-check reference if a playlist entry doesn't
    # have desired metadata
    all_song_meta_data = gm_api.get_all_songs()
    for track in pl['tracks']:
        # Check source:
        # '2' indicates hosted on Google Music, '1' otherwise
        if t['source'] == '2':
            song = Track.Track(title=t['track']['title'],
                               artist=t['track']['artist']) 
            playlist.append(song)
        elif track['source'] == '1':
            # Important: when source is '1', playlistEntry object's 'trackId' 
            # will correspond w/ a track object's 'id' in all_song_meta_data
            badtrackID = track['trackId']
            song = next((t for t in all_song_meta_data \
                            if t['id'] == badtrackID), None)
            if song != None:
                # create track object, add to new "playlist"
                track_obj = Track.Track(title=song['title'],
                                        artist=song['artist']) 
                playlist.append(track_obj)
            else:
                msg = "Error with track " + str(badtrackID) + ": 'source'"
                      " field is '1', but could not find matching metadata."
                print(msg, file=sys.stderr)
                notFound.append(badtrackID)
        else:
            msg = "Error with track " + str(track['trackId']) + ": 'source'"
                  " field not '1' or '2'."
            print(msg, file=sys.stderr)
            notFound.append(track['trackId'])

    return playlist, notFound

def add_tracks_to_lib(title, gm_api):
    """
    Takes in a playlist title and an authenticated gmusic api object. With
    this, extracts a google music playlist dictionary, which contains the field
    'tracks'; itself a list of "properly ordered playlist entry dicts".
    Adds those tracks with a valid storeID to your Google Music Library.
    """
    # Extract single playlist
    if not (gm_api.is_authenticated):
        sys.stderr.write('Error: api not authenticated')
        return None
    allPLs = gm_api.get_all_user_playlist_contents()

    pl= next((p for p in allPLs if p['name'] == title), None)
    if pl == None:
        sys.stderr.write('Error: could not find desired playlist')
        return None
    # add playlist's tracks to library
    # to_add = []
    num_added = 0
    num_bad_data = 0
    for t in pl['tracks']:
        metadata = t.get('track', None)
        if metadata != None:
            #to_add.append(metadata['storeId'])
            gm_api.add_store_tracks([metadata['storeId']])
            num_added += 1
        else:
            num_bad_data += 1
    # Gmusicapi call
    #gm_api.add_store_tracks(to_add)
    #print("Added ", len(to_add), " tracks to library.\n")
    print("Added ", num_added, " tracks to library.\n")
    print("Unable to add ", num_bad_data, " tracks.\n")

def print_tracks(td, _sep=' '):
    """
    Prints the elements of 'td', a list of track objects, in string format, to
    screen with the separating character '_sep'.
    """
    track_strings = []
    for t in td:
        track_strings.append(t.songStr())
    print(*track_strings, sep=_sep)
