#!/usr/bin/env python3

import glob
import subprocess
import os


song_list = glob.glob('*.mp3')

#for x in song_list:
    #print(x)
    #print(x[:-3] + 'm4a')

for i in song_list:
    subprocess.call(['avconv', '-i', i, '-b', '96k', i[:-3] + 'm4a'])


#song_list_converted = glob.glob('*.m4a')

#os.mkdir('converted')
#subprocess.call(['mv', song_list_converted, 'converted/'])

