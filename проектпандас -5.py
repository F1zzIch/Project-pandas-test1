import pandas as pd
import numpy as np

def clean_salary(row):
    
    if pd.isna(row['salary']):
        res = 0
    else:
        res = int(str(row['salary']).replace('$', '').strip())
    
    row['clean_salary'] = res
    return row

data = {
    'name': ['Anna', 'Ivan', 'Dmitry', 'Elena'],
    'salary': [60000, '75000$', None, '100000$']
}

df = pd.DataFrame(data)

# ПОДСКАЗКА: 
# 1. Проверить на NaN можно через pd.isna(значение)
# 2. Убрать символ из строки: str(значение).replace('$', '')
# 3. Не забудь привести результат к int()
df = df.apply(clean_salary,axis=1)
print(df)