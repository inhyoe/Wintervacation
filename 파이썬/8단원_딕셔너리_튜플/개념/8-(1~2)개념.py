""" 딕셔러리와 리스트의 차이점
    딕셔너리는 값과 키가 있다.
    딕셔너리 생성 방법 """
# 딕셔너리 생성 방법
변수 = {} # 공백 딕셔너리 생성 후
변수['홍길동'] = "010-3636-9292" #홍길동 이라는 키값에 전화번호 입력
print(변수)



#딕셔너리 생성과 동시에 초기화 하는 방법
print('-----------------------1')

변수 = {'홍길동': "010-6631-3964"}
변수 = {'강감찬': '010-9393-9393'}
변수 = {'이인재': '010-9352-4123'} # 이 방법은 생성과 동시에 초기화 하므로 키값을 넣을 때는 적절하지 않음.
print(변수)




print('-----------------------2')
변수['홍길동'] = '010-6631-3964'
변수['강감찬'] = '010-2144-3224'
print(변수)
print(변수.keys()) # 변수의 키를 나타낸다
print(변수.values()) # 각각의 변수의 값을 나타낸다
print(변수.items()) # 변수의 키와 값을 나타낸다.

for name,phone_num in 변수.items():
    print(name,":",phone_num)  
    # 변수의 키와 값을 아렇게 나타낼 수도 있다.
    
    
    
print('-----------------------3')
person = {'Name' : '홍길동','Age':27,'Class':'초급'}
person['Name'] = '이영호'
print(person['Age'])
print(person['Name'])

test = {'강감찬' : '010-6631-3964','모씨':'010-8382-4829'}
for 이름,전화번호 in test.items():
    print('이름 : ' , 이름,'전화번호 : ' ,전화번호)


contect = {'성':'김','이름':'모찌','직장':'에스택'}
print(contect.keys())
print(contect.values())

print(contect.items())
for 성이름직장,내용 in contect.items():
    print(성이름직장,'',내용,'') # 질문하기

