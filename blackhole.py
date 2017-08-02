"""A program for automatically organizing files."""
import os
import time
import json

with open("blackhole.json") as data_file:
    data = json.load(data_file)
watch_directory = data["watch_directory"]

def movefile(filename, fileextension):
    path = getpathforfilename(filename)
    if not path:
        path = getpathforextension(fileextension)
    if path:    
        #Check for directory.  
            #If not there, create.
        #Put in try/except.
        os.rename(watch_directory+filename+fileextension, path+filename+fileextension)

def getpathforextension(extension):
    path = ""
    for hext in data["handle_extensions"]:
        for ext in hext["extensions"]:
            if extension == ext:
                path = hext["directory"]
    return path

def getpathforfilename(filename):
    path = ""
    for hfn in data["handle_filenames"]:
        for fn in hfn["filenames"]:
            if filename.find(fn)>-1:
                path = hfn["directory"]
    return path

#Update this to just look for files in watch directory.
before = dict([(f, None) for f in os.listdir (watch_directory)])
while True:
    time.sleep(3)
    after = dict([(f, None) for f in os.listdir (watch_directory)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    before = after

    for f in added:
        filename, file_extension = os.path.splitext(f)
        movefile(filename, file_extension)
