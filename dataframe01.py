import pandas as pd
from numpy.lib.function_base import average

data={
    'name':['rupa','sita','geeta'],
    'age':[25,30,35],
    'city':['bagalkote','solapur','gilbarga']
}
df=pd.DataFrame(data)

print(df)

df_sorted=df.sort_values(by='age', ascending=False)
print(df_sorted)
print(df)

df_sorted['salary']=[5000,6000,7000]
print(df_sorted['salary'])
print(df)

age_above_30=df_sorted[df_sorted['age']>30]
print(age_above_30)
print(df)

df_sorted.loc[df_sorted['name']=='sita','city']='bagalkot'
print("inDataFrame without city:in",df)

df_no_city = df_sorted.drop(columns='city')
print("DataFrame without city:", df_no_city)

average_age=df_sorted['age'].mean()
print("inaverage age:",average_age)

any_from_bagalkot = 'bagalkot' in df_sorted['city'].values
print("Is any person from Bagalkot?", any_from_bagalkot)

sita_info =df_sorted[df_sorted['name']=='sita']
print("in info of sita:ln", sita_info)

