import numpy as np
import pandas as pd

df = pd.read_csv('mpg.csv')

# Группируем по году и цилиндрам, считая статистику для MPG и Weight
# Получаем мульти-индекс в строках (year, cyl) и в столбцах (metric, stat)
task_df = df.groupby(['cylinders','model_year'])['mpg'].mean()
multi = df.set_index(['model_year', 'cylinders', 'origin']).sort_index()

#1
print(multi.xs(key=78,level='model_year'))

#2
print(df.set_index('origin').xs(1))
