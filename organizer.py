import os
import shutil

# input folder dir
# look for extensions and organize into folder categories
# if organized print a message alerting that files are already correctly organized

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def category(dir_path):
    # Documents
    # Archive
    # Audio
    # Video
    # Applications
    # Others

    category = ["Documents", "Archive", "Audio", "Video", "Applications", "Others"]

    for i in category:
        if not os.path.isdir(f"{dir_path}/{i}"):
            os.mkdir(f"{dir_path}/{i}")
        

def organize(dir_path):
    # get the current working directory path to traverse through it later on.
    if os.path.isdir(dir_path):

        print(bcolors.OKGREEN + "PATH EXISTS" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Invalid directory path specified!" + bcolors.ENDC)


for filename in os.listdir():
    if filename.endswith(".mkv"):
        base, extension = os.path.splitext(filename)



category("sample_data")
organize("sample_data")