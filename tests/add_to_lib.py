import sys
sys.path.append('../')
import os
import gmusic

title1 = "All songs part 1"
title2 = "All songs part 2"
gm_api = gmusic.login_to_gmusic_with_oauth()
allPlEntries = gm_api.get_all_user_playlist_contents()
allTrackData = gm_api.get_all_songs()
allPt1 = next((p for p in allPlEntries if p['name'] == title1), None)
allPt2 = next((p for p in allPlEntries if p['name'] == title2), None)
badtrackID = ''
storeIdsToAdd = []
# compile a list of storeId's: this gathers storeIds from 'good' plEntries,  or
# gets the corresponding storeId from the allTrackData dict with a matching
# 'id' field. This second process is another search (slower), which is why it's
# not done for every track.
# plEntry['id'] == track['id']
# ^from a playlist    ^from get_all_songs()
for t in allPt1['tracks']:
    if t['source'] == '1':
            badtrackID = t['trackId']
            # match trackId of a 'plEntry' object with id field of 'track' object
            song = next(t for t in allTrackData if t['id'] == badtrackID)
            storeIdsToAdd.append(song['storeId'])
    else:
        storeIdsToAdd.append(t['track']['storeId'])
print(len(storeIdsToAdd))
print(*storeIdsToAdd)
# gmusic.add_tracks_to_lib(title2, gm_api)
#new_lib_ids = gm_api.add_store_tracks(storeIdsToAdd)
#print(len(new_lib_ids))
