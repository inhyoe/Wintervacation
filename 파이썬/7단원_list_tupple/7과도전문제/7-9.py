def overlap(A,B):       #문자열을 합쳐주는 overlap 함수를 생성한다
    if A[0] != B[0]:
        return(A+B)
    else:
        
        return(B)
        
print(overlap('commu','munny')) # 출력한다
print(overlap('boxok','xbox'))
print(overlap('deter','detery'))
print(overlap('boxok','xbox'))
print(overlap('waycom','ycomget'))
print(overlap('tttt','ttttt'))
