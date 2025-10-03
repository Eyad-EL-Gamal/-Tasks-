import matplotlib.pyplot as plt 
x = ["saturday", "sunday", "monday", "tuesday", "wednesday",
     "thursdy", "friday"]
y = [26,32,25,30,31,34,20]
plt.plot(x,y, marker = 'o', linestyle = '-', color ='red')
plt.title('The temperature throughout the week')
plt.xlabel('Days of the week')
plt.ylabel('Temperature {°C}')
plt.xticks(rotation = 45)
plt.show()