#quickfix for tests
import sys
sys.path.append('../')
import os
import gmusic

def find_oauth_creds():
    return os.getenv('OAUTH_CREDS_PATH')

secret_path = find_oauth_creds()
gm_api = gmusic.onetime_perform_oauth(secret_path)

