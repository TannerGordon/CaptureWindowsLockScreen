# Call me Mr. Comp Sci
# Author: Tanner Gordon
# Date: 9/29/21
# Description: Captures 6 backgrounds from windows home page and inserts them
#              in directory labeled 'Captured_Backgrounds'
# Notes:       This file and corrosponding folder must be in Desktop Directory

import os 
import shutil

path = '../../tjgor\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets/'

files = os.listdir(path)
# size = os.path.getsize(path)
arr = []
for f in files:
    arr.append(f)

def sortBySize(f):
    return os.path.getsize(path + f)

arr.sort(reverse=True, key=sortBySize)

for i in range(6):
    shutil.copyfile(path + arr[i], './Captured_Backgrounds/' + arr[i])

os.chdir('./Captured_Backgrounds/')
os.system('ren *.* *.jpg\n')
# out, err = p.communicate()
# os.path.join('/Captured_Backgrounds', 'bgOG.jpg.png')
# os.rename('bgOG.jpg.png', './Captured_Backgrounds/bgOG.jpg.png')
# print(os.listdir('.'))
# print(arr)
#     f = os.path.getsize(path + f)
#     print(f)

# print(size)