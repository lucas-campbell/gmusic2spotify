# GMusic_modules.py -- interactions with gmusicapi

import sys
from gmusicapi import Mobileclient
from track import track

def onetime_perform_oauth(path, open_browser=False):
    """
    params: path to store oauth credentials, after a call to this you should
    only need to call api.oauth_login()
    returns authenticated api
    """
    api = Mobileclient()
    #f = open(path, "w")
    api.perform_oauth(path, open_browser)

    #api.perform_oauth(f, open_browser)
    return api
    
def login_to_gmusic_with_oauth():
    api = Mobileclient()
    if api.oauth_login(api.FROM_MAC_ADDRESS, \
            oauth_credentials=u'/home/lucas/.local/share/gmusicapimobileclient.cred', locale=u'es_ES'):
        return api
    else:
        sys.stderr.write('error logging in, exiting program')
        sys.exit()
def login_to_gmusic(username, password):
    """
    params: username & password for your gmusic account
    returns the authenticated gmusic api object
    """
    api = Mobileclient()
    #api.oath_login(
#    api.login(email=username, password=password, \
#              android_id=api.FROM_MAC_ADDRESS, locale=u'es_ES')
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
            playlist.append("Error: Song not hosted on Gmusic")
            notHosted.append(t['id'])

    return (playlist, notHosted)
