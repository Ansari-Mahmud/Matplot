import matplotlib.pyplot as plt

Counter_Sales = [534, 689, 258, 401, 724, 689, 350]
Online_Sales= [854, 499, 678, 561, 854, 799, 460]
Referal_Sales= [224, 329, 548, 561, 524, 289, 4460]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

plt.plot(days, Counter_Sales, label = 'Counter Sales Data', marker ='o', markerfacecolor = 'b')
plt.plot(days, Online_Sales, label = 'Online Sales Data', marker ='o', markerfacecolor = 'orange')
plt.plot(days, Referal_Sales, label = 'Influencers Sales Data', marker ='o',markerfacecolor = 'g')
plt.xlabel('Days of the Week')
plt.ylabel('Sales')
plt.xlim(0,7)
plt.ylim(100,900)
#plt.legend(loc = 'upper right')
plt.legend(loc = 'lower right')

plt.title('Sales Over the Week')
plt.grid(True)
plt.show()
