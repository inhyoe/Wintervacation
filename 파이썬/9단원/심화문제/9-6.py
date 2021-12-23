import re
part , average , sum = 0,0,0
s = 'English = 89, Science = 90, Math = 92, History = 80.'

print(re.findall('[0-9]+',s))
print(s)
for i in re.findall('[0-9]+',s):
    part += 1
    sum += int(i)
    average = sum/part
     
print('총점 : ' , sum)
print('평균 : ' , average)
