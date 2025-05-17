# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# res=a//b
# print(res)
# #Example of exception handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    res=a//b
    print(res)
except Exception:
    print("Exception occurred")
    print("Please enter a valid number")
finally:
    print("This is finally block")
#=========
#  #Example of exception handling
#User defined exceptions:
#    user can raise the exception
try:
    p = int(input("Enter principle: "))
    q = int(input("Enter tenure: "))
    r = int(input("Enter rate: "))
    if p<0 or q<0 or r<0:
        raise ValueError("Principle should be positive")
    out = r*p*q/100
    print(out)
except ValueError as e:
    print("Exception occurred")
    print(e)
