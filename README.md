# gmusic2spotify

## Current State
Working rudimentary convert.py, with interactive search results choice (when
explicit query did not yield only a single result)

## Usage
Make sure to install gmusic & spotify apis for python:
```
python3 -m pip install -r requirements.txt
```
(can use virtualenv or pipenv for this, see:
 https://docs.python-guide.org/dev/virtualenvs/)

Additionally, ensure that your environment variables are appropriately set (see
below). Then, run the following to ensure that login to both platforms is
working:
```
source scripts/envSetup.sh
cd tests
python3 runonce.py
python3 test_spotipy_login.py
```
And finally, 
```
cd ..
python3 convert.py
```
The final command above will walk you through playlist transferral. Go into
convert.py and change interactive=False in the call to spotify.new_playlist()
(or remove the parameter) to not go through the search errors resolution
process, and simply write the failures to a file.
Failures/errors (if any) will be written to a file regardless of if you opt for
an interactive session or not.



## Environment Setup
Set up all necessary variables via env vars:

|        Variable          |                   Value                  |
|:------------------------:|:----------------------------------------:|
| GMUSIC_USERNAME          | \<your-google-music-username\>           |
| GMUSIC_PW                | NOTE: not needed                         |
| SPOTIFY_CLIENT_ID        | \<your-spotify-client-id\>               |
| SPOTIFY_CLIENT_SECRET    | \<your-spotify-client-secret\>           |
| SPOTIFY_REDIRECT_URI     | can be just 'http://localhost/'          |
| SPOTIFY_USERNAME         | username or email used for Spotify login |
| GMUSIC_OAUTH_CREDS_PATH  | desired path to store oauth token        |

I use a simple script to set these values, aka one .sh file with a lot of
 ```
 export GMUSIC_USERNAME='xxxxx'
```
So the whole setup process is:
```
python3 -m pip install virtualenv
python3 -m virtualenv VENV
source VENV/bin/activate
python3 -m pip install -r requirements.txt
source scripts/envSetup.sh
```

## Tests
### Google Music
**Run this once, then can use other tests **<br/>
Gets/stores oauth credentials in path indicated by environment variable 
GMUSIC_OAUTH_CREDS_PATH:
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

### Spotify
test basic login functionality
```
source scripts/envSetup.sh
cd tests/
python3 test_spotipy_login
```
spotify search function demo
```
source scripts/envSetup.sh
cd tests/
python3 test_spotipy_login
```
