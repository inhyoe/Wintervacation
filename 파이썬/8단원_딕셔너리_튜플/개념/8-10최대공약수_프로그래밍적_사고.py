num = 10
divisors = []
for i in range(2,num):
    if num%i == 0:
        divisors.append(i)
        
print(num,'의 진 약수 :',divisors)

divisors = []
def get_divisiors(num):
    
    for i in range(2,num): 
        if num% i == 0:
            divisors.append(i)
    return divisors

x = 48
print(x,'의 진약수 :',get_divisiors(x))
y = 60
print(y,'의 진약수 :',get_divisiors(y))


num = 10
divisors = []
for i in range(2,num):
    if num%i == 0:
        divisors.append(i)
        
print(num,'의 진 약수 :',divisors)


def get_divisiors(num):
    divisors = set() # 중복을 제거
    for i in range(2,num): 
        if num% i == 0:
            divisors.add(i)
    return divisors

x = 48
print(x,'의 진약수 :',get_divisiors(x))
y = 60
print(y,'의 진약수 :',get_divisiors(y))

print(get_divisiors(x)&get_divisiors(y))
print('최대 공약수' , max(get_divisiors(x)&get_divisiors(y)))