import string

src_str = string.ascii_uppercase # 대문자
dst_str = src_str[3:] + src_str[:3] 
# 문제 해결 방법
# 입력된 값을 src_str에 대입한 후 입력된 문자열의 인덱스 번호를 dst_str에 대입


def ciper(a):
    idx = src_str.index(a) # a에 대입된 문자순서인 인덱스값을 idx에 대입한다.
    return dst_str[idx] # 카이사르 암호에 대입한다.

src = input('문장을 입력하세요 : ')
print('암호화된 문장 : ',end='')

for ch in src:
    if ch in src_str:
        print(ciper(ch),end='')
    else:
        print(ch,end='')
print()