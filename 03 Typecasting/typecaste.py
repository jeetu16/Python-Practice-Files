# typecasting = The process of converting a value of one data type to another (string,integer,float,boolean)

# Explicit Vs Implicit

'''
name = "Jeetu"
age = 25
gpa = 7.2
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# ---> int to float conversion
age = float(age)
print(age,type(age))

# ---> float to int conversion
gpa = int(gpa)
print(gpa,type(gpa))

# ---> string to bool conversion
name = bool(name);
print(name,type(name))

# ---> boolean to string conversion
student = str(student)
print(student,type(student))

'''

# ---> int,float to boolean
'''
num = 0.0
num2 = -10   # except zero(0 or 0.0) in boolean everthing is true value considering only int and float here
num = bool(num) 
num2 = bool(num2)
print(num, type(num))
print(num2, type(num2))
'''

# ---> string to boolean
'''
name = "Jeetu"
name2 = ""
name = bool(name)
name2 = bool(name2) # except empty string ("",'') in boolean everything is True value considering only String here
print(name,type(name))
print(name2,type(name2))
'''

# ---> int,float to string
'''
number = 250
float_num = 20.3
number = str(number)
float_num = str(float_num)
print(number,type(number))
print(float_num,type(float_num))
'''

# ---> string to int,float
'''
# we can only convert integer string into integer and float string into floating point number. We cannot convert a character or special characters string into int or float

name = "Jeetu16"
int_str = "230"
float_str = '250.4'

name = int(name)
int_str = int(int_str)
float_str = float(float_str)

print(name,type(name))
print(int_str,type(int_str))
print(float_str,type(float_str))
'''

# Falsy values in python are: 0, False, None, an empty string('',""), an empty list (e.g,[]), an empty tuple (e.g,()) and an emptye dictionary (e.g, {}).

# The Truthy values are other values that aren't Falsy