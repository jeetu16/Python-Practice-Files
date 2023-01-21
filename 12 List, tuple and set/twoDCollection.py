
# ---> 2D List of List 
'''
fruits = ['apple','banana','mango','kiwi','orange']
vegetables = ['onion','potatoes','beans']
meats = ['fish','chicken','mutton','turkey']

groceries = [fruits,vegetables,meats]

# updating 2D list element
groceries[0][1] = 'Watermelon'

# iterating 2d list from for loop
for collections in groceries:
    for item in collections:
        print(item, end=" ")
    print()
'''

# 2D list of tuples
'''
num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")]

# iterating 2d list of tuples
for collection in num_pad:
    for num in collection:
        print(num,end=" ")
    print()

# we can't change the tuple element inside 2d list of tuples
num_pad[0][1] = 33  # TypeError: 'tuple' object does not support item assignment
'''

# 2D list of sets
num_pad = [{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}]

# we can't change set element inside two list of sets
# num_pad[0][2] = 16  # TypeError: 'set' object does not support item assignment



'''
# 2D tuple of lists
num_pad = ([1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"])

# 2D tuple of tuples
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# 2D tuple of sets
num_pad = ({1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"})

# 2D set of lists (NOT VALID)
num_pad = {[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]}

# 2D set of tuples
num_pad = {(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")}

# 2D set of sets (NOT VALID)
num_pad = {{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}}
'''


for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
