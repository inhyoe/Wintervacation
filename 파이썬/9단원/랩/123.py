import re

s = 'Korea is awesome! I REALLY LOVE KOREA'
print(len(re.findall('korea', s, re.I)))