city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)] # 튜플인 도시 집합.
max_city = 0 # 튜플인 도시 집합에서의 도시 인구
max_name = None
total = 0

for city in (city_info): #도시 인구 구하는 식
    if max_city > city[1]:
        
        max_city = max_city
        total = total +1
    else :
        max_city[1] = city[1]
        total = total +1
    max_city[0] = city[0]

print('최대 인구 : ' ,max_city[0], '인구 :' ,max_city[1],'천명')
print(total)

''' max_pop = 0
min_pop = 9999999
total_pop = 0

max_city = None
min_city = None

for city in city_info:
    total_pop += city[1]
    if city[1] > max_pop:
        max_pop = city[1]
        max_city = city
    if city[1] < min_pop:
        min_pop = city[1]
        min_city = city
print(max_city)
print('최대 인구 :', max_city[0] , ' 인구 : ', max_city[1] , '천명') '''
        