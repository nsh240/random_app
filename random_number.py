from __future__ import print_function
import random

range_start = int(input("Please enter the beginning of the number range: "))

range_end = int(input("Please enter the end of the number range: "))

if range_end<range_start:
    print("please enter an ending number that is greater than the starting number.")
    print(range_start,range_end)
else:
    random_num= random.randint(range_start, range_end)
    print('Your random number is:  ', random_num)



