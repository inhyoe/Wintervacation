import matplotlib.pyplot as plt
닥스훈트_길이 = [77,78,85,83,73,77,73,80]
닥스훈트_높이 = [25,28,29,30,21,22,17,35]

사모예드_길이 = [75,77,86,86,79,83,83,88]
사모예드_높이 = [56,57,50,53,60,53,49,61]

말티즈_길이 = [35,38,38,41,30,37,41,35]
말티즈_높이 = [22,25,19,30,21,24,28,18]


plt.scatter(닥스훈트_길이,닥스훈트_높이,color ='r',marker = 'o',label ='Dachshund')



plt.scatter(사모예드_길이,사모예드_높이,color = 'b',marker= '^', label = 'Samoyed')



plt.scatter(말티즈_길이,말티즈_높이,color = 'g',marker = 's',label = 'Maltese')

plt.title('Dog size')
plt.legend() # 범례 표시한다.
plt.show()
