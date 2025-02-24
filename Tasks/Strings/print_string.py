s='a2b3c2'
out=''
for i in range(0, len(s)):
    if s[i].isdigit()==True:
        out=out+s[i-1]*int(s[i])
print(out)