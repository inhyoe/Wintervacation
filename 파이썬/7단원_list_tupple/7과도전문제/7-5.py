Tupple1 = ('A','B','C')
Tupple2 = ('1','2')
print(len(Tupple1))
A = []

for i in range(len(Tupple1)):
    for k in range(len(Tupple2)):
        A.append(Tupple1[i] + Tupple2[k])
        
print(A)
# 출력형식이 리스트 형식이므로 리스트를 생성하여 추가한다.
print('--------------------------------')


A = []
Tupple1 = ('A','B','C')
Tupple2 = (1,2)

for i in range(len(Tupple1)):
    for k in range(len(Tupple2)):
        A.append(Tupple1[i]+str(Tupple2[k]))
print(A)
# 정수형을 str형으로 형변환하여 리스트에 넣어 출력한다.