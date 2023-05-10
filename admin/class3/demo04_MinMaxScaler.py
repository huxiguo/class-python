import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 读取原始数据
df = pd.read_csv("学号_data4.csv")

# 使用MinMaxScaler对H3MeK4_N列进行归一化
min_max_scaler = MinMaxScaler()
df["H3MeK4_N_normalized"] = min_max_scaler.fit_transform(df[["H3MeK4_N"]])

# 使用StandardScaler对CaNA_N列进行标准化
standard_scaler = StandardScaler()
df["CaNA_N_standardized"] = standard_scaler.fit_transform(df[["CaNA_N"]])

# 将处理结果保存为学号_data5.csv
df.to_csv("学号_data5.csv", index=False)