#**02012025 Task 2:#union     
a=[1,2,3,4,5]     
b=[3,4,5,6,7]     
# #intersection     
# #union
c = []
for i in a:
    c.append(i)
for j in b:
    if j not in c:
        c.append(j)
print(c)