# Capture Windows Lock Screen Spotlight Images
# Author: Tanner Gordon
# Date: 9/29/21
# Description: Captures 6 backgrounds from windows home page and inserts them
#              in directory labeled 'Captured_Backgrounds'
# Notes:       There are a few must-haves for this program to work
#           1. The path must reach correctly. Please update the myUser variable
#           2. Create a directory called 'Captured_Backgrounds' and keep it where
#              this program lives. Your images will save into this directory
import os 
import shutil

# in order for this program to work for you, you must change {username} to your PC username
myUser = '../../{username}' # additionally, the '../../' brings me from current directory to where my
                            # PC username directory lives. I like to keep this program in my Desktop
                            # directory, but wherever you put it, make sure the path reaches username
path = '\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets/'
# the above path is how to navigate to the recently used Windows Lock Screen Spotlight Images
# the full path is:
# %userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
path = myUser + path

files = os.listdir(path)
arr = []
for f in files:
    arr.append(f)

def sortBySize(f):
    return os.path.getsize(path + f)
# sorts files by size and puts the greatest files first
arr.sort(reverse=True, key=sortBySize)
# copies 5 largets files and moves them into 'Captured_Backgrounds' directory
for i in range(6):
    shutil.copyfile(path + arr[i], './Captured_Backgrounds/' + arr[i])
# these commands convert the files into png images!!!
os.chdir('./Captured_Backgrounds/')
os.system('ren *.* *.jpg\n')
