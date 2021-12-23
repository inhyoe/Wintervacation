import matplotlib.pyplot as plt
월 = [7,8,9,10,11,12]
신규_사용자 = [456,492,578,599,670,854]

plt.plot(월,신규_사용자)
plt.title('Daehan company speeda net new customer')
plt.xlabel('Month')
plt.ylabel('User')


plt.subplot(1,4,1)
plt.bar(월,신규_사용자)
plt.subplot(1,4,2)
plt.plot(월,신규_사용자)
plt.subplot(1,4,3)
plt.scatter(월,신규_사용자,marker= '^')
plt.subplot(1,4,4)
plt.barh(월,신규_사용자)
plt.show() 