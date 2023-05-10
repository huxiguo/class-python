# 定义元组
# 不能修改结构
tup1 = (1, 2, False, [1, 2, 3])
print(tup1)
tup1[3][0] = 4
print(tup1)

tup2 = (1, (2, (3)))
# print(tup2)

tup3 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

# 下标取出数据
# print(tup1[0])
# print(tup1[3][0])

# print(tup2[1][1])

# index 查找
# print(tup2.index(1))

# count 统计出现次数
# print(tup3.count(1))

# len 元组长度
# print(len(tup2))

# for i in tup2:
#     print(i)
