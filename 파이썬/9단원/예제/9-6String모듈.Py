import string

src_str = string.ascii_uppercase # 대문자 모듈
print(src_str) 
src_str = string.ascii_lowercase # 소문자 모듈
print(src_str) 

# ------------------------
n = src_str.index('a')
print('src_str의 a 인덱스 =',n) # 'a'가 있는 번호를 출력한다.

dst_str = src_str[1:]  + src_str[:1] # b~z까지 + a
print(dst_str)
print('src_str의 a 위치에 있는 dst_str의 문자 =',dst_str[n]) # b

