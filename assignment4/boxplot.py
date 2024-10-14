import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
np.random.seed(0)
data = np.random.randn(100)

# Create the boxplot
plt.boxplot(data, vert=True, patch_artist=True, labels=['Sample Data'], showmeans=True,
            notch=True, sym='*', whis=2.0, boxprops= dict(color='r'),capprops= dict(color='g'),whiskerprops=dict(color='y'))
plt.title('Boxplot Example')
plt.show()


