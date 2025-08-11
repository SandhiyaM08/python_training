'''import csv
import pandas as pd
import json
import random
import zipfile

old=pd.read_csv("old_airline_data_2023.csv")
new=pd.read_json("new_airline_data_2024.json")


missing_value=new.isnull().sum()
new.iloc[:,1:]=new.iloc[:,1:].fillna(new.iloc[:,1:].mean())

new.dropna()
new[new['Month'].isin(['Jan','Feb'])]

new.columns=new.columns.str.lower()
new.columns=new.columns.str.replace(' ','_')
new['month']=new['month'].str.capitalize()
new=new.groupby('month',as_index=False).first()

#combined_airline_data
combined_df=pd.concat([new,old],ignore_index=True)
print(combined_df)


combined_df['year']=[random.choice([2023, 2024]) for _ in range(len(combined_df))]
	

month_counts = combined_df['Month'].value_counts()
months_once = month_counts[month_counts == 1].index.tolist()

combined_df=combined_df.sort_values('year',ascending=True)

############

combined_df=combined_df.dropna(subset=['Passengers Carried','Target Passengers','Flights Operated'])

combined_df.columns=combined_df.columns.str.replace(' ','_')
	
combined_df['pct_diff_target'] = ((combined_df['Passengers_Carried'] - combined_df['Target_Passengers']) /combined_df['Target_Passengers'])* 100


target_not_achieved=combined_df[combined_df['pct_diff_target']<0]
print(target_not_achieved[['Month','year','pct_diff_target']])

#yearly summary
yearly_summary=combined_df['Passengers_Carried'].sum()
print(yearly_summary)
yearly_summary=combined_df['Flights_Operated'].sum()
print(yearly_summary)
yearly_summary=combined_df.groupby('Month')['pct_diff_target'].mean()
print(yearly_summary)


best = combined_df[combined_df['pct_diff_target'] ==combined_df['pct_diff_target'].max()]
print(best[['month', 'year', 'pct_diff_target']])


worst = combined_df[combined_df['pct_diff_target'] == df['pct_diff_target'].min()]
print(worst[['month', 'year', 'pct_diff_target']])


combined_df=combined_df.to_csv("combined_df_data.csv",index=False)
target_not_achieved=target_not_achieved.to_csv("target_not_achieved.csv",index=False)
yearly_summary=yearly_summary.to_json("yearly_summary.json",index=False)


with zipfile.ZipFile("airline_analysi_outputs.zip",'w') as zf:
	zf.write("combined_df_data.csv")
	zf.write("target_not_achieved.csv")
	zf.write("yearly_summary.json")

print("Successfully")'''

import csv
import json
import pandas as pd
import zipfile
import random

new=pd.read_json("new_airline_data_2024.json")
old=pd.read_csv("old_airline_data_2023.csv")

missing_values=new.isnull().sum()
new.iloc[:,1:]=new.iloc[:,1:].fillna(new.iloc[:,1:].mean())

new.dropna()
new[new['Month'].isin(['Jan','Feb'])]

new.columns=new.columns.str.lower().str.replace(' ','_')
new.columns=new.columns.str.capitalize()
new = new.groupby('Month', as_index=False).first()

combined_df=pd.concat([old,new],ignore_index=True)

combined_df['year']=[random.choice
([2023,2024]) for _ in range(len(combined_df))]

month_counts=combined_df['Month'].value_counts()
month_once=month_counts[month_counts==1].index.tolist()



combined_df=combined_df.sort_values('year','month',ascending=True,True)
combined_df.columns=combined_df.columns.str.replace(' ','_')

combined_df['pct_diff_target']=((combined_df['Passengers_Carried'] - combined_df['Target_Passengers']) / combined_df['Target_Passengers']) * 100

target=combined_df[combined_df['pct_diff_target']<0]
print(target[['Month','year','pct_diff_target']])

annual_summary=combined_df['Passengers_Carried'].sum()
annual_summary=combined_df['Flights_Operated'].sum()
annual_summary=combined_df.groupby('pct_diff_target')['pct_diff_target'].mean()
best=combined_df[combined_df['pct_diff_target']==combined_df['pct_diff_target'].max()]

worst=combined_df[combined_df['pct_diff_target']==combined_df['pct_diff_target'].min()]
print(best)
print(worst)

'''combined_df=combined_df.to_csv("combined_airline_data.csv",index=False)
target=target.to_csv("target_not_achieved.csv",index=False)
annual_summary=annual_summary.to_json("yearly_summary.json",index=False)

with open zipfile.ZipFile("airline_analysis_outputs.zip",'w') as z:
	z.write("combined_airline_data.csv")
	z.write("target_not_achieved.csv")
	z.write("yearly_summary.json")'''














