import matplotlib.pyplot as plt

Counter_Sales = [534, 689, 258, 401, 724, 689, 350]
Online_Sales = [694, 899, 548, 201, 714, 699, 390]

days = range(1,8)

plt.bar([a-0.25 for a in days], Counter_Sales, label = 'Counter Sales Data', width = 0.25, align = 'edge')
plt.bar([a+0.25 for a in days], Online_Sales, label = 'Online Sales Data', width = -0.25, align = 'edge')
plt.xlabel('Days of the Week')
plt.ylabel('Sales')
#plt.xticks(days)
plt.title('Sales Over the Week')
plt.grid(True)
plt.show()
