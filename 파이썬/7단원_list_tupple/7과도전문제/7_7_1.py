fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']
mostlen = []
''' fruit_list.remove(max(fruit_list)) '''
print('가장 길이가 긴 문자열 :' , end = ' ')
for i in fruit_list:
    if(len(i) == len(max(fruit_list))):
        mostlen.append(i)
print(mostlen[0], ' , ' , mostlen[1])
for i in mostlen:
    fruit_list.remove(i)
print(fruit_list)