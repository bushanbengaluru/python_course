"""
    *
  * * *
* * * * * """
num = 0
b=' '
bnum = 7
while num < 7:
    if num%2!=0:
        pattern = (b+("*"))*num
        print(b*bnum, pattern)
    num+=1
    bnum-=1