# f = open('base/public/test.txt', 'r', encoding='UTF-8')
# print(f.readlines())
# f.close()
# with open('base/public/test.txt', 'r', encoding='UTF-8') as f:
#     for i in f:
#         print(i)

f = open('base/public/test.txt', 'a', encoding='UTF-8')
f.write('\npython is the best lang')
f.flush()
f.close()
