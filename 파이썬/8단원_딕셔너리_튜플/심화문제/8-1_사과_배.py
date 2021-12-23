
fruit_names = ['사과', '배', '수박', '귤', '포도']
fruit = input('사과 배 수박 귤 포도 가격을 공백으로 구분하여 입력 : ')
split_fruit_value = fruit.split() # 스플릿을 하여 각각의 값을 리스트로 받았음.
fruits_dic = {}
print('——————— 오늘의 과일 가격 ———————')
for i in range(len(fruit_names)):
    fruits_dic[fruit_names[i]] = split_fruit_value[i]
for k, v in fruits_dic.items(): # k 값에 키값 v값에 value 대입
    print(k , ":", v) 

