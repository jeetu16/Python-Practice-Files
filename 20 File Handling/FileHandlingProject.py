import os,shutil


extensions = []

source_path = "F:\\Everything"
destination_path = "G:\\Dumy New"

# storing all files name
list_of_files = os.listdir(source_path)


# getting extensions of files
for file in list_of_files:
    extensions.append(file.split('.')[-1])

# removing duplicate extensions using set()
extensions = list(set(extensions))

for ex in extensions:
    # making directory for storing files 
    os.mkdir(destination_path + "\\" + ex.upper())
    for file in list_of_files:
        if ex in file.split('.')[-1]:
            # Here files are copying from source to destination
            shutil.copy(source_path+"\\"+file,destination_path+"\\"+ex.upper())

