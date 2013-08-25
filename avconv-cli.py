#!/usr/bin/env python3

import glob
import os

song_list = glob.glob('*.mp3')

for x in song_list:
    print(x)

os.mkdir(converted)

