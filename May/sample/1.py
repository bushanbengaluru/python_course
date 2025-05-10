import matplotlib.pyplot as p
# print(dir(p))
x = [1, 2, 3, 4, 5]
y = [0, 2, 1, 4, 5]
p.plot(x,y,marker='o',ms=10.0, mfc='g',lw=2.5, linestyle='dotted', color='black')
# p.plot(x,marker='o',ms=10.0, mfc='g',lw=2.5, linestyle='dotted', color='black')
font1= {'family':'serif','color':'blue','weight':'normal','size':16}
font2= {'family':'serif','color':'red','weight':'normal','size':16}
font3= {'family':'serif','color':'red','weight':'bold','size':20}
p.xlabel("lenovo product rating",fontdict=font1)
p.ylabel("lenovo product review",fontdict=font2)
p.title("lenovo product review rating",font3)
p.grid(axis='y',color='#2222', linestyle='--', linewidth=0.5)
p.show()