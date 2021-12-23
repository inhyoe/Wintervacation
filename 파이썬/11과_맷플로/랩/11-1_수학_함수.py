import matplotlib.pyplot as plt

x = [x for x in range(-20, 20)]
y = [t**2 for t in x]

plt.plot(x,y,marker='o')


plt.axis([-20,20, 0, 400])


plt.show()

# 난수를 가지는 그래프를 그리기.
# 난수를 가지려면 x축은 1~ 1000까지 일정하게 가야한다
# y축은 난수가 생성된 값이다
# 그렇다면

