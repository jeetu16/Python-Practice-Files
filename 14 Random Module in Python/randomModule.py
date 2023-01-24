import random

# random methods: 

# 1 random.random() : it gives random floating point number between 0 to 1. 
'''
num = random.random() 
print(num)             # random number(0 to 1) : 0.27936367103139514
'''


# 2 random.randint(start, end): it gives any random number between given start to end point.
'''
start = 1
end = 10
num = random.randint(start,end)
print(num)          # random number (1 to 10) : 3
'''


# 3 random.choice(iterative) : it returns any random element from the iterative variable
'''
technology = ["JavaScript","Python","C++","Java","Golang"]
name = 'jeetu'
ch = random.choice(technology)
ch2 = random.choice(name)

print(ch2)
print(ch)
'''

# 4 random.shuffle(iterative) : It shuffles the iterative vaiable element(Means changes the position).

technology = ["JavaScript", "Python", "C++", "Java", "Golang"]
name = 'jeetu'
random.shuffle(technology)  # after shuffle ['C++', 'Golang', 'Python', 'Java', 'JavaScript']
random.shuffle(name)        # TypeError: 'str' object does not support item assignment

print(technology)

