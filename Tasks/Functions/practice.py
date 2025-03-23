from functools import reduce
x=[1,2,3,4,5,6]
res=reduce(lambda a,b:a+b,x)
print((res))