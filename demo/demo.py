import pandas as pd

data = [['a','b','c'], ['1','2','3','4']]

def createDataFrame():
  df = pd.DataFrame(data, columns=['name', 'value', 'key', 'values'])
  return df

if __name__ == '__main__':
  df = createDataFrame()
  print(df)
