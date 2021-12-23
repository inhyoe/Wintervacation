
fruit_names = ['사과', '배', '수박', '귤', '포도']
fruit = input('사과 배 수박 귤 포도 가격을 공백으로 구분하여 입력 : ')
split_fruit_value = fruit.split() # 스플릿을 하여 각각의 값을 리스트로 받았음.
fruits_dic = {}
print('——————— 오늘의 과일 가격 ———————')
for i in range(len(fruit_names)):
    fruits_dic[fruit_names[i]] = split_fruit_value[i]


want = input('구매를 원하는 과일의 이름을 입력하시오.') # 구매를 원하는 과일 선택
print('오늘의',want , '가격은 ' ,fruits_dic[want] ) # 출력

