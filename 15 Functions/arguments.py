# default arguments = A defualt value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduce # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitary



# ------------ Exercise 1 ---------------
'''
def net_price(price,discount=0,tax=0):
    return price * (1 - discount) * (1 + tax)

print(net_price(500,0.1,0.1))
print(net_price(100,0.1))

# ----------------- Exercise 2 --------------------
import time
import os

def count(end,start = 0):
    for num in range(start,end+1):
        print(num,end=" ")
        time.sleep(1)
        os.system('cls')

count(1,10)         # not working
count(20)

'''

# keyword arguments = arguments prefixed with the names of parameters
#                     order of the arguments doesn’t matter
#                     helps with readability
#                     positional argument follows keyword argument


# ------------ EXAMPLE 1 ---------------

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", last="John", first="James", title="Mr.")


# ------------ EXAMPLE 2 ---------------

for number in range(1, 11):
    print(number, end=" ")                  # here end=" " is keyword argument
print("1", "2", "3", "4", "5", sep="-")     # here sep="-" is keyword argument


# ------------ EXAMPLE 3 ---------------

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(last=7890, country=1, area=123, first=456)
print(phone_num)
