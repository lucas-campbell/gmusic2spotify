# gmusic2spotify

## Current State
Unable to move forward because much of the time google music will not show
metadata for a track, even when it should. 12/5/2019

## Usage
Can use virtualenv or pipenv for this, see: https://docs.python-guide.org/dev/virtualenvs/
and https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
According to the above  documentation, 'virtualenv' command is for python 2, and
'venv' command is for python 3. Both use the package called virtualenv?

If not already set up with virtualenv, run the following script. Add the --upgrade flag if necessary.
```
python3 -m pip install --user --upgrade pip
python3 -m pip install --user --upgrade virtualenv
python3 -m venv VENV
source VENV/bin/activate
```

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
| OAUTH_CREDS_PATH      | wherever you want to store oauth token   |

I use a simple script to set these values, aka a lot of
 ```
 export GMUSIC_USERNAME='xxxxx'
```

## Running Tests
**Only need to run once**
Gets/stores oauth credentials in path indicated by OAUTH_CREDS_PATH
```
python3 tests/runonce.py
```

```
python3 tests/test.py
```
