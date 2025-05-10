#Pie graph
import matplotlib.pyplot as p
import numpy as np
import random
x = [0,2,3,4,5,2]
mylabels = ['HP', 'Dell', 'Lenovo', 'Bata', 'Paragon', 'google']
mycolors = ['red', 'blue', 'green', 'hotpink', 'purple', 'orange']
c=[0.0,0.2,0.0,0.0,0.0,0.0] #Explode
p.pie(x,labels=mylabels,colors=mycolors, explode=c) #histogram
p.legend(title="Product name")
p.show()



