
txt = "My name is Jeetu\n"

# for writting in a file we have to open a file in write mode 'w'
# also there is a point to be noted if file is not exist in a given path then automatically file created on given path

# when you open a file in write mode 'w' it removes the previous data and inserted the given data

# with open('F:\\Python Practice Files\\19 File Handling\\textFile.txt','w') as fl:
#     fl.write(txt)


# for overcome that problen we can use append mode 'a' which doesn't overwrite the previous data and append the given data after the last character of file

with open('F:\\Python Practice Files\\19 File Handling\\textFile.txt', 'a') as fl:
    fl.write(txt)
