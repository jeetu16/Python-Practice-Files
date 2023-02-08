import os
import shutil

path = "G:\\Program Files\\Not Empty Folder"

try:
    # os.remove(path)         # for deleting the file
    # os.rmdir(path)          # for deleting the empty dir(folder)
    shutil.rmtree(path)     # for deleting the folder which is not empty
except FileNotFoundError:
    print("That file/folder is not found to the given path")
except PermissionError:
    print("You do not have permission to delete a folder using os.remove()")
except OSError:
    print("You can not delete that non-empty folder using os.rmdir() method")
else:
    print("File sucessful deleted")
