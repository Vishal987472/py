import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,4.5,8,1,8,1])
y = np.array([1,8,1,6,6,1])

plt.plot(x,y,marker="o",c="red",ms=10)
plt.grid()
plt.show()


# plt.bar([1],[2],label="red",width=0.5,color='r')
# plt.bar([2],[6],label="green",width=0.5,color='g')
# plt.bar([3],[3],label="orange",width=0.5,color='orange')
# plt.bar([4],[5],label="pink",width=0.5,color='m')
# plt.bar([5],[1],label="yellow",width=0.5,color='y')
# plt.bar([6],[3],label="blue",width=0.5,color='b')
# plt.legend()
# plt.ylabel('Children')
# plt.xlabel('Favourite color')
# plt.title("Children's favourite color")
# plt.show()

# slices=[30,20,25,15,10]
# act=['Scifi','comedy','Action','Romance','Drama']
# cols=['c','m','r','b','g']
# plt.pie(slices,labels=act,colors=cols,startangle=90,shadow=
# False,explode=(0.1,0,0,0,0),autopct='%1.2f%%')
# plt.legend()
# plt.title('Favorite Type of Movie')
# plt.show()

# x = np.linspace(-20, 20, 100)
# y = x**2
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Plot of y = x^2')
# plt.grid(True)
# plt.show()

# # Data for the bar graph
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [10, 40, 30, 20, 50]

# # Create the figure and axis
# fig, ax = plt.subplots()

# # Create the bar graph
# ax.bar(categories, values)

# # Set the title and labels
# ax.set_title('Simple Bar Graph')
# ax.set_xlabel('Categories')
# ax.set_ylabel('Values')

# # Show the graph
# plt.show()