# 集合set 去重，顺序无法保证
set1 = {'1', '2', '3', '4'}
for i in set1:
    print(i)
len(set1)
# print(set1)
set1.add(666)
# print(set1)

# set1.remove('1')
# print(set1)

# print(set1.pop())
# set1.clear()

set2 = {1, 2, 3}
set3 = {1, 2, 4}
# set2.difference_update(set3)
# print(set2)
print(set2.union(set3))
