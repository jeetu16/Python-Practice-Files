import os
import shutil

# 1. check current directory(folder).
# path = os.getcwd()
# print(path)

# 2. changes the current workiing dir to given path.
# os.chdir(r"G:/Downloads") 
# print(os.getcwd())

# 3. gives all the dir name list of current working dir.
# lst = os.listdir()
# print(lst)

# 5. given the list of root, directories and files of given path.
'''
for root,dirs,files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
'''

# 6. create dir on a given path or same working directory
'''
try:
    os.mkdir(r'G:/MyDir')
except FileExistsError:
    print("File is already there, can't create")
else:
    print("Sucessfully Created")
'''

# 7. remove the empty directory with help of os.redir(path) method
# os.rmdir(r'G:/New folder')

# 8. remove non-empty directory using shutil.rmtree(path)
# shutil.rmtree(r'G:\Dumy Folder')

# 9. create dir inside dir using os.makedirs(path)
# os.makedirs(r'G:\Dumy Folder\My Dumy Folder')

# 10. remove dir inside dir using os.removedirs(path)
# os.removedirs(r'G:\Dumy Folder\My Dumy Folder')
# shutil.rmtree(r'G:\Dumy Folder')

# 11. rename dir using os.rename(currentName,newName)
# os.rename(r'G:\Dumy',r'G:\Dumy New')


# 12 get file size of any file using os.stat(path).st_size (it gives size in bytes):
'''
get_Size = os.stat(r'G:\ISO File\kali-linux-2017.1-amd64.iso').st_size
get_Size = get_Size/(1024**2)
print("File size is :", get_Size)
'''

# 13 get current User folder path
# currentUser = os.environ['UserProfile'] + '\Desktop'
# print(currentUser)
