import sys
sys.path.append('../')
import os
import gmusic
from login_plush_test import get_u_pw

title1 = "All songs part 1"
title2 = "All songs part 2"
(u, pw) = get_u_pw()
gm_api = gmusic.login_to_gmusic_with_oauth()
gmusic.add_tracks_to_lib(title2, gm_api)
