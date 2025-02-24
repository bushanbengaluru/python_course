"""
ord(a) - we will get ascii 
chr(65) - A
**** TASK2 - a-z = ascii value for A-Z=ascii values
"""
for i in range(65,91):
    print(f"{i} = {chr(i)}")
for i in range(97,123):
    print(f"{i} = {chr(i)}")

    s = 'a,b c'
    out = ''
    for i in s:
        a_code=ord(i):
        if a_code >= 65 and a_code <= 90:
            out=out+i(90-a_code+65)
        elif a_code >= 97 and a_code <= 122:
            out=out+i(122-a_code+97)
        else:
            out=out+i   
    print(out)