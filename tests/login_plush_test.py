#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

def get_u_pw():
    u = os.getenv('GMUSIC_USERNAME')
    pw = os.getenv('GMUSIC_PW')
    return (u, pw)

def main():

    (u, pw) = get_u_pw()

    gm_api = gmusic.login_to_gmusic_with_oauth()

    p = gmusic.convert_playlist("Plush", gm_api)

    print(p)

if __name__ == "__main__":
    main()
