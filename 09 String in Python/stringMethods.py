# ---> String Methods 

# 1. len(str) : return number of characters in string
'''
name = "Jeetu "
name2 = ''
print("Number of characters on your first name are: ",len(name))
print("Number of characters on last name are: ",len(name2))
'''


# 2. str.find(subStr or a char) : returns index number of found character
'''
name = 'jeetu' # if character not found returns -1
print(name.find('ee'))
print(name.rfind('e')) # returns last occurance of character index number
print(name.find('J'))
'''


# 3. str.index(subStr or a char) : finds the first occurrence of the specified value, raises an exception if the value is not found.
'''
name = 'jeetu'
print(name.index('t'))
print(name.index('d'))
'''


# 4. string.capitalize() : returns a string where the first character is upper case, and the rest is lower case.
'''
name = "jeetu dewangan"
name2 = "DAVID"
print(name.capitalize())
print(name2.capitalize())
'''


# 5. str.upper() : returns a string where all characters are in upper case.
'''
name = "jeetu"
print(name.upper())
'''


# 6. str.lower() : returns a string where all characters are lower case.
'''
name = "JEETU"
print(name.lower())
'''

# 7. str.isdigit() : returns True if all the characters are digits, otherwise False
'''
name = "jeetu";
name2 = "ABC123@"
name3 = "12345"
print(name.isdigit())
print(name2.isdigit())
print(name3.isdigit())
'''


# 8. str.isalpha() : returns True if all the characters are alphabet letters (a-z) or (A-Z)
'''
name = "jeetu"
name2 = "jeetu@gmail.com"
print(name.isalpha())
print(name2.isalpha())
'''


# 9. str.isalnum() : returns True if all the characters are alphanumeric, meaning alphabet letter (a-z)(A-Z) and numbers (0-9).
'''
email = "abc@1234"
email2 = "abc1234"
print(email.isalnum())
print(email2.isalnum())
'''


# 10. str.count() : returns the number of times a specified value appears in the string
'''
name = "jeetu jeetu"
print(name.count('ee'))
print(name.count('EE'))
'''


# 11. str.replace(oldValue,newValue,count(optional)) : replaces a specified phrase with another specified phrase and returns
'''
name = "jeetu"
print(name.replace('e','i'))
print(name.replace('e','i',1)) 
'''


# 12. str.strip() : method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters and returns
'''
name = "    jeetu     "
print("Without removing white spaces "+ name + " End")
print("After removing white spaces "+name.strip()+" End")
'''


# 13. str.isspace() : returns True if all the characters in a string are whitespaces, otherwise False
'''
name = '    '
name2 =  "Jeetu Dewangan"
print(name.isspace())
print(name2.isspace())
'''


# 14. str.isupper() : returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
'''
name = "jeetu";
name2 = 'JEETU'
name3 = "jeetu123"
name4 = "JEETU123"
print(name.isupper())
print(name2.isupper())
print(name3.isupper())
print(name4.isupper())
'''

# 15. str.islower() : returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
'''
name = 'jeetu'
name2 = "JEETU"
print(name.islower())
print(name2.islower())
'''


