# def add(num1, num2):
#     return num1+num2

[1, 2, 3, [1, 2, 3, 'a']]
# print(add(1, 20))

num = 0


def test():
    global num
    num = 100
    print(num)  # 100


test()
print(num)  # 100
