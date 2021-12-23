import matplotlib.pyplot as plt

#우라니라의 연간 1인당 국민 소득을 years, gdp에 저장
years = [ 1950, 1960,1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# 선 그래프를 그린다. x축에는 years값, y축에난 gdp값이 표시된다.
plt.bar(range(len(years)),gdp)
        #

# 제목을 설정한다.

plt.title('GDP per capita') #1인당 국민 소득
# 차트의 제목 레이블 설정

#y축에 레이블을 붙인다.
plt.xticks(range(len(years)),years)
plt.show()