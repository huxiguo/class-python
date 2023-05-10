import os,sys
os.chdir(sys.path[0])
import pandas as pd
df=pd.read_csv('./dataSet2.csv')

# 使用全1填充H3MeK4_N列中的缺失值
df['H3MeK4_N'].fillna(1, inplace=True)

# 将处理完的数据另存为学号_data3.csv
df.to_csv("学号_data3.csv", index=False)