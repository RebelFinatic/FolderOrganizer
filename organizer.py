import os
import shutil

# input folder dir
# look for extensions and organize into folder categories
# if organized print a message alerting that files are already correctly organized

extensions = {
  "Documents": ["pdf", "doc", "docx", "txt", "xls", "xlsx", "xml"],
  "Archive": ["7z", "zip", "rar", "tar", "gz"],
  "Audio": [],
  "Video": ["mp4", "mkv", "mov"],
  "Images": [],
  "Applications": [],
  "Others": []

}

############ DONT EDIT BELOW HERE ############

category = list(extensions.keys())
ext = list(extensions.values())
#print(ext)
#print(extensions)

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

def categorize(dir_path):
    for i in category:
        if not os.path.isdir(f"{dir_path}/{i}"):
            os.mkdir(f"{dir_path}/{i}")
        

def organize(dir_path):

    # get the current working directory path to traverse through it later on.
    if os.path.isdir(dir_path):
        categorize(dir_path)
        print(bcolors.OKGREEN + "PATH EXISTS" + bcolors.ENDC)
        for filename in os.listdir(dir_path):
            #for i in extensions[]
            for i in category:
                for x in extensions[i]:
                    if filename.endswith(x):
                        print(x)
                        #base, extension = os.path.splitext(filename)

    else:
        print(bcolors.FAIL + "Invalid directory path specified!" + bcolors.ENDC)

#categorize("sample_data")
organize("sample_data")