import os,shutil

source_path = "G:\\Books in pdf form\\Computer Science Books"

list_of_files = os.listdir(source_path)

# print(list_of_files)

for file in list_of_files:
    file_size = ((os.stat(source_path + "\\" + file).st_size)/(1024*1024))
    if os.path.isdir(source_path + "\\" + file):
        continue
    if file_size >5:
        print(f"{file} : {file_size:.2f}")
        # print(f"{file_size:.2f}",f"{file_size:.2f}")