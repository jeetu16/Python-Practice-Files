import os

# if file is present in your current working directory then no need to give full path
 
pt = "F:\\Python Practice Files\\19 File Handling\\textFile.txt"

if os.path.exists(pt):              # checking location exist or not
    print("That location exits")
    if os.path.isfile(pt):          # checking selected path is file or not
        print("It is a file")       
    elif os.path.isdir(pt):         # checking selected path is dir(folder) or not
        print("It is a directory")
else:
    print("Doesn't exits")