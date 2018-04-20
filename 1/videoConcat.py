#-*- coding: utf-8 -*-

import os
import re
from functools import cmp_to_key

# define a compare function to apply in sorted
def compare(a, b):
    pattern = re.compile('(\d+).flv$')
    num1 = int(pattern.findall(a)[0])
    num2 = int(pattern.findall(b)[0])
    return num1 - num2

# generate configurate file for ffmpeg
def createFile(path):
    dirInMain = os.listdir(path)
    for adir in dirInMain:
        paths = os.path.join(path, adir)
        if os.path.isdir(paths):
            subdirs = os.listdir(paths)
            subdirs = [i for i in subdirs if i.endswith('.flv')]
            subdirs = sorted(subdirs, key=cmp_to_key(compare))
            f = open(adir+'.txt', 'w')
            for i in subdirs:
                    f.write("file \'"+paths+'\\'+ i + "\'\n")
            f.close()

# merge some .flv file to a .mp4 file            
def createVideo():
    files = os.listdir()
    for i in files:
        if i.endswith('.txt'):
            if os.path.getsize(i):
                os.system(r".\ffmpeg -f concat -safe 0 -i " + i + " -c copy " + i.rstrip('.txt')+'.mp4')
            os.remove(i)
            
if __name__ == "__main__":
    mainPath = os.path.pardir
    createFile(mainPath)
    createVideo()
    
