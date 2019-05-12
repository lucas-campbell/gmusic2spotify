#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

#def setup0():
#    u = os.getenv('GMUSIC_USERNAME')
#    pw = os.getenv('GMUSIC_PW')
#    return (u, pw)

def setup1():
    return os.getenv('OAUTH_CREDS_PATH')


#(u, pw) = setup()
secret_path = setup1()

#gm_api = gmusic.onetime_perform_oauth(secret_path)
#gm_api = gmusic.login_to_gmusic(u, pw)
gm_api = gmusic.login_to_gmusic_with_oauth()

p = gmusic.convert_playlist("Plush", gm_api)

print(p)
