import matplotlib.pyplot as plt

times = [ 8, 14 ,2]
timelabels = ['sleep','study','play']
plt.pie(times , labels = timelabels , autopct='%.2f')
plt.show()