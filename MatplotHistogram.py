import matplotlib.pyplot as plt

sales = [534, 689, 258, 401, 724, 689, 350]
bins =[100,200,300,400,500,600,700,800,900]

plt.hist(sales, bins, label = 'My Project')
plt.xlabel('Days of the Week')
plt.ylabel('Sales')
plt.legend(loc = 'upper right')
plt.title('Sales Over the Week')
plt.xticks(bins)
plt.show()
