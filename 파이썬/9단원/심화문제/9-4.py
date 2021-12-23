a = 'ABCD'
b = '1234'
 #  -4321
print('a' ,'=',a)
print('b' ,'=',b)
print('new_str = ' ,end='')
for k in range(len(a)):
    print("{0}{1}".format(a[k:k+1],b[k:k+1]),end='')
print()
print('new_str2 = ' ,end='')

for k in range(len(a)):
    print("{0}{1}".format(a[k:k+1],b[len(a)-1-k:len(a)-k]),end='') 


# start stop end -1-2-3-4