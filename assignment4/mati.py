from matplotlib import pyplot as plt
x = [3,5,7,3,7,3]
y = [2,7,2,5,5,2]

# plt.title("Plot")
# plt.xlabel("inches")
# plt.ylabel("metres")
# plt.plot(x,y)
# plt.figure(figsize=(10,10))
# plt.show()

plt.subplot(3,3,1)
plt.plot([2,4],[2,4])
plt.title("1st")

plt.subplot(3,3,2)
plt.plot([2,4,2,4],[2,4,4,2])
plt.title("2nd")

plt.subplot(3,3,3)
plt.plot([2,4],[4,2])
plt.title("3rd")

plt.subplot(3,3,4)
plt.plot([4,2,2,4],[4,2,4,2])
plt.title("4th")

plt.subplot(3,3,5)
plt.plot([2,4,3,2,4],[4,2,3,2,4])
plt.title("5th")

plt.subplot(3,3,6)
plt.plot([2,4,4,2],[4,2,4,2])
plt.title("6th")

plt.subplot(3,3,7)
plt.plot([4,2],[2,4])
plt.title("7th")

plt.subplot(3,3,8)
plt.plot([2,4,2,4],[4,2,2,4])
plt.title("8th")

plt.subplot(3,3,9)
plt.plot([2,4],[2,4])
plt.title("9th")

plt.show()