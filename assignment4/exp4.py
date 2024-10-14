import numpy as np

# # Create a sample array
# arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# # Original array
# print("Original Array:\n",arr,"\n")

# # Swap columns 1 and 2 using direct assignment
# temp = arr[:, 1].copy()
# arr[:, 1] = arr[:, 2]
# arr[:, 2] = temp

# # array with column swaped
# print("Swaped Array :\n",arr)



import pandas as pd

# Assume your dataset is in a file called "color_srgb.csv" with the following format:
#Name,HEX,RGB
# White,#FFFFFF,"rgb(100,100,100)"
# Silver,#C0C0C0,"rgb(75,75,75)"
# Gray,#808080,"rgb(50,50,50)"
# Black,#000000,"rgb(0,0,0)"
# Red,#FF0000,"rgb(100,0,0)"
# Maroon,#800000,"rgb(50,0,0)"
# Yellow,#FFFF00,"rgb(100,100,0)"
# Olive,#808000,"rgb(50,50,0)"
# Lime,#00FF00,"rgb(0,100,0)"

# Use read_csv to import the dataset
data = pd.read_csv('color_srgb.csv')

# Print the imported data
print("Imported data:")
print(data)

# Check the data types of each column
print("Data types:")
print(data.dtypes)