#Program to print star in christmas tree fashion
"""
          * 
         * * 
        * * * 
       * * * * 
      * * * * * 
     * * * * * * 
    * * * * * * * 
   * * * * * * * * 
  * * * * * * * * * 
 * * * * * * * * * * 
          *
"""
b = ' '
bnum = int(input("Enter number to print piramid: "))
for num in range(1, bnum+1):
  if num%2!=0:
    pattern = ((" "))*bnum
    print((pattern)+ (("*"+b)*(num)))
  else:
    pattern = ((" "))*bnum
    print((pattern)+ (("*"+b)*(num)))
  bnum-=1
print(b*(num)+"*")