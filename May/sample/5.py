#Normal data distribution
#numpy is used for analysis of data
import matplotlib.pyplot as p
import numpy as np
import random
x = np.random.normal([0.0,5.0,250])
p.hist(x) #histogram
p.show()
print(x)

