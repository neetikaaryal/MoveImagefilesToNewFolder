import os
import shutil
#try and except will only run if runable else it ignores the code 
try:
    os.mkdir("imgFolder") #making new folder imgFolder 
except:
    pass 
f=os.listdir() #list of names of existing folder and files
for ffile in f:
    if os.path.isdir(ffile): # if ffile a directry?
        continue #skip ffile
    if ffile.split(".")[1] == "jpg" or ffile.split(".")[1] == "png": #choose only image files
        print(ffile.split(".")[1])
        shutil.move(ffile,"imgFolder") #moves files from ffile to imgFolder
    
