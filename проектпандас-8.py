import numpy as np
import pandas as pd

df = pd.read_csv('movie_scores.csv')

print(df.isnull())#метод df.isnull() проверка на nan

print(df.notnull())#метод обратный df.isnull() то есть nan=False

print(df[df['pre_movie_score'].notnull()])

print(df[df['pre_movie_score'].isnull()])

#оставить данные как есть 1
#удалить данные 2
#заменить какими-то другими значениями 3

print(df.dropna(thresh=1))#параметр trashold=1 задает минимальное количество заполненных (не-NaN) значений, которое должно быть в строке или столбце, чтобы их не удалили. 
print(df.dropna(subset=['last_name']))


print(df.fillna('0'))
df['pre_movie_score'] = df['pre_movie_score'].fillna(0)
print(df)