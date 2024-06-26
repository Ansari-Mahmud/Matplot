import matplotlib.pyplot as plt

sales = [534, 689, 258, 401, 724, 689, 350]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

plt.plot(days, sales, label = 'My Project', marker ='o', color = 'g', markerfacecolor = 'r',linestyle='dashed', linewidth = 5)
plt.xlabel('Days of the Week')
plt.ylabel('Sales')
#plt.legend(loc = 'upper right')
plt.legend(loc = 'lower right')

plt.title('Sales Over the Week')
plt.grid(True)
plt.show()
