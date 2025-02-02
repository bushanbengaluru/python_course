#find Arm strong number for given number
#123 -- 3
#1**3+2**3+3**3 == 123 amstrong
b=0
num = int(input("Enter a number to check: "))
c=1
tens = num//10
while tens !=0:
   b = tens//10
   c-=1
print (b)
"""
1 find digit based on given number
2 count  = 0
cnt=0
bkp=a
while a>0:
   a=a//10
   cnt=cnt+1
s=0
while a>0:
   t=a%10
   s=s+t**cnt
   a=a//10
if s==bkp:
   print('armstr')
"""

# hun = num//100
# thousand = num//1000
# print(tens)
# print(hun)
# print(thousand)
