import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=[8, 5], facecolor='lightpink', layout='constrained', edgecolor='black', dpi=100)

fig.suptitle('Figure')
ax = fig.add_subplot(111)
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
ax.plot([1,2,3],[4,5,6])
plt.show()

fig, axs = plt.subplots(2,2,figsize=(7,4), facecolor='lightgreen')
fig.suptitle('2x2 example')
axs[0,0].plot([1,2,3],[4,5,6])
axs[0,1].plot([4,2,3],[4,5,6])
axs[1,0].plot([4,2,3],[4,5,6])
axs[1,1].plot([4,2,3],[4,5,6])
plt.tight_layout()
plt.show()

# fig = plt.figure(figsize=[8, 5], facecolor='lightblue', layout='constrained', edgecolor='black', dpi=100)
# fig.suptitle('Figure')
# ax=plt.axes([0.1,0.1,0.8,0.8])

# ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
# plt.plot([1,2,3,4],[5,8,4,6])
# plt.show()

