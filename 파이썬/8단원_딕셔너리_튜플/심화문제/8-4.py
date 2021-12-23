lst = [10,30,40,50,30,30,20,20,20,10,30]
new_list = []
hap = 0
""" for i in lst:
    print(i) """
for i in lst:
    for k in lst:
        if i == k:
           hap = hap +1 # i , k 값이 같을경우 hap을 출력하고
        
    if hap < 2: # hap이 2미만이면 중복되지 않았다는 의미이므로 
        new_list.append(i) # i 값을 출력.
    
    hap = 0 # 합은 k반복문이 종료되면 초기화한다.
""" new_list = new_list.append(1) """


# 2) 중복되는 원소를 한번씩만 출력하자.

print(set(lst)) # set 메서드를 이용하여 출력한다.


# 3) 중복 빈도 출현을 나타내자.
lst = sorted(lst)
for i in lst:
    for k in lst:
        if i == k:
           hap = hap +1
        
    if hap < 2:
        new_list.append(i) #1)과 같다.

    if hap >=2:
        print(i ,':',hap,'회') # i가 몇번 반복하여 출력되었는지 ,
                              # i가 반복되어 출력되지 않았다면 출력 x
        
       
    hap = 0
 # 
            
