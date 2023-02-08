import os

# os.listdir() : gives the all the name of the files,dirs(folder) of current directory in form of 'List'
# os.listdir(path) : gives the all the name of the files,dirs(folder) of given path in form of 'List'

path = "F:\\"

# print(os.listdir())
# print(os.listdir("../"))  # one directory back
# print(os.listdir(path))

found = False
content = os.walk(path)
fileName = "style.css"
for rt, dr, fl in content:
    if fileName in fl:
        found = True
        print(os.path.join(rt,fileName))

if not found:
    print("File not Found")
