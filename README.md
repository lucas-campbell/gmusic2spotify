# gmusic2spotify

## Current State
12/5/2019
Unable to move forward because of apparent inconsistencies in Google Music's
underlying representation of a track

## Usage
1. make sure to
```
pip install gmusicapi
```
(can use virtualenv or pipenv for this, see:
 https://docs.python-guide.org/dev/virtualenvs/)

2. Install gmusic api library for python
```
python3 -m pip install gmusicapi
```

## Environment Setup
Set up all necessary variables via env vars:

|        Variable       |                   Value                  |
|:---------------------:|:----------------------------------------:|
| GMUSIC_USERNAME       | \<your-google-music-username\>           |
| GMUSIC_PW             | \<your-google-music-password\>           |
| SPOTIFY_CLIENT_ID     | \<your-spotify-client-id\>               |
| SPOTIFY_CLIENT_SECRET | \<your-spotify-client-secret\>           |
| SPOTIFY_REDIRECT_URI  | often just 'http://localhost/'           |
| SPOTIFY_USERNAME      | username or email used for Spotify login |
| OAUTH_CREDS_PATH      | desired path to oauth token              |

I use a simple script to set these values, aka a lot of
 ```
 export GMUSIC_USERNAME='xxxxx'
```

## Tests
### Google Music
**Run this once, then can use other tests **<br/>
Gets/stores oauth credentials in path indicated by environment variable 
OAUTH_CREDS_PATH:
```
source scripts/envSetup.sh
cd tests/
python3 runonce.py
```

Infinite loop that waits for the name of a playlist on the command line and
checks that the playlist is available to the API. Useful for quick testing of
API access.
```
source scripts/envSetup.sh
cd tests/
python3 test_get_gmusic_playlist.py
```

Prints contents (titles + number of songs) to command line.
```
source scripts/envSetup.sh
cd tests/
python3 print_playlist_contents.py <Title of playlist>
```
