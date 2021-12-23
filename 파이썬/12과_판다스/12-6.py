import pandas as pd
name = pd.Series(['김수안','김수정','박동윤','강이안','강지안'])
age = pd.Series([19,23,22,19,16])
sex = pd.Series(['여','여','남','여','남'])
grade = pd.Series([4.35,4.23,4.25,4.37,4.25])
''' print(name,age,sex,grade)
 '''
df = pd.DataFrame({'이름':name,'나이':age,'성별':sex,'학점':grade})
print(df)