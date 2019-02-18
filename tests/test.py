#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

def setup():
    u = os.getenv('GMUSIC_USERNAME')
    pw = os.getenv('GMUSIC_PW')
    return (u, pw)

(u, pw) = setup()

#secret_path = '/home/lucas/.local/share/gmusicapimobileclient.cred'
#gm_api = gmusic.onetime_perform_oauth(secret_path, open_browser=True)
#gm_api = gmusic.login_to_gmusic(u, pw)
gm_api = gmusic.login_to_gmusic_with_oauth()

p = gmusic.convert_playlist("Plush", gm_api)

print(p)
