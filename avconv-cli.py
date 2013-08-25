#!/usr/bin/env python3

import glob
import subprocess

song_list = glob.glob('*.mp3')

for x in song_list:
    print(x)
    print(x[:-3] + 'm4a')

for i in song_list:
    print('avconv', '-i', i, '-b', '96k', i[:-3] + 'm4a')

