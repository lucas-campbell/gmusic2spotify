import os
import gmusic

def setup():
    u = os.getenv('GMUSIC_USERNAME')
    pw = os.getenv('GMUSIC_PW')
    return (u, pw)

(u, pw) = setup()
gm_api = gmusic.login_to_gmusic(u, pw)

p = gmusic.convert_playlist("Plush", gm_api)

print(p)
