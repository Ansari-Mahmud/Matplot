import matplotlib.pyplot as plt

labels = ['IT','Management','Medicine','Engineering']
data =[100,200,300,900]
explode = [0,0.2,0,0]

#For Donut
plt.pie(data, labels = labels, explode = explode, autopct = '%1.1f%%',
        wedgeprops = {'width':0.3}
        )

#plt.pie(data, labels = labels, explode = explode, autopct = '%1.1f%%' )
plt.show()
