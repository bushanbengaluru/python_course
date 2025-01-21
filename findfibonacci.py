# program to find fibonacci number
x = int(input("Enter a number: "))
a = 0
b = 1
y = 1
xlist = []
while y <= x:
    c=a+b
    xlist.append(c)
    a=b
    b=c
    y+=1
if x in xlist:
    print(x, "is a Fibonacci number")
else:
    print(x, "is not a Fibonacci number")