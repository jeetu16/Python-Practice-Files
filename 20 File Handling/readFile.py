import os


# There are some file opening modes present by default it's (read)'r' mode 

try:
    # using 'with open(filePath, openingMode(optional)):'  we can open a file
    with open('F:\\Python Practice Files\\19 File Handling\\textFile.txt') as fe:

        # here with help of read() function we can read a file
        print(fe.read())
except FileNotFoundError:
    print("That file was not find")


# print(fe.closed) # here we checking file close or not it gives True/False
