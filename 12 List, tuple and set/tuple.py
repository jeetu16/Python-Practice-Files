# collection = single "variable" used to store multiple values
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# tuple indexing 
'''
fruits = ('apple', 'orange', 'banana', 'coconut')
print(fruits[2])        # 'banana'
print(fruits[1:])       # ('orange', 'banana', 'coconut')
print(fruits[0::2])     # ('apple', 'banana')
print(fruits[-1])       # 'coconut'
print(fruits[::-1])     # ('coconut', 'banana', 'orange', 'apple')
'''

# ---> tuple() methods:

# 1 tuple.count(value) : Return number of occurrences of value.
'''
fruits = ('apple', 'orange', 'banana', 'coconut','apple')
print(fruits.count('apple'))   # 2 ('apple' present two times in fruits container)
print(fruits.count('Kiwi'))    # 0 ('Kiwi' doesn't present in fruits container)
'''

# 2 tuple.index(value) : Return first index of value. Raises ValueError if the value is not present.
'''
fruits = ('apple', 'orange', 'banana', 'coconut')
print(fruits.index('coconut'))  # 3
print(fruits.index("kiwi"))     # ValueError: tuple.index(x): x not in tuple
'''