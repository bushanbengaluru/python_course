#program to print star in decending left triangle
c= 5
b = ' '
c=int(input("Enter number of stars: "))
for a in range(1, c+1):
    print (' '*(c-a)+'*'*(a))