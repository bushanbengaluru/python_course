import matplotlib.pyplot as p
font1= {'family':'serif','color':'blue','weight':'normal','size':16}
font2= {'family':'serif','color':'red','weight':'normal','size':16}
font3= {'family':'serif','color':'red','weight':'bold','size':20}

p.title("HP product review rating")
p.xlabel("HP product rating")
p.ylabel("HP product review")
x = [1, 2, 3]
y = [7, 2, 4, 8, 5]
p.plot(x,y,marker='o',ms=10.0, mfc='g',lw=2.5, linestyle='dotted', color='black')
p.subplot(1, 2, 1)



p.title("DELL product review rating")
p.xlabel("DELL product rating")
p.ylabel("DELL product review")
x = [1, 2, 3, 3, 2]
y = [7, 2, 4, 8, 5]
p.plot(x,y,marker='o',ms=10.0, mfc='g',lw=2.5, linestyle='dotted', color='black')
p.subplot(1, 2, 2)

