import pandas as pd

data = [['a','b','c'], ['1','2','3','4']]
df = pd.dataframe(data, columns=['name','value','key','values'])

print(df)
