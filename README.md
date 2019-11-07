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

## Running Tests
**Only need to run once**<br/>
Gets/stores oauth credentials in path indicated by OAUTH_CREDS_PATH
```
python3 tests/runonce.py
```

```
python3 tests/test.py
```