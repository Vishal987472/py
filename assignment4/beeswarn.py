import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'category':['A','A','A','B','B','B','C','C','C','D','D','D'],
    'values':[3,5,2,6,7,8,9,1,3,2,5,8]
}
df = pd.DataFrame(data)
plt.figure(figsize=(8,6))
sns.swarmplot(x='category',y='values', data=df,palette=['red','green','blue','yellow'])
plt.title('bee swarm plot')
plt.ylabel("values")
plt.xlabel("categories")
plt.show()