#!/usr/bin/env python3

import glob
import subprocess
import os
import sys


print('\nHello, this script will convert mp3 songs in current directory to requested audio format.')
print('Make sure in current dir is no folder called "converted". If it is, move it elsewhere or rename it.')
print('If there already are some files in requested format in current directory, move them.\n')


song_list = glob.glob('*.mp3')



print('There is', len(song_list), 'mp3 files in current directory.')

if len(song_list) < 1:
    sys.exit('I cannot work without mp3 files in current directory.')



output_file = int(input('\nNow select requested output format:\n1 - M4A\n2 - OGG\n3 - WAV\n4 - AAC\n5 - MP3\n'))

if output_file == 1:
    out = 'm4a'
elif output_file == 2:
    out = 'ogg'
elif output_file == 3:
    out = 'wav'
elif output_file == 4:
    out = 'aac'
elif output_file == 5:
    out = 'mp3'
else:
    sys.exit('You inserted unknown request, run program and try it again.')

print('Working on', out)



bitrate_input = int(input('\nSelect requested quality:\n1 - Very high (256 kb/s)\n2 - High (128 kb/s)\n3 - Average (96 kb/s)\n4 - Poor (64 kb/s)\n'))

if bitrate_input == 1:
    bit = 256
elif bitrate_input == 2:
    bit = 128
elif bitrate_input == 3:
    bit = 96
elif bitrate_input == 4:
    bit = 64
else:
    sys.exit('You inserted unknown request, run program and try it again.')

print('Selected quality is', bit, 'kb/s')



os.mkdir('converted')

print('Creating directory "converted"')

for i in song_list:
    subprocess.call(['avconv', '-i', i, '-b', bit + 'k', 'converted/' + i[:-3] + out])

print('Done, converted files can be found in "converted" directory.')
