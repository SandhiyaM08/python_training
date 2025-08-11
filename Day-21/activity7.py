import pandas as pd
df=pd.read_csv('student.csv')
result=df[(df['mark']>=70) &((df['class']=='Four') | (df['class']=='Five' ))&(df['gender']=='male')]
print(result)



