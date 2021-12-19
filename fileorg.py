import os
import shutil

#Write the name of the directory that needs to be sorted

path=input("Enter the name of directory to be sorted : ")

list_of_files=os.listdir(path)

# Loop to split the ext from root

for file in list_of_files:
    name, ext= os.path.splitext(file)
    ext=ext[1:]

    if ext=="":
        continue

    if os.path.exists(path+'/'+ ext):
        shutil.move(path+'/'+file, path+'/'+ext+ '/'+file)
    
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+ '/'+file)