#!/usr/bin/env python3

import glob
import os
import subprocess

song_list = glob.glob('*.mp3')

for x in song_list:
    print(x)

os.mkdir('converted')

subprocess.call('for i in *.mp3; do avconv -i "${i}" -b 94k "${i%.mp3}.m4a"; done', shell=True)
subprocess.call('mv *.m4a converted', shell=True) 

