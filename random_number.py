import random

range=[]
range_start = input("Please enter the beginning of the range: ")
range_end = input("Please enter the end of the range: ")
print(range_start,range_end)
random_num= random.randint(range_start, range_end)
print(random_num)
