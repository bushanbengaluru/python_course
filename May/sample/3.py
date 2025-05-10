import matplotlib.pyplot as p
x = [1, 2, 3, 3, 2]
y = [7, 2, 4, 8, 5]
colors = [0, 10, 20, 30, 40]
# colors = ['red', 'blue', 'green', 'yellow', 'purple']
p.scatter(x, y, c=colors, alpha=0.5, cmap='viridis')
p.colorbar()  # Show color scale
p.show()
