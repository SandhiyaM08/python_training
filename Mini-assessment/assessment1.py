'''import csv 
import json
import pandas as pd 

df_csv =pd.read_csv("old_airline_data_2023.csv")
df_json=pd.read_json("new_airline_data_2024.json")

missing_values=df_json.isnull().sum()
#print(missing_values)

#finding mean for null values
df_json.iloc[:,1:]=df_json.iloc[:,1:].fillna(df_json.iloc[:,1:].mean())
#print(df_json.iloc[:,1:])

#drop record
df_json=df_json.dropna()

#valid month
df_json.iloc[:,:1]=df_json[df_json.iloc[:,:1].isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Nov','Dec'])]


#standardization
df_json.columns=df_json.columns.str.lower()
df_json.columns=df_json.columns.str.replace(' ','_')

df_json.columns=df_json.columns.str.lower().str.replace(' ','_')


#month capitalize

df_json['month']=df_json['month'].str.capitalize()

#remove duplicate month first occurence

df_json=df_json.groupby('month',as_index=False).first()
print(df_json)


New one

import csv
import pandas as pd
import json

old=pd.read_csv("old_airline_data_2023.csv")
new=pd.read_json("new_airline_data_2024.json")
missing_values=new.isnull().sum()
new.iloc[:,1:]=new.iloc[:,1:].fillna(new.iloc[:,1:].mean())
new=new.dropna()
new.iloc[:,:1]=new[new.iloc[:,:1].isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Nov','Dec'])]
new.columns=new.columns.str.lower().str.replace(' ','_')new['month']=new['month'].str.capitalize
new=new.groupby('month',as_index=False).first()
print(new)

import json
import csv
import pandas as pd

new=pd.read_json("new_airline_data_2024.json")
old=pd.read_csv("old_airline_data_2023.csv")
#print(old)

#concat both data
new_merged=pd.concat([new,old],ignore_index=True)
#print(new_merged)

#create new column year
new['year']=2023
old['year']=2024

year_merge=pd.concat([new['year'],old['year']],ignore_index=True)
#print(year_merge)


#month should be exactly one time
new=new.groupby('Month',as_index=False).sum()
#print(new)

#sort year and month 
new=new.sort_values(['year','Month'],ascending=[True,False])
#print(new)

new.columns=new.columns.str.replace(' ','_')
#print(new.columns)

#create pct_diff_target
def pct_diff_target(row):
	pct_diff_target=(row['Passengers_Carried'] - row['Target_Passengers'])/row['Target_Passengers']*100
	return pct_diff_target
new['pct_diff_target']=new.apply(pct_diff_target,axis=1)
#print(new)

#target non-achievement
target=new[new['pct_diff_target']<0]
#print(target['Month','year','pct_diff_target'])


#total passenger in print else it overwrite for all rows
#print(new['Passengers_Carried'].sum())
#print(new['Flights_Operated'].sum())

#average across all month
average=new.groupby('Month')['pct_diff_target'].mean()

#max value and min value
maxi=new['pct_diff_target'].agg('max')
mini=new['pct_diff_target'].min()
print(mini)
print(maxi)



print(new.Month.describe())'''


import csv
import pandas as pd
import json
import random

old=pd.read_csv("old_airline_data_2023.csv")
new=pd.read_json("new_airline_data_2024.json")


'''missing_value=new.isnull().sum()
new.iloc[:,1:]=new.iloc[:,1:].fillna(new.iloc[:,1:].mean())

new.dropna()
new[new['Month'].isin(['Jan','Feb'])]

new.columns=new.columns.str.lower()
new.columns=new.columns.str.replace(' ','_')
new['month']=new['month'].str.capitalize()

combined_df=pd.concat([old,new],ignore_index=True)
combined_df['year']=[random.choice([2023, 2024]) for _ in range(len(combined_df))]
combined_df=combined_df.groupby('Month',as_index=False)

def pct_diff_target(row):
	
	pct_diff_target = ((row['Passengers Carried'] - row['Target Passengers']) / row['Target Passengers'])* 100
	return pct_diff_target
combined_df['pct_diff_target']=combined_df.apply(pct_diff_target,axis=1)

print(combined_df)'''































def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

# Example
nums = [9, 5, 1, 4, 3]
insertion_sort(nums)
print(nums)  








































