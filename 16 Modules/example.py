
def primeNum(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    original_num = num
    sum = 0
    while num > 0:
        rem = num % 10
        sum  = 10 * sum + rem
        num = num // 10
    if sum == original_num:
        return True
    else:
        return False