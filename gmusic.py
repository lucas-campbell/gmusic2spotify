# GMusic_modules.py -- interactions with gmusicapi

import sys
import os
from gmusicapi import Mobileclient
from track import track

def onetime_perform_oauth(path, open_browser=False):
    """
    params: path to store oauth credentials, after a call to this you should
    only need to call api.oauth_login()
    returns authenticated api
    """
    api = Mobileclient()
    api.perform_oauth(path, open_browser)
    print('\n\nOK, OAuth credentials stored at: ', path, '\n\n')

    return api

def login_to_gmusic_with_oauth():
    api = Mobileclient()
    creds = os.getenv('OAUTH_CREDS_PATH')
    if api.oauth_login(api.FROM_MAC_ADDRESS, \
            oauth_credentials=creds, locale=u'en_US'):
        return api
    else:
        sys.stderr.write('error logging in, exiting program')
        sys.exit()

def login_to_gmusic(username, password):
    """
    DEPRECATED, use login_to_gmusic_with_oauth() instead
    params: username & password for your gmusic account
    returns the authenticated gmusic api object
    """
    api = Mobileclient()
    api.login(email=username, password=password, \
              android_id=api.FROM_MAC_ADDRESS, locale=u'es_ES')
    if api.is_authenticated():
            print('Logged in to Google Music')
            return api
    else:
            sys.stderr.write('error logging in, exiting program')
            sys.exit()

def convert_playlist(title, gapi):
    """
    param [title] the title of a playlist
    param [gapi] an authenticated gmusic api object
    returns a dictionary of the tracks of that playlist
    """
    if not (gapi.is_authenticated):
        sys.stderr.write('Error: api not authenticated')
        return None
    allPLs = gapi.get_all_user_playlist_contents()

    wanted = next((p for p in allPLs if p['name'] == title), None)
    if wanted == None:
        sys.stderr.write('Error: could not find desired playlist')
        return None
    return tracksDict(wanted) # convert found pl into tracksDict format

def tracksDict(pl):
    """
    takes in a google music playlist dictionary, which contains the field
    'tracks'; itself a list of "properly ordered playlist entry dicts".
    Returns a list of track objects, in the order they appear in the
    given playlist. Returned list may be incomplete if not all tracks are
    hosted in GMusic (and thus metadata cannot be accessed via gmusic api),
    in which case a list of those trackIDs will be returned as well.
    """
    playlist = []
    notHosted = []
    for t in pl['tracks']:
        metadata = t.get('track', None)
        if metadata != None:
            # create track object, add to 'playlist'
            song = track(title=metadata['title'], artist=metadata['artist']) 
            playlist.append(song)
        else:
            playlist.append(track(title="Error: Song metadata not accessible"))
            notHosted.append(t['id'])

    return (playlist, notHosted)

def add_tracks_to_lib(title, gapi):
    """
    takes in a playlist title and an authenticated gmusic api object. With
    This, extracts a google music playlist dictionary, which contains the field
    'tracks'; itself a list of "properly ordered playlist entry dicts".
    Adds those tracks with a valid storeID to your Google Music Library.
    """
    # Extract single playlist
    if not (gapi.is_authenticated):
        sys.stderr.write('Error: api not authenticated')
        return None
    allPLs = gapi.get_all_user_playlist_contents()

    pl= next((p for p in allPLs if p['name'] == title), None)
    if pl == None:
        sys.stderr.write('Error: could not find desired playlist')
        return None
    # add playlist's tracks to library
    # to_add = []
    added = 0
    bad_data = 0
    for t in pl['tracks']:
        metadata = t.get('track', None)
        if metadata != None:
            #to_add.append(metadata['storeId'])
            gapi.add_store_tracks([metadata['storeId']])
            added = added + 1
        else:
            bad_data = bad_data + 1
    # Gmusicapi call
    #gapi.add_store_tracks(to_add)
    #print("Added ", len(to_add), " tracks to library.\n")
    print("Added ", added, " tracks to library.\n")
    print("Unable to add ", bad_data, " tracks.\n")

def print_tracks(td, _sep=' '):
    """
    Prints the elements of 'td', a list of track objects, in string format, to
    screen with the separating character '_sep'.
    """
    track_strings = []
    for t in td:
        track_strings.append(t.songStr())
    print(*track_strings, sep=_sep)
