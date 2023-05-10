# 把工作目录在运行当前代码的时候设置为当前python文件所在的目录
import os,sys
os.chdir(sys.path[0])
# 统计数据集dataSet2.csv的样本个数
import pandas as pd
# 使用绝对路径不用设置工作目录
# df=pd.read_csv(r"E:\workspace\python\admin\class3\dataSet2.csv")
df=pd.read_csv('./dataSet2.csv')
# 统计H3MeK4_N列特征值个数
h3mek4_n_counts = df['H3MeK4_N'].value_counts()
print("H3MeK4_N列特征值个数为：\n", h3mek4_n_counts)

# 统计CaNA_N列特征值个数
cana_n_counts = df['CaNA_N'].value_counts()
print("CaNA_N列特征值个数为：\n", cana_n_counts)

# 统计class列中每个类别的样本个数
class_counts = df['class'].value_counts()
print("class列的类别个数为：", class_counts.shape[0])
print("class列每个类别的样本个数为：\n", class_counts)

# 统计grade列中每个类别的样本个数
grade_counts = df['grade'].value_counts()
print("grade列的类别个数为：", grade_counts.shape[0])
print("grade列每个类别的样本个数为：\n", grade_counts)

# 计算H3MeK4_N列的均值、方差及中位数
h3mek4_n_stats = df['H3MeK4_N'].describe()
h3mek4_n_mean = h3mek4_n_stats['mean']
h3mek4_n_var = h3mek4_n_stats['std'] ** 2
h3mek4_n_median = h3mek4_n_stats['50%']
print("H3MeK4_N列的均值为：", h3mek4_n_mean)
print("H3MeK4_N列的方差为：", h3mek4_n_var)
print("H3MeK4_N列的中位数为：", h3mek4_n_median)

# 计算CaNA_N列的均值、方差及中位数
cana_n_stats = df['CaNA_N'].describe()
cana_n_mean = cana_n_stats['mean']
cana_n_var = cana_n_stats['std'] ** 2
cana_n_median = cana_n_stats['50%']
print("CaNA_N列的均值为：", cana_n_mean)
print("CaNA_N列的方差为：", cana_n_var)
print("CaNA_N列的中位数为：", cana_n_median)
