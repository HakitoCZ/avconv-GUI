#!/usr/bin/env python3

import glob
import subprocess
import os
import sys


print('\nHello, this script will convert mp3 songs in current directory to requested audio format.')
print('Make sure in current dir is no folder called "converted". If it is, move it elsewhere or rename it.')
print('If there already are some files in requested format in current directory, move them.')

output_file = int(input('\nNow select requested output format:\n1 - M4A\n2 - OGG\n3 - WAV\n4 - AAC\n5 - MP3\n'))



song_list = glob.glob('*.mp3')



if output_file == 1:
    out = 'm4a'
elif output_file == 2:
    out = 'ogg'
elif output_file == 3:
    out = 'wav'
    print('wav')
elif output_file == 4:
    out = 'aac'
elif output_file == 5:
    out = 'mp3'
elif output_file > 5:
    print('You inserted unknown request, run program and try it again.')

os.mkdir('converted')

bitrate_input = int(input('\nNow set number of bitrate, in kbps. If you want to use default, insert 0\n'))

if bitrate_input == 0:
    bitrate_input = 96
elif bitrate_input < 0:
    print('Bitrate have to be more than 0!')
else:
     print('You inserted unknown request, run program and try it again.')


for i in song_list:
    subprocess.call(['avconv', '-i', i, '-b', str(bitrate_input) + 'k', 'converted/' + i[:-3] + out])

