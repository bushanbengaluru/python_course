""" print number pattern
1
1 2
1 2 3 4
1 2 3 4 5 
"""
num = 1 #initialize num to 1
while num < 7: #less than 8 to exclude number itself
    div = 1
    while div < num:
        print(div, end=" ")
        div = div + 1
    print()
    # print() #print new line
    num = num + 1