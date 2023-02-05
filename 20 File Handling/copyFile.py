# copyfile() =  copies contents of a file
# copy()     =  copyfile() + permission mode + destination can be a directory
# copy2()    =  copy() + copies metadata (file’s creation and modification times)

# copy in the same directory and within the drive
'''
import shutil
try:
    shutil.copy2('.//19 File Handling//textFile.txt', './19 File Handling//copy.txt') # (source, destination)
except FileNotFoundError:
    print("File not found")
'''

# copy in different drive

import shutil
try:
    shutil.copy2('.//19 File Handling//textFile.txt',
                 'G://Program Files//copy.txt')  # (source, destination)
except FileNotFoundError:
    print("File not found")
