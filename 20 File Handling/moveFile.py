import os
import shutil


# os.replace(src,destination) is used to move the file within same drive
'''
source = "F:\\Python Practice Files\\19 File Handling\\movableFile1.txt"
destination = "F:\\movedFile.txt"

try:
    if os.path.exists(destination):
        print("There is a file there")
    else:
        os.replace(source,destination)  # moving file
        print("File is moved to the destination")
except FileNotFoundError:
    print("File not found ")
'''

# for moving a file into another drive we have use shutil.move(src,destination)

source = "F:\\Python Practice Files\\19 File Handling\\movableFile2.txt"
destination = "G:\\Program Files\\movedFile.txt"

try:
    if os.path.exists(destination):
        print("There is a file there")
    else:
        shutil.move(source, destination)    # moving file
        print("File is moved to the destination")
except FileNotFoundError:
    print("File not found ")
