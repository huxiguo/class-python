# 把工作目录在运行当前代码的时候设置为当前python文件所在的目录
import os,sys
os.chdir(sys.path[0])
# 统计数据集dataSet2.csv的样本个数
import pandas as pd
# 使用绝对路径不用设置工作目录
# df=pd.read_csv(r"E:\workspace\python\admin\class3\dataSet2.csv")
df=pd.read_csv('./dataSet2.csv')

# 筛选出H3MeK4_N列和CaNA_N列在最大最小阈值内的数据
df_filtered = df[(df['H3MeK4_N'] >= 0.2) & (df['H3MeK4_N'] <= 2) &
                 (df['CaNA_N'] >= 0.2) & (df['CaNA_N'] <= 2)]

# 将处理完的数据另存为学号_data1.csv
df_filtered.to_csv("学号_data1.csv", index=False)

