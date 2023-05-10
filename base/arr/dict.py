my_dict1 = {
    'zs': 99,
    'ls': 100
}
print(my_dict1['zs'])

score = {
    'zs': {
        '语文': 77,
        '数学': 66,
        '英语': 33
    },
    'ls': {
        '语文': 88,
        '数学': 86,
        '英语': 55
    },
    'xm': {
        '语文': 99,
        '数学': 96,
        '英语': 66
    }
}
for k in score:
    print(score[k])
# print(score['zs']['语文'])  # 77
# print(score.keys())
# score['zs']['语文'] = 100
# score['hh'] = {'语文': 100}
# print(score)

# print(score.pop('hh'))
# print(score)
