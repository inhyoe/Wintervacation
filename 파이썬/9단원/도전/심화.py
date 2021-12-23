import re

text =''' 101 COM PyhtonProgramming1 
        102 MAT LinearAlgebra2 
        103 ENG ComputerEnglish3''' 
        
print(re.findall('\s\d+',text))