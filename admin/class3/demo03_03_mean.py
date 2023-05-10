import os,sys
os.chdir(sys.path[0])
import pandas as pd
df=pd.read_csv('./dataSet2.csv')

# 使用均值填充H3MeK4_N列中的缺失值
mean = df['H3MeK4_N'].mean()
df['H3MeK4_N'].fillna(mean, inplace=True)

# 将处理完的数据另存为学号_data4.csv
df.to_csv("113120200176_data4_mean.csv", index=False)