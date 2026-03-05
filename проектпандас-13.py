import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([
    ('RU', 'Data Science', 'DS_01'),
    ('RU', 'Data Science', 'DS_02'),
    ('RU', 'Design', 'DES_01'),
    ('KZ', 'Data Science', 'DS_03'),
    ('KZ', 'Marketing', 'MAR_01'),
    ('KZ', 'Marketing', 'MAR_02'),
    ('BY', 'Design', 'DES_02'),
    ('BY', 'Marketing', 'MAR_03'),
], names=['Country', 'Course', 'Stream_ID'])

df = pd.DataFrame({
    'Students': [120, 80, 200, 50, 150, 90, 110, 70],
    'Price_per_One': [50000, 55000, 30000, 45000, 25000, 28000, 32000, 26000],
    'Ad_Spend': [1000000, 800000, 1500000, 500000, 600000, 400000, 700000, 300000]
}, index=index)

print("--- Данные по курсам ---")
print(df)

#1
print('______________________________Revenue_________________________________________________')
df1 = df.copy()
df1['Revenue'] = df1['Students']*df1['Price_per_One']
df1['Net_Profit'] = df1['Revenue']-df1['Ad_Spend']
print(df1)
print('______________________________________________________________________________________')
print('\n')
#2
print('______________________________СРАВНЕНИЕ_______________________________________________')
df2 = df.copy()
df2['Revenue'] = df2['Students']*df2['Price_per_One']
df2['Country_A_R'] = (df2.groupby('Country')['Revenue'].mean()).round()
print(df2)

print('______________________________________________________________________________________')
print('\n')
#3
print('______________________________СРЕЗ_______________________________________________')
df3 = df.copy()

df3['Revenue'] = df3['Students']*df3['Price_per_One']
df3['Net_Profit'] = df3['Revenue']-df3['Ad_Spend']

df4 = df3.xs(key='Data Science',level='Course')
print(df4)
print('_________________________________________________________________________________')

print('\n')
#4
print('______________________________ФИЛЬТРАЦИЯ_______________________________________________')

print(df4[df4['Net_Profit'] >= 2500000])

print('_______________________________________________________________________________________')