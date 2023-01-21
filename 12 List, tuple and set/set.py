# collection = single "variable" used to store multiple values
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates


# ---> set indexing (doesn't use)
'''
# we can't access the set elements by index because of it is not follow any sequence or indexing

fruits = {'apple', 'orange', 'banana', 'coconut', 'watermelon'}
print(fruits[0])    # TypeError: 'set' object is not subscriptable
'''


# we can interate the set elements by for loop
'''
fruits = {'apple', 'orange', 'banana', 'coconut', 'watermelon'}
for fruit in fruits:
    print(fruit)
'''

# ---> set{} methods :

# 1 set.add(element) :  Add an element to a set.
'''
# set doesn't store duplicate value in container

fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits.add('kiwi')  # {'coconut', 'orange', 'kiwi', 'apple', 'banana'}
fruits.add('apple')  # {'kiwi', 'orange', 'apple', 'banana', 'coconut'}
print(fruits)
'''


# 2 set.clear() : Remove all elements from this set.
'''
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits.clear()      # returns empty set -> set()
print(fruits)
'''


# 3 set.copy() : Return a shallow copy of a set.
'''
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits_copy = fruits.copy()  # {'orange', 'banana', 'coconut', 'apple'}
print(fruits_copy)
'''


# 4 set.discard(...) : Remove an element from a set if it is a member. If the element is not a member, do nothing.
'''
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits.discard('kiwi')      # doing nothing becuase kiwi not present in fruits set
fruits.discard('apple')     # removing 'apple' from the 'fruits' set
print(fruits)
'''


# 5 set.pop() : Remove and return an arbitrary(random) set element. Raises KeyError if the set is empty.
'''
fruits = {'apple', 'orange', 'banana', 'coconut'}
print(fruits.pop()) # removing any random element from fruits set
'''


# 6 set.remove() : Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
'''
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits.remove('apple')      # after removing 'apple' set is -> {'coconut', 'orange', 'banana'}
fruits.remove('Kiwi')       # KeyError: 'Kiwi'
print(fruits)
'''


# 7 len(set) : returns total number of element in a set

fruits = {'apple', 'orange', 'banana', 'coconut'}
print(len(fruits))  # 4