import random

num = random.randint(1, 100)
flag = True
print('开始猜数字')
while flag:
    guess_num = int(input('请输入你猜的数字:'))
    if guess_num < num:
        print('你猜的数字太小了，重新猜一下。')
    elif guess_num > num:
        print('你猜的数字太大了，重新猜一下。')
    else:
        print('恭喜你，猜对了！！')
        flag = False
