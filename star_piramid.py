"""
    *
  * * *
* * * * * """
num = 0
b=' '
bnum = 9
while num < 9:
    if num%2!=0:
        pattern = (b+("*"))*num
        print(b*bnum, pattern)
    num+=1
    bnum-=1