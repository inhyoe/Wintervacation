items = { "커피음료":7,'펜':3,'종이컵':2,'우유':1,'콜라':4,'책':5}

while True:
    menu = int(input('1) 재고조회 2)입고 3)출고 4)종료 : '))
    if menu == 1:
        name =  input('[재고 조회]물건의 이름을 입력하세요')
        print(items[name])
    elif menu == 2:
        입고 = input('[입고] 물건의 이름과 수량을 입력하세요')
        수정_입고 = 입고.split()
        이름 = 수정_입고[0]
        수량 = 수정_입고[1] 
        print(items['콜라'])
        print(수량)
        update =int(수량)+int(items[수량]) #반드시 타입을 바꿔줘야함. ***
        items[이름] = update
        print(이름 ,'의 재고 : ' , items[이름])
    elif menu == 3:
        출고 = input('[출고]물건의 이름과 수량을 입력하세요')
        수정_출고 = 출고.split()
        이름 = 수정_출고[0]
        수량 = 수정_출고[1]
        잔고량 =  int(items[이름]) -int(수량) 
        items[이름] = 잔고량
        print(이름,'의 재고',items[이름] )
    elif menu == 4:
        print('프로그램을 종료합니다')
        break
        
        
        
        



       #
""" 
dict = { 'one' : 0, 'two' : 2 }

dict['one'] = 1
 """