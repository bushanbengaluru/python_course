#Program to print incremental number in ascending order
""" print number pattern
1
1 2
1 2 3 4
1 2 3 4 5 
"""
for num in range(2,7): #less than 8 to exclude number itself
    for div in range(1,num):
        print(div, end=" ")
    print()