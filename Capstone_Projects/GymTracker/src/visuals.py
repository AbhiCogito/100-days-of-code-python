from matplotlib import pyplot as plt

x = ['Money', 'Sophie', 'Priya', 'Anne']
y = [1,2,3,4]
age = [41, 5, 36, 15]

plt.bar(x,y, width=0.6, color='cyan', edgecolor='pink', linewidth=3, alpha=0.3)
plt.bar(x,age, width=0.6, color='blue', edgecolor='pink', linewidth=3, alpha=0.3)
plt.title("My first matplotlib graph")
plt.xlabel("Name", fontsize=21, color='pink')
plt.ylabel("Order")
# plt.gca().set_facecolor('black')   # axes background
# plt.gcf().set_facecolor('black')   # figure background
plt.show()

