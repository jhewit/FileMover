import os
import glob
import shutil
from pathlib import Path

FILE_TYPE = '.wav'

def print_files(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            print(os.path.join(path, name))

def get_folder_path(file):
    file_path = Path(file).parts[-1]
    dir_path = file[0:(file.find(file_path) - 1)]
    return dir_path

def move_files(path):

    for files in glob.glob(path + '/**/*' + FILE_TYPE, recursive=True):
        if get_folder_path(files) != path:
            shutil.move(files, path)
        else:
            print('Skipping ' + files + '...')
    print('\nDone.\n')
    print('********************************************************************\n')

path = os.getcwd()

print('********************************************************************\n')

print("The current directory is: " + path)
input("Press Enter to see all files\n")
print_files(path)
print('\n')

print('********************************************************************\n')

entry = input("Would you like to move all .wav files in sub-folders into this directory?\n\nEnter 'Y' for Yes and 'N' for No: ")
print('')

if entry == 'N' or entry == 'n':
    print("Oh, okay. Fuck you, then.")
else:
    move_files(path)
