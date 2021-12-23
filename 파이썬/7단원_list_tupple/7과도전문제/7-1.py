num_list = [100,200,300,400,500,600,700,800]
#           0   1   2   3   4   5   6   7
high = 6
low = 3
#num_list[high]
print(num_list[high]) # 700
#num_list[ high - 2 ]
print( num_list[ high - 2 ] ) # 인덱스값은 4이므로 500
#num_list[ high - low ]
print(num_list[ high - low ] ) # 인덱스값은 3이므로 400
#num_list[- 1 ]
print( num_list[-1]) # 뒤에서부터 시작하므로 800
#num_list[ 2*3]
print( num_list[2*3]) # 인덱스값은 6이므로 700
#num_list[ 2 ] *3
print( num_list[2] * 3 ) #300 *3 = 900
#num_list[ 5%4 ]
print( num_list[5%4] ) # 정수형 계산이므로 인덱스값 1 = 100
#len(num_list)
print( len(num_list) ) # 길이를 반환하므로 7
#min(num_list)
print( min(num_list) ) # 최솟값을 반환하므로 100
#max(num_list)
print( max(num_list) ) # 최댓값을 반환하므로 700
#num_list[:3]
print(num_list[:3]) # start값 0 end값 3이므로 0~2인덱스값까지 출력
# num_list[1:5]
print(num_list[1:5]) # start 값 1 end값 5이므로 1~4인덱스값까지 출력
# num_list[-1:-5:-1] 
print(num_list[-1:-5:-1] ) # start값 -1 end값 -5 step값 -1이므로 -1~-4번째 인덱스값까지 출력
# num_list[-5:-1:1]
print(num_list[-5:-1:1]) # start값 -5 end값 -1 step값 1이므로 -5~-2번째 인덱스값까지 출력