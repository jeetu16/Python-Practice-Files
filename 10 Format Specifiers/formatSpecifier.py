# format specifiers = {:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimal places
'''
price1 = 345.554
price2 = -383.22387438437

print(f'Price is: ${price1:.2f}')
print(f'Price is: ${price2:.3f}')
'''


# :(number) = allocate that many spaces
'''
price1 = 345.554
price2 = -383.22387438437

print(f'Price is: ${price1:10}')
print(f'Price is: ${price2:20}')
'''


# :0(number) = allocate and zero pad that many spaces
'''
price1 = 345.554
price2 = -383.223

print(f'Price is: ${price1:015}')
print(f'Price is: ${price2:015}')
'''


# :< = left justify
'''
price1 = 345.554
price2 = -383.2238

print(f'Price is: ${price1:<15}')
print(f'Price is: ${price2:<15}')
'''


# :> = right justify
'''
price1 = 345.554
price2 = -383.2238

print(f'Price is: ${price1:>15}')
print(f'Price is: ${price2:>15}')
'''


# :^ = center align
'''
price1 = 345.554
price2 = -383.2238

print(f'Price is: ${price1:^15}')
print(f'Price is: ${price2:^15}')
'''


# :+ = use a plus sign to indicate positive value
'''
price1 = 345.554
price2 = -383.2238

print(f'Price is: ${price1:+}')
print(f'Price is: ${price2:+}')
'''


# :  = insert a space before positive numbers
'''
price1 = 345.554
price2 = -383.2238

print(f'Price is: ${price1: }')
print(f'Price is: ${price2: }')
'''


# :, = comma separator
'''
price1 = 35245.5543432
price2 = -38855583.2238

print(f'Price is: ${price1:,}')
print(f'Price is: ${price2:,}')
'''
# :+,2f = combination of specifier
price1 = 35245.554
price2 = -38855583.2238

print(f'Price is: ${price1:+,.2f}')
print(f'Price is: ${price2:+,.2f}')

