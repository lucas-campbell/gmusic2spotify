import sys
sys.path.append('../')
import gmusic
import spotify
from Track import *
from Playlist import *

def main():

    # Google Music MobileClient api
    gm_api = gmusic.login_to_gmusic_with_oauth()
    all_songs = gm_api.get_all_user_playlist_contents()

    # Spotify api
    sp_api = spotify.login2spotify()
    user = sp_api.me()
    sp_user_id = user['id']

    found = False
    while not found:
        try:
            pl_name = input("Playlist name: ")
            pl = next((p for p in all_songs if p['name'] == pl_name), None)
            if pl == None:
                print('Could not find playlist with name ', pl_name,
                        ', please try again.')
            else:
                found = True
        except EOFError:
            print('Ok yes goodbye')
            sys.exit(1)

    # Found desired playlist, so get data about its tracks
    all_song_meta_data = gm_api.get_all_songs()

    badtrackID = ''
    tracks = []
    count = 0
    for t in pl['tracks']:
        # Check for bad source.
        # '2' indicates hosted on Google Music, '1' otherwise
        if t['source'] == '1':
            badtrackID = t['trackId']
            song = next((t for t in all_song_meta_data if t['id'] == badtrackID), None)

        else: # t['source'] == '2'
            song = t['track']

        if song is not None:
            count += 1

        title = song['title']
        artist = song['artist']
        album = song['album']

        track = Track(title=title, artist=artist, album=album)
        tracks.append(track)

    new_playlist = Playlist(tracks=tracks, plTitle=pl_name)
    print('ok, added ', count, ' songs to Playlist object with length ', new_playlist.length)
    spotify.new_playlist(sp_api, new_playlist)


if __name__ == "__main__":
    main()
