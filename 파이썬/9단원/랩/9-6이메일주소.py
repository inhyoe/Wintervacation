import re

txt = ' abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다'
regex = re.complie('(\d{3})와(\d{4})')
match_obj = regex.search(txt)

print(match_obj.group(1),match_obj.group(2))