'''
Test Credit Card Account Numbers
American Express 378282246310005
American Express 371449635398431
American Express Corporate 378734493671000
Australian Bankcard 5610591081018250
Diners Club 30569309025904
Diners Club 38520000023237
Discover 6011111111111117
Discover 6011000990139424
JCB 3530111333300000
JCB 3566002020360505
MasterCard 5555555555554444
MasterCard 5105105105105100
Visa 4111111111111111
Visa 4012888888881881
'''

# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

credit_card = input("Enter your credit card number")

# ---> step 1 

if credit_card.find("-") or credit_card.find(" "):
    credit_card = credit_card.replace(' ',"")
    credit_card = credit_card.replace('-',"")

# ---> step 2

odd_sum = 0
for i in range(len(credit_card)-1,-1,-2):
    odd_sum = odd_sum + int(credit_card[i])

# ---> step 3

even_sum = 0
for i in range(len(credit_card)-2,-1,-2):
    double_index = int(credit_card[i]) * 2

    if double_index > 9:
        double_index = (double_index % 10) + 1
    
    even_sum = even_sum + double_index

# ---> step 4

total_sum = even_sum + odd_sum

# ---> step 5

if total_sum % 10 == 0:
    print("valid")
else:
    print("not valid")

