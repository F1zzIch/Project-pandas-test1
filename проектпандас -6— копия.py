import pandas as pd

def prem(row):
    if row['fact']>=row['plan']:
        res = row['fact']*0.1
    elif (row['fact']<row['plan']) and (row['fact']>row['plan']*0.5):
        res = row['fact']*0.05
    else:
        res = 0
    row['bonus'] = res
    return row

data = {
    'manager': ['Игорь', 'Анна', 'Олег', 'Елена'],
    'dept': ['Standard', 'VIP', 'Standard', 'VIP'],
    'plan': [1000, 2000, 1500, 3000],
    'fact': [1200, 1800, 500, 2900]
}


df = pd.DataFrame(data)
df = df.apply(prem,axis=1)
print(df)
