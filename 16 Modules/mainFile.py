# module = A file containing code you want to include in your program
#          Use 'import' to include a module (built-in or your own)
#          Useful to break up a large program into small files for reusable and 
#          readibility purpose


# ---> Different ways to include a module into your program
'''
# import math               # including math module
# import math as m          # renaming module name in your program
# from math import floor    # only floor() function is including from math module
# from math import *        # everthing is including from math module

# print(floor(9.6))
'''

# ---------------- Example of your own module ----------------------
'''
# import example
from example import palindrome

# print(primeNum(16))
print(palindrome(123))
'''