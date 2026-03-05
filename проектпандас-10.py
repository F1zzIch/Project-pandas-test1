import pandas as pd

# Создаем MultiIndex DataFrame
index = pd.MultiIndex.from_product(
    [['2023', '2024'], ['City_A', 'City_B'], ['Sales', 'Profit']],
    names=['Year', 'City', 'Metric']
)
df = pd.DataFrame([100, 20, 150, 35, 120, 25, 180, 45], index=index, columns=['Value'])

print(df)

print('\n')

#1
print(df.xs(key='2024',level='Year'))

print('\n')
#2
print(df.xs(key='Profit',level='Metric'))

#3
print(df.xs(key='City_A',level='City').xs(key='2023',level='Year'))