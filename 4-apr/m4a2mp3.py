'''
4/13/23 mini description
super annoying quicktime m4a audio export format but fastest sys default audio rip
so easier to create this script and convert in one-go after
'''


import sys
import os
from pydub import AudioSegment

def convert_m4a_to_mp3(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.m4a'):
            input_file = os.path.join(folder_path, file)
            output_file = os.path.join(folder_path, os.path.splitext(file)[0] + '.mp3')
            audio = AudioSegment.from_file(input_file, 'm4a')
            audio.export(output_file, format='mp3')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        folder_path = sys.argv[1]
        convert_m4a_to_mp3(folder_path)
    else:
        print("Usage: python m4a2mp3.py <folder_path>")
