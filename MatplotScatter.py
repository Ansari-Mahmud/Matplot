import matplotlib.pyplot as plt

Counter_Sales = [534, 689, 258, 401, 724, 689, 350]

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

plt.scatter(days, Counter_Sales, label = 'Counter Sales Data')
plt.xlabel('Days of the Week')
plt.ylabel('Sales')

plt.title('Sales Over the Week')
plt.grid(True)
plt.show()
