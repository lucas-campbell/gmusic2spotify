# GMusic_modules.py -- interactions with gmusicapi

import sys
from gmusicapi import Mobileclient
from track import track

def login_to_gmusic(username, password):
    """
    params: username & password for your gmusic account
    returns the authenticated gmusic api object
    """
    api = Mobileclient()
    api.login(email=username, password=password, \
              android_id=api.FROM_MAC_ADDRESS, locale='en_US')
    if api.is_authenticated():
            print('Logged in to Google Music')
            return api
    else:
            sys.stderr.write('error logging in, exiting program')
            sys.exit()

def login_to_gmusic_webclient(username, password):
    """ params: obvious
    returns the gmusic Webclient api object that has been authenticated """
    
    api = Webclient()
    if api.login(email=username, password=password):
            print('aye')
            return api
    else:
            sys.stderr.write('error logging in, exiting program')
            sys.exit()

def convert_playlist(title, gapi):
    """
    param [title] the title of a playlist
    returns a dictionary of the tracks of that playlist
    """
    if not (gapi.is_authenticated):
        sys.stderr,write('Error: api not authenticated')
        return None
    allPLs = gapi.get_all_user_playlist_contents()

    wanted = next((p for p in allPLs if p['name'] == title), None)
    if wanted == None: 
        sys.stderr,write('Error: could not find desired playlist')
        return None
    return tracksDict(wanted)

def tracksDict(pl):
    """
    takes in a google music playlist dictionary, which contains the field
    'tracks'; itself a list of "properly ordered playlist entry dicts".
    Returns a list of track_type objects, in the order they appear in the
    given playlist. Returned list may be incomplete if not all tracks are
    hosted in GMusic (and thus metadata cannot be accessed via gmusic api),
    in which case a list of those trackIDs will be returned as well.
    """
    playlist = []
    notHosted = []
    for t in pl['tracks']:
        metadata = t.get('track', None)
        if metadata != None:
            song = track(metadata['title'], metadata['artist'])
            playlist.append(song.songStr())
        else:
            notHosted.append(t['id'])

    return (playlist, notHosted)
