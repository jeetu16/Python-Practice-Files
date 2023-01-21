# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK


# ---> list indexing
'''
fruits = ['apple','orange','banana','coconut','watermelon']
print(fruits[0])      # apple
print(fruits[9])      # IndexError: list index out of range
print(fruits[0:2])    # ['apple', 'orange']
print(fruits[:3])     # ['apple', 'orange', 'banana']
print(fruits[1::2])   # ['orange','coconut']
print(fruits[-1])     # watermelon
print(fruits[::-1])   # ['watermelon', 'coconut', 'banana', 'orange', 'apple']
'''


# iterating lists through for loop
'''
for fruit in fruits:
    print(fruit)
'''


# ---> List[] Methods:

# 1 updating list items
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits[0] = 'Cherry'    # ['Cherry', 'orange', 'banana', 'coconut', 'watermelon']
'''

# 2 list.append(object) : Append object to the end of the list.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.append('Kiwi')   # ['Cherry', 'orange', 'banana', 'coconut', 'watermelon', 'Kiwi']  
'''


# 3 list.clear() : Remove all items from list.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.clear()      # []
'''


# 4 list.copy() : Return a shallow copy of the list.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits_copy = fruits.copy()     # ['apple', 'orange', 'banana', 'coconut', 'watermelon']
'''


# 5 list.count(value) : Return number of occurrences of value.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon','apple']
fruits.count("Kiwi")        # 0 because 'Kiwi' doesn't exist in fruits list
fruits.count("apple")       # 2
'''


# 6 list.extend(iterable) : Extend list by appending elements from the iterable.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.extend(['Kiwi','Cherry'])    # ['apple', 'orange', 'banana', 'coconut', 'watermelon', 'Kiwi', 'Cherry']
'''


# 7 list.index(value) : Return first index of value.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.index('banana')  # 2 (index number)
fruits.index('Tomato')  # ValueError: 'Tomato' is not in list
'''


# 8 list.insert(index, object) : Insert object before index.
'''


fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.insert(2,"Kiwi") # ['apple', 'orange', 'Kiwi', 'banana', 'coconut', 'watermelon']
'''


# 9 list.pop(index=-1) : Remove and return item at index(default last).
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.pop(0)   # remove and return 'apple' because of index 0
fruits.pop()    # remove and return 'watermelon' because of default last index -1
'''


# 10 list.remove(value) : Remove first occurrence of value.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon','apple']
fruits.remove('apple')  # removes first occurance of 'apple' from list fruits
fruits.remove('Kiwi')   # ValueError: list.remove(x): x not in list
'''


# 11 list.reverse() : Reverse *IN PLACE*.
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
fruits.reverse()    # ['watermelon', 'coconut', 'banana', 'orange', 'apple']
'''


# 12 list.sort(self, /, *, key=None, reverse=False):Sort the list in ascending order and return None.
'''

nums = [100,1,20,4,3,10]
nums.sort()                 # [1, 3, 4, 10, 20, 100] sort in ascending order
nums.sort(reverse=True)   # [100, 20, 10, 4, 3, 1] sort in descending order

fruits = ['orange', 'apple', 'banana', 'mango', 'kiwi', 'melon']
fruits.sort()  # ['apple', 'banana', 'kiwi', 'mango', 'melon', 'orange']
'''


# 13 len(list) : Return the number of items in a container.
'''
fruits = ['apple', 'orange', 'banana', 'coconut', 'watermelon']
print(len(fruits))  # returns 5 because there are total 5 items in fruits container
'''
