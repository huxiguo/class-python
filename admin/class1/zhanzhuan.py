# 用户输入两个数，输出最大公约数
print("请输入两个数：")
a = int(input("a = "))
b = int(input("b = "))
if a > b:
    a, b = b, a  # 交换两个数
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print("%d和%d的最大公约数是%d" % (a, b, factor))
        print("%d和%d的最小公倍数是%d" % (a, b, a*b//factor))
        break  # 一旦找到最大公约数就退出循环
