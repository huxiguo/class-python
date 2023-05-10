import os,sys
os.chdir(sys.path[0])
import pandas as pd
df=pd.read_csv('./dataSet2.csv')

# 使用中位数填充H3MeK4_N列中的缺失值
median = df['H3MeK4_N'].median()
df['H3MeK4_N'].fillna(median, inplace=True)

# 将处理完的数据另存为学号_data4.csv
df.to_csv("113120200176_data4_median.csv", index=False)