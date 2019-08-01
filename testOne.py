#!/usr/bin/env python
# coding: utf-8

# In[99]:


import shutil
import os
from os import path

def main():
    mainDirectory = input("-->")
    for directory in os.listdir(mainDirectory):
        if(os.path.isdir(directory)):
            individualFire(directory)

    def indivudalFire(currentDirectory):

            def convert(list):
                res = ''
                for i in list: 
                    res += i     
                return res
                   
        if currentDirectory.endswith("/"):
            currentDirectory = currentDirectory[:-1]
            print(currentDirectory)

        name = convert(convert(currentDirectory.split("-")[1:]).split("FIgLib/"))

        afterDir = currentDirectory + "/"+ name + "AFTER"
        beforeDir = currentDirectory +"/"+ name + "BEFORE"

        try:
            os.mkdir(afterDir)
        except FileExistsError:
            print("already run")
        try:
            os.mkdir(beforeDir)
        except FileExistsError:
            print("already run")

        for filename in os.listdir(currentDirectory):
            abspath = currentDirectory+"/"+filename
            if ord(filename[0]) <= 57 and filename.endswith(".jpg"):
                if("+" in filename):
                    shutil.copy(abspath, afterDir)
                elif("-" in filename):
                    shutil.copy(abspath, beforeDir)
                    
