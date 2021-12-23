import matplotlib.pyplot as plt

years = [1960, 1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505.0,11865.0,22105.0]

plt.plot(gdp,years,color = 'green' , marker = 'o' , linestyle='solid')


plt.title('Gdp per caplita')

plt.ylabel('dollars')


plt.show()