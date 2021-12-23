print('사전 프로그램 시작 .. 종료는 q를 입력,,')
사전= {}


while True:
    st = input('$ ')
    command = st[0]
    if command == '<':
        st1 = st[2:]        # one : 하나
        input_str = st1.split(':')      # :을 기준으로 나눈다.{ 'one' , 'two'}
        사전[input_str[0]] = input_str[1] # 
        print(사전)
        print(사전.keys())
        
    elif command == '>':
        st = st[1:]
        input_str = st.strip()
        if 사전[st1] in 사전:
            st1 = st[2:]
            print(st1)
            print(사전[st1])
        else:
            print(command,'가 사전에 없습니다')    
        
        
    elif command == 'q':
        print('사전을 종료합니다.')
        break
    
        
        
        