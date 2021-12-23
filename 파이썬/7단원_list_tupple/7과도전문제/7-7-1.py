fruit_list  =  ['orange','banana','kiwi','apple','melon']
max = 0 # 최대값의 원소를 찾기
max_len = []


for i in range(len(fruit_list)): # fruit_list만큼 반복한다
    
    if len(fruit_list[i]) >= max:
        max = len(fruit_list[i])   # max값을 찾는다,
        max_len.append(fruit_list[i])
        print(max)
   
     
print('가장 길이가 긴 문자열 : ',max_len)
for i in range(len(fruit_list)-len(max_len)):
    if len(fruit_list[i]) == max:
        fruit_list.remove(fruit_list[i])

print('fruit_list = ',fruit_list) 
    
