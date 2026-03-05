import pandas as pd
import numpy as np

def cl_s(row):
    
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

df = df.apply(cl_s,axis=1)
print(df)
