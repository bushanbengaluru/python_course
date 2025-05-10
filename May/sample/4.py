#Bar graph
import matplotlib.pyplot as p
x = ['lenovo', 'HP', 'DELL']
y = [7, 2, 4]
p.bar(x, y, color=['red', 'blue', 'green'])
# p.barh(x, y, color=['red', 'blue', 'green']) # for horizontal bar graph
p.xlabel("product name")
p.ylabel("product rating")
p.title("product review rating")
p.grid(axis='y', color='#2222', linestyle='--', linewidth=0.5)
p.show()