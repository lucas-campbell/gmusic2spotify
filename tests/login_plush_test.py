#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

def main():

    #(u, pw) = get_u_pw()

    # Get a MobileClient api
    gm_api = gmusic.login_to_gmusic_with_oauth()
    all_songs = gm_api.get_all_user_playlist_contents()
    plush = next((p for p in all_songs if p['name'] == 'Plush'), None)
    all_song_meta_data = gm_api.get_all_songs()

    badtrackID = ''
    count  = 0
    for t in plush['tracks']:
        # Check for bad source.
        # '2' indicates hosted on Google Music, '1' otherwise
        if t['source'] == '1':
            badtrackID = t['trackId']
            song = next(t for t in all_song_meta_data if t['id'] == badtrackID)
            print(song)
            break
        else: # t['source'] == '2'
            print(t['track']['title'])
        count += 1
    print(count)
    print(plush['tracks'][0])
        
#    print (sources.count('1'))
#    print (errors)

    #p = gmusic.convert_playlist("Plush", gm_api)

    #print(p)

if __name__ == "__main__":
    main()
