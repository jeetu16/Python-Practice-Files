# ---> String
'''
# string = In Python, strings can be created by enclosing the character or the sequence of characters in the quotes. Python allows us to use single quotes, double quotes and triple quote to define a string.
# 'str' object does not support item assignment

# name = """Jeetu"""
# print(name)
'''

# ---> String Indexing
'''
# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])
'''

# ---> EXERCISE 1

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# ---> EXERCISE 2

credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)