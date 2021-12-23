fruit = []
for i in range(3):
    name= input('당신이 좋아하는 과일 이름을 입력하세요.')
    fruit.append(name)

name = input('당신이 좋아하는 과일의 이름을 입력하세요.')
print(type(name))
print (name)
print(fruit)
print(type(fruit))
if name in fruit:
    print('당신이 좋아하는 과일입니디')
else:
    print('좋아하는 과일이 아닙니다.')

# 오답노트
# fruit.append를 붙이지 않았음.
# in 을 사용할 때는 (타입형) in 리스트형 으로 해야함.
