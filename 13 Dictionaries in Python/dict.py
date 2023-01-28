# Dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates of Keys.

# ---> Dictionary Example :

'''
capitals = {'CG':'Raipur', 'UP':'Lucknow', 'Bihar':'Patna', 'MP':'Bhopal', 'Karnataka':'Bengaluru'}

# Accessing dictionary element : we can access the dictionary using key
print(capitals['CG'])

# Updating/Inserting element in dictionary
capitals['Bihar'] = 'Chapra'        # updating 'Patna' to 'Chapra'
capitals['Maharashtra'] = 'Mumbai'  # if key doesn't exist in dict then it insert at last of the dictionary
print(capitals)
'''


# ---> Dictionary Methods

# 1 dict.clear() : It removes the every key value pair from dictionary and return 'None'
'''
capitals = {'CG': 'Raipur', 'UP': 'Lucknow', 'Bihar': 'Patna',
            'MP': 'Bhopal', 'Karnataka': 'Bengaluru'}

print(capitals.clear())     # None     
print(capitals)             # {}
'''


# 2 dict.copy() : It returns a shallow copy of dictionary.
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen', 'Philippines': 'Peso'}
new_cur = currencies.copy()
print(new_cur)
'''


# 3 dict.get(key) : returns the value which is associated with the given key.
''' 
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen', 'Philippines': 'Peso'}
print(currencies.get('India'))  # 'Indian Rupees'
'''


# 4 dict.keys() : returns the all the keys of dictonary.
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen', 'Philippines': 'Peso'}
for key in currencies.keys():
    print(f"'{key}'",end=" ")   # 'USA' 'India' 'UK' 'Japan' 'Philippines'
'''


# 5 dict.values() : returns the all the values of dictonary which is associated with keys
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen', 'Philippines': 'Peso'}
for value in currencies.values():
    print(f"'{value}'",end=" ")    # 'Dollar' 'Indian Rupees' 'Pound' 'Yen' 'Peso'
'''


# 6 dict.items() : It returns key and value of dictionary. We can iterate key and value from items() method using for loop.
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen', 'Philippines': 'Peso'}

for key,value in currencies.items():
    print(f"{key}:{value}")

# USA: Dollar
# India: Indian Rupees
# UK: Pound
# Japan: Yen
# Philippines: Peso
'''


# 7. dict.update({key:value}) : if given key is not present in dict then it insert the given key:value pair at the last of the dict. If given key is present then it replaces the that key's value with the given value.
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Euro', 'Japan': 'Yen'}

currencies.update({'Philippines': 'Peso'}) # this key value pair inserted at the last of dictionary
currencies.update({'UK':'Pound'})   # key 'UK' value 'Euro' replaces by value 'Pound'

print(currencies)
'''


# 8 dict.pop(key) : remove spacified key from dictionary and return value associated with spacified key. If key is not present in the dictionary it gives keyError 
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen'}

print(currencies.pop('UK'))     # 'Pound'
print(currencies.pop('China'))  # KeyError: 'China'
'''


# 9 dict.popitem() : Remove and returns the last pair of key and value from the dictionary as a tuple of two elements. If dictionary is empty then raises the KeyError.
'''
currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
              'UK': 'Pound', 'Japan': 'Yen'}
print(currencies.popitem())     # ('Japan','Yen')
'''



# 10 dict.setdefault() : This method insert the key value pair in last of the dictionary. If key is already present in the dictionary then it doesn't insert the given key value in dictionary and returns the already present value of given key. 

# currencies = {'USA': 'Dollar', 'India': 'Indian Rupees',
#               'UK': 'Pound', 'Japan': 'Yen'}
# print(currencies.setdefault('China', 'Chinese Yuan'))
# print(currencies.setdefault('India','Rupees'))
# print(currencies)



# dictionary comprehension

states = ['CG','MP','MH','PB']
capitals = ['Raipur','Bhopal',"Mumbai",'Chandigarh']

combo_dictionary = {st:cp for st,cp in zip(states,capitals)}
print(combo_dictionary)