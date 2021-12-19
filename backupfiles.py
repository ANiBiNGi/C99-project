import os
import shutil

source = input("Enter the folder you want to backup: ")
destination = input("Enter the destination of this folder: ")

source = source + '/'
destination += '/'
listfiles = os.listdir(source)

for file in listfiles:
    shutil.copy((source+file), destination)