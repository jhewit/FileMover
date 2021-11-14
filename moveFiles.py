import os
import glob
import shutil
from pathlib import Path

FILE_TYPE = '.wav'
SOURCE_DIRECTORY = ''
TARGET_DIRECTORY = ''
CURRENT_DIRECTORY = os.getcwd()

def print_files(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            print(os.path.join(path, name))

def get_folder_path(file):
    file_path = Path(file).parts[-1]
    dir_path = file[0:(file.find(file_path) - 1)]
    return dir_path

def move_files(source_path, target_path):

    files_moved = 0

    for files in glob.glob(source_path + '/**/*' + FILE_TYPE, recursive=True):
        if get_folder_path(files) != source_path:
            shutil.move(files, target_path)
            files_moved += 1
        else:
            print('Skipping ' + files + '...')
    print('\nFinished moving ' + str(files_moved) + ' files.\n')
    print('********************************************************************\n')

print('********************************************************************\n')

print("The current directory is: " + CURRENT_DIRECTORY)
input("Press Enter to see all files\n")
print_files(CURRENT_DIRECTORY)
print('\n')

print('********************************************************************\n')

entry = input("Would you like to move all " + FILE_TYPE + " files in sub-folders into this directory?\n\nEnter 'Y' for Yes and 'N' for No: ")
print('')

if entry == 'Y' or entry == 'y':
    move_files(CURRENT_DIRECTORY, CURRENT_DIRECTORY)
else:
    if SOURCE_DIRECTORY != '' or TARGET_DIRECTORY != '':
        entry = input("Would you like to move all " + FILE_TYPE + " files from " +
                    SOURCE_DIRECTORY + " to " + TARGET_DIRECTORY + "?\n\nEnter 'Y' for Yes and 'N' for No: ")
        if entry == 'y' or entry == 'Y':
            move_files(SOURCE_DIRECTORY, TARGET_DIRECTORY)
        else:
            print("Why did you even use this program?")
    else:
        print("Oh, okay. Fuck you, then.\n")
        