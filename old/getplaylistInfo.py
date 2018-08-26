#!/usr/bin/env/python3

import sys
from code import InteractiveConsole
from gmusicapi import Mobileclient

def add_tracks(f=None, tracks=[], playlist_title=None, api=None):     
        """f is a file object that is being used to write song info for a playlist
        t should be a nonempty list of 'playlist entry' dictionaries
        playlist_title should match the online version exactly
        api should be the gmusicapi MobileClient

        this funtion writes any tracks with valid track IDs to the desired file,
        and logs any others to a separate list object, to be dealt with by log_errors() """

        unadded_tracks = []
        f.write('{}\n\n'.format(playlist_title))
        if tracks != None:
                for t in tracks:
                        if t['trackId'].startswith('T'):
                                track_info = api.get_track_info(t['trackId'])
                                #print('{}, {}\n'.format(track_info['title'], track_info['artist']))
                                f.write('{}, {}\n'.format(track_info['title'], track_info['artist']))
                        else:
                                unadded_tracks.append(t)

        return unadded_tracks

def log_errors(unadded_tracks=None, playlist_title=None):
        if unadded_tracks is None or unadded_tracks == []:
                return
        else:
                missed = open('{}_{}.txt'.format(playlist_title, 'errors'), 'w')
                for m in unadded_tracks:
                        missed.write('{}\n'.format(m))


def main():
        api = Mobileclient()

        api.login(email='EMAIL', password='PW',
                android_id=api.FROM_MAC_ADDRESS)

        if api.is_authenticated():
                print('Successfully logged in')
        else:
                print('error logging in, exiting program')
                sys.exit()

        i = InteractiveConsole()

        num_playlists = int(i.raw_input("How many playlists?: "))
        user_playlists = []
        for x in range(num_playlists):
                user_playlists.append(i.raw_input("playlist name?: "))
        print('playlist names aquired, getting info')

        full_playlist_contents = api.get_all_user_playlist_contents()
        print("got info on ALL playlists")

        f = open(str(i.raw_input("File name to write to (include '.txt'): "), 'w'))
        print('Opened file OK OK')

        count = 0

        #iterate through list of playlist dictionaries
        for p in full_playlist_contents:
                #iterate through separate list of user-given playlist names, match them up
                for playlist_title in user_playlists:
                        if p['name'] == playlist_title:
                                count += 1
                                #['tracks'] returns a list of playlist entry dicts
                                le_tracks = p['tracks']
                                log_errors(add_tracks(f, le_tracks,    
                                        playlist_title, api), playlist_title)

        if count == num_playlists:
                print('\tsuccess!(?)\n\tprocessed {} playlists'.format(count))
        else:
                print('hm didn''nt process the right number of playlists')

if __name__ == '__main__':
        main()
