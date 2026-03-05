import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([
    ('Moscow', 'Electronics', 'Express'),
    ('Moscow', 'Electronics', 'Standard'),
    ('Moscow', 'Food', 'Express'),
    ('Spb', 'Electronics', 'Standard'),
    ('Spb', 'Food', 'Standard'),
    ('Spb', 'Food', 'Express'),
    ('Kazan', 'Food', 'Express'),
    ('Kazan', 'Electronics', 'Standard'),
], names=['City', 'Type', 'Delivery'])

def mrg(row):
    ans = ((row['Revenue']-row['Cost'])/row['Revenue'])*100
    return ans

def vb(row):
    if row['Margin']>=15:
        return row
    elif row['Margin']<15:
        pass

df = pd.DataFrame({
    'Revenue': [50000, 30000, 2500, 45000, 1500, 2000, 2200, 35000],
    'Cost': [42000, 25000, 1800, 38000, 1200, 1700, 1600, 31000],
    'Items_Sold': [1, 2, 5, 1, 10, 8, 7, 1]
}, index=index)

print("--- Исходный DataFrame ---")
print(df)


print('\n')
print('_________________________________МАРЖА______________________________')
df['Margin'] = df.apply(mrg,axis=1)
print(df)
print('____________________________________________________________________')

print('\n')
print('_________________________________MAХ_З______________________________')
ans = df.groupby('Type')['Revenue'].max()
ans1 = df.groupby('Type')['Revenue'].sum()
print((ans1/ans)*100)
print('____________________________________________________________________')

print('\n')

print('_________________________________ВЫБОР______________________________')

df1 = df.xs(key='Moscow',level='City').xs(key='Express',level='Delivery')
print(df1[df1['Margin'] >= 15])


