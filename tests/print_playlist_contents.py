#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

def main(argv):

    if len(sys.argv) != 2:
        sys.stderr.write("Error: please supply the name of a playlist\n")
        exit(-1)

    # Get a MobileClient api
    gm_api = gmusic.login_to_gmusic_with_oauth()
    all_songs = gm_api.get_all_user_playlist_contents()
    pl = next((p for p in all_songs if p['name'] == argv[1]), None)
    all_song_meta_data = gm_api.get_all_songs()

    badtrackID = ''
    count  = 0
    for t in pl['tracks']:
        # Check for bad source.
        # '2' indicates hosted on Google Music, '1' otherwise
        if t['source'] == '1':
            badtrackID = t['trackId']
            song = next(t for t in all_song_meta_data if t['id'] == badtrackID)
            song_str = song['title']
            print(song_str, end=", ")
            #break
        else: # t['source'] == '2'
            print(t['track']['title'], end=", ")
        count += 1
    print("")
    print(count)
    #print(pl['tracks'][0])
        
#    print (sources.count('1'))
#    print (errors)

    #p = gmusic.convert_playlist("Plush", gm_api)

    #print(p)

if __name__ == "__main__":
    main(sys.argv)
