# Email Slicer program

email = input("Enter your email: ")

name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

print(f"Your name is {name} and domain name is {domain_name}")
