#일반 함수
def add(x,y):
    return x+y

#람다 함수 -이름이 없는 함수이고 재사용이 불가능하다.
lambda x,y : x+y

print('100+200 = ' , (lambda x,y : x+y)(100,200))

# 인자값에는 변수도 올 수 있다
t = [100,200,300]
print((lambda x : x[0])(t))