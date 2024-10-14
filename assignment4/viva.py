
# class rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         a = self.length * self.width
#         print("area of rectangle is",a)
        
#     def perimeter(self):
#         b = 2 * (self.length + self.width)
#         print("perimeter of rectangle is",b)
        
# rect = rectangle(3,4)
# rect.area()
# rect.perimeter()
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(x, y1, label="sin(x)", color="blue", linestyle="--", marker="o", markersize=6, linewidth=2)
plt.plot(x, y2, label="cos(x)", color="green", linestyle="-.", marker="s", markersize=6, linewidth=2)

# Customizations
plt.title("Sine and Cosine Waves", fontsize=16, fontweight='bold')
plt.xlabel("x-axis", fontsize=12, color='purple')
plt.ylabel("y-axis", fontsize=12, color='purple')
plt.legend(loc="upper right", fontsize=10, title="Legend")  # Position and title for legend
plt.grid(True, which='both', linestyle=':', linewidth=0.5)  # Add a dotted grid
plt.xlim(0, 10)  # Set x-axis limits
plt.ylim(-1.5, 1.5)  # Set y-axis limits

# Highlight a specific point
plt.scatter([np.pi/2], [1], color='red', zorder=5)
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(1.5, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
