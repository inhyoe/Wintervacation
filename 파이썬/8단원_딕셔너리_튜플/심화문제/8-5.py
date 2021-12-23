print('사전 프로그램 시작')
dictionary = {}

while True:
    st = input('$ ')
    command = st[0]
    if command == '<':
        st = st[1:]
        inputStr = st.split(':') # 구분자 : 를 이용한다.
        if len(inputStr) < 2 : # 3개 이상의 값을 입력한 경우
            print('입력 오류')
        else:
            dictionary[inputStr[0].strip()]= inputStr[1].strip() # 딕셔너리에 저장된 key inputStr[0].strip 값 inputStr[1].strip()
                                                                 # 이때 strip()함수를 사용한 이유는 빈칸을 없에기 위함이다
                                                                 
    elif command == '>':
        st = st[1:]
        inputStr = st.split()
        if inputStr in dictionary :            
            print(dictionary[inputStr.split()])
        else:
            print(dictionary)
            print(dictionary(inputStr))
            print('잘못 입력하셨습니다.')

    elif command == 'v':
        print('영어 사전에 있는 단어와 뜻을 출력합니다')
        print(dictionary)