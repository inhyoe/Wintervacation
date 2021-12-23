a = ','.join(['apple','carrot','bannana'])
print(a) #구분자는 ,
b = '-'.join('010.1234.5678'.split('.'))
print(b) # 구분자는 -
c = '010.1234.5678'.replace('.','-')
print(c) 
# '(구분자)'.join(a,b,c)

d = '010.1234.5678'.split('.')
print(d)

s = 'hello world'
slist= list(s)
print(slist) # 문자열을 하나하나 자르기.
hap = ''.join(slist) # 구분자 x
print(hap)