#Program to print number in right increment fashion
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
        i+=1
    print()
