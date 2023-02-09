import time
import os

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x/3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    
    #delay the execution of current thread in seconds(here 1 second)
    time.sleep(2)

    # clears the output screen
    os.system('cls')

print("Time's Up")
