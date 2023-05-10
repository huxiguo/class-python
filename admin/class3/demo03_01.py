import os,sys
os.chdir(sys.path[0])
import pandas as pd
df=pd.read_csv('./dataSet2.csv')
# 删除包含缺失值的行
df_cleaned = df.dropna()

# 将处理完的数据另存为学号_data2.csv
df_cleaned.to_csv("学号_data2.csv", index=False)
