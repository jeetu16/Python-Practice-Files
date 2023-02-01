# exception =   events detected during execution that interrupt the flow of a program


try:
    first = int(input("Enter a number to divide :"))
    second = int(input("Enter a number to divide by: "))
    result = first / second
except ZeroDivisionError as e:
    print(e)
    print("You can't divide a number by Zero!")
except ValueError as vL:
    print(vL)
    print("Please enter numbers only")
except Exception as Ex:
    print(Ex)
    print("Something went wrong :(")
else:
    print(f"Result is: {result}")
finally:
    print("This will always execute")
    