# program to find fibonacci number
x = int(input("Enter a number to check if its in fibonnaci series: "))
a = 0
b = 1
y = 1
xlist = []
for i in range(1,x+1):
    c=a+b
    xlist.append(c)
    a=b
    b=c
if x in xlist:
    print(x, "is a Fibonacci number")
else:
    print(x, "is not a Fibonacci number")