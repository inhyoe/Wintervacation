import string

src_str = string.ascii_uppercase
dst_str = src_str[3:]+src_str[:3]

def ciper(a):
    idx = src_str.index(a)
    return dst_str[idx]

src = input('암호를 입력하시오')
print('암호화된 문장 :',end = '')

for ch in src:
    if ch in src_str:
        print(ciper(ch),end='')
    else:
        print(ch,end='')
        
print()