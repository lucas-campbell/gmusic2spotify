import sys
from gmusicapi import Mobileclient
from gmusicapi import Webclient

def login_to_gmusic(username, password):
        """ params: obvious
        returns the gmusic api object that has been authenticated """
        
        api = Mobileclient()
        api.login(email=username, password=password, android_id=api.FROM_MAC_ADDRESS, locale='en_US')
        if api.is_authenticated():
                print('Logged in to Google Music!')
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
