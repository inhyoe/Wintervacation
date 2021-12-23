import matplotlib.pyplot as plt

""" years = [1960, 1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505.0,11865.0,22105.0]

plt.plot(gdp,years,color = 'green' , marker = 'o' , linestyle='solid')


plt.title('Gdp per caplita')

plt.ylabel('dollars')


plt.show() """


x = [ x for x in range(-10,10)]
y = [ 2*t for t in x]

plt.plot(  x,  y,color = 'blue' ,marker = 'o')
plt.title('Math')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-20,20,-20,20])
plt.show()