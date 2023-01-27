# function = A block of reusable code
#            place () after the function name to invoke it


def happy_function(name,old):
    print(f"Happy birthday to {name}!")
    print(f"You are {old} years old!")
    print()

print()
happy_function("Jeetu",20)
happy_function("Ajay",23)
happy_function("Raman",30)


# ---------- Exercise 1 --------------


def display_invoice(username,amount,date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount} is due {date}")
    print()

display_invoice("Jeetu",22,"01/03")
display_invoice("Hemant",25,"23/03")


# return = statement used to end a function 
#          and send a result back to the caller


# ----------- Exercise 2 ----------------

def create_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    return first_name + " " + last_name

full_name = create_name("jeetu","dewangan")
print(full_name)

# ------------ Exercise 3 -----------------

def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z


print(add(5,3))
print(sub(5,3))
print(multiply(5,3))
print(divide(8,4))

