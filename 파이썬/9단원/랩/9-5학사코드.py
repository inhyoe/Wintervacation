import re

text =''' 101 COM PyhtonProgramming
          102 MAT LinearAlgebra
          103 ENG ComputerEnglish'''
          
print(re.findall('\d+',text))
"match = re.search('Life',txt,)"

text1 = '''101 COM Pyhton Part1 Programming1
          102 MAT LinearAlgebra
          103 ENG ComputerEnglish'''

print(re.search('101',text1))
print(re.search('102',text1))
print(re.search('103',text1))
# 수정후
print(re.search('COM',text1))
print(re.search('COM',text1))
print(re.search('COM',text1))
