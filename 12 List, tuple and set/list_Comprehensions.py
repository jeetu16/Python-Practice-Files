# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# Here i created natural numbers list using list comprehension
# naturalNumber = [ i for i in range(1,11)]
# print(naturalNumber)


# here we use list comprehension to find all the numbers which is greater number 
# nums = [2, 4, 5, 6, 7, 8, 9, 12, 18, 23, 98]
# greater_nums = [ i for i in nums if i > 9]
# print(greater_nums)

# find the table of all number between 15 to 20
# table = [[i*j for j in range(1,11)] for i in range(15, 21)]
# for tb in table:
#     print(tb)


# get the all the list methods using list comprehension
# list_methods = [i for i in dir(list) if "__" not in i]
# print(list_methods)

# getting square of numbers using list comprehension
# squares = [(i,i**2) for i in range(1,11)] 
# print(squares)

# here we are taking power of all the numbers which is not divisible by 2 if number divisible by 2 then we take the number it self
# power_num = [num*num if not num%2==0 else num for num in range(1,20)]
# print(power_num)


# get the all numbers which is divisible by 3 and 9 both
# get_num = [num for num in range(1,100) if num%3==0 and num%9==0]
# print(get_num)


# changing 2d list into a list using list comprehension
# lst = [[1,2,3],[4,5],[6,7,8,9],[10,11,12,13]]
# flatten = []
# flatten_list = [[flatten.append(i) for i in num] for num in lst]  # method 1
# flatten = [ele for nums in lst for ele in nums]                   # method 2
# print(flatten)


# all posible combination of two characters of given list
# character = ['a','b','c','d']
# pairs = [[x,y] for x in character for y in character if x!=y]
# print(pairs)


# getting those word which len is 4 or less than 4
#paragraph = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
# words = [wd for wd in paragraph.split() if len(wd)<=4 ]
# print(words)


# prime number using list comprehension
# prime = [i for i in range(2,51) if all(i%num!=0 for num in range(2,i))]
# print(prime)

# creating passwords using list comprehensive

import random,string

str_chars = string.printable

passwords = [''.join(random.choice(str_chars) for x in range(8,20)) for i in range(5)]
print(passwords)

# print(str_chars)