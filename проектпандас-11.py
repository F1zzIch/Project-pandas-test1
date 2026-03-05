import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([
    ('Morning', 'Cakes', 'Order_1'),
    ('Morning', 'Cakes', 'Order_2'),
    ('Morning', 'Bread', 'Order_3'),
    ('Evening', 'Cakes', 'Order_4'),
    ('Evening', 'Bread', 'Order_5'),
    ('Evening', 'Bread', 'Order_6'),
], names=['Shift', 'Category', 'ID'])

df = pd.DataFrame({
    'Price': [1500, 2000, 500, 1800, 400, 600],
    'Status': ['Delivered', 'Cancelled', 'Delivered', 'Delivered', 'Delivered', 'Refunded']
}, index=index)


def roi(row):
    ans = 0
    if row['Status'] == 'Delivered':
        ans += row['Price']
    elif row['Status'] =='Cancelled':
        ans += 0
    elif row['Status'] == 'Refunded':
        ans -= row['Price']
    
    return ans



print(df)

print('\n')
#1
print('_________Вечерние заказы_________')
print(df.xs(key='Evening',level='Shift'))
print('_________________________________')
print('\n')

#2 типа дополнение
print('_________Общая выручка___________')
df['LTV'] = df.apply(roi, axis=1)
print(df)
print(f'{df['LTV'].sum()} - за все заказы')
ans = df.groupby('Status')['Price'].sum()
print(ans)
print('_________________________________')
print('\n')

#3 логика
df_indexed = df.set_index('Status', append=True) #перенс индекс

print('_________________________________')
df1 = df_indexed.xs(key=('Cakes', 'Delivered'), level=['Category', 'Status'])
print(df1)
print(df1['LTV'].mean())
print('_________________________________')

