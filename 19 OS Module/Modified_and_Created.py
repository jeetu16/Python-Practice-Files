import time,os

# get modified and created time of a file

path = "G:\\Books in pdf form\\Computer Science Books"

list_of_files = os.listdir(path)

# Method 1
# for file in list_of_files:
#     print('*'*110)
#     print(file)
#     print("Created Time: ",time.ctime(os.stat(path+"\\"+file).st_ctime))
#     print("Modified Time: ",time.ctime(os.stat(path+"\\"+file).st_mtime))

# print('*'*110)

# Method 2
for file in list_of_files:
    created_time = time.ctime(os.path.getctime(path+"\\"+file))
    modified_time = time.ctime(os.path.getmtime(path+"\\"+file))
    print('*'*110)
    print(file)
    print("Created Time: ", created_time)
    print("Created Year: ",created_time[-4:])
    print("Modified Time: ", modified_time)
    print("Modified Year: ", modified_time[-4:])
print('*'*110)
