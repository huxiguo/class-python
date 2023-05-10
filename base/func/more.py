# def test1():
#     return 1, 2


# x, y = test1()
# print(x)  # 1
# print(y)  # 2


# def user_info(**kwargs):
#     print(kwargs)


# user_info('zs', 20, '男')
# user_info(age=20, name='zs', gender='女')


# def add(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum


# print(add(1, 2, 3, 4, 5, 6))

def test_func(func):
    result = func(1, 2)
    print(result)


def com(num1, num2):
    return num1+num2


test_func(com)
test_func(lambda x, y: x+y)
