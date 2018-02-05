"""
tools to handle directories and files. For example create directory, open file, check dir exists.
"""
import os
import sys
import logging

"""
Creates a folder on the given path. If folder exist, overwrite it. 
On error return false.
"""
def createDir(full_path):
    success= True
    try:
        if os.path.exists(full_path):
                pass
        else:
            os.makedirs(full_path,exist_ok=True)
    except:
          e = sys.exc_info()[0]
          logging.exception(e)
          success=False

    return success

#function to handle moving files to appropriate folders
def move(filename, dirpath):
    shutil.move(os.path.join(srcpath, filename), dirpath)
    #creates the folders with three digits as folder name by calling the create function above
    targets = [(folder, create(folder, destpath)) for folder in destdir]
    #handles moving files to appropriate folders if the three digits in file name matches the created folder
    for dirname, full_path in targets:
            for filename in srcfiles:
                    if dirname == filename[19:22]:
                            move(filename, full_path)
                    else:
                        pass
                    
def fileToString(fullpath):
    f = open(fullpath,"r")
    content= f.read()
    return content