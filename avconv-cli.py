#!/usr/bin/env python3

import glob
import subprocess
import os


bitrate_input = input('\nHello, this script will convert mp3 songs in current directory to m4a audio format.\nMake sure in current dir is no folder called "converted". If it is, move it elsewhere or rename it.\nIf there already are some m4a files in current directory, move them.\n\nNow set number of bitrate, in kbps. If you want to use default, insert 0: ')

song_list = glob.glob('*.mp3')

os.mkdir('converted')

bitrate = int(bitrate_input)

if bitrate == 0:
    bitrate = 96
elif bitrate < 0:
    print('Bitrate have to be more than 0!')

for i in song_list:
    subprocess.call(['avconv', '-i', i, '-b', str(bitrate) + 'k', 'converted/' + i[:-3] + 'm4a'])

