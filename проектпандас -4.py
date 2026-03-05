import pandas as pd
import numpy as np

def del_d(row):
    if row['status'] == 'Cancelled':
        row['delivery_days'] = -1
    else:
        row['delivery_days'] = (row['delivered_date'] - row['order_date']).days

    return row
data = {
    'order_date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04'],
    'delivered_date': ['2023-10-05', '2023-10-10', '2023-10-03', '2023-10-07'],
    'status': ['Shipped', 'Shipped', 'Cancelled', 'Shipped']
}

df = pd.DataFrame(data)

# Сначала превратим строки в настоящие даты, чтобы их можно было вычитать
df['order_date'] = pd.to_datetime(df['order_date'])
df['delivered_date'] = pd.to_datetime(df['delivered_date'])

# ТВОЯ ЗАДАЧА:
# Напиши функцию check_delivery(row), которая создаст столбец 'days_diff'
# Подсказка: разницу в днях можно получить так: (дата2 - дата1).days

df = df.apply(del_d,axis = 1)
print(df)