import os
import pathlib
from datetime import datetime
# os.chdir(r'D:/') # change the location
# print(os.getcwd())# GET CURRENT LOCATION
# os.makedirs("Tutorials") # if taken directory doesnt exit, creates it
# os.mkdir("Made-directory/Sub-directory1") #creates a directory in a created directory
# os.rmdir("Made-directory/Sub-directory1") # delete last taken directory
# os.removedirs("Made-directory/Sub-directory2") # delete all path
# # os.rename("ex15_sample.txt", "demo.txt")
# os.path.splitext() # creates tuple. Firtst element has a filename and second has an extention
# b = os.listdir() # get information of objects in the current directory
# for line in b:
    # if line == "Gladiator-Dewey_Gram_Audio.zip":
    #     os.startfile(os.getcwd() + f"/{line}")
# print(os.stat("demo.txt")) # get infirmation of a file
# mod_time = os.stat("demo.txt").st_mtime # get last time of changing of an object
# print(datetime.fromtimestamp(mod_time)) # convert mod_time to the readable date
for dirpath, dirnames, filenames in os.walk(r'D:/'): #walk through directories, return theyr containing
    # print("Current Path: ", dirpath)
    # print("Directories: ", dirnames)
    for extention in dirnames:
        if extention[-2:] == "py":
            print(dirnames)
    # print("Files: ", filenames)
# print(os.path.basename(r'D:/Scripts'))
# print(os.path.dirname(r'D:/Scripts'))
# print(os.path.split(r'D:/Scripts'))
# print(os.path.exists(r'D:/Scripts'))
# b = os.path.relpath("Desktop_191001_2050.jpg")
# print(os.getlogin())


# print(os.stat_result("ex1.py"))
# print(os.path.abspath('0.jpg'))
