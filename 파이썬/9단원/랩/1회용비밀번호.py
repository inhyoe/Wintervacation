import random

password = int(input('몇자리의 비밀번호를 원하시나요?'))
for i in range(password):
    print(random.randint(0,password), end='')