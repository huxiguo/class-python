import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts

f_usa = open('project/usa.txt', 'r', encoding='UTF-8')
f_jp = open('project/jp.txt', 'r', encoding='UTF-8')
f_ind = open('project/ind.txt', 'r', encoding='UTF-8')

us_data = f_usa.read()
jp_data = f_jp.read()
ind_data = f_ind.read()


us_data = us_data.replace('jsonp_1629344292311_69436(', '')
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
ind_data = ind_data.replace('jsonp_1629350745930_63180(', '')


us_data = us_data[:-2]
jp_data = jp_data[:-2]
ind_data = ind_data[:-2]


us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
ind_dict = json.loads(ind_data)


# trend
us_trend = us_dict['data'][0]['trend']
jp_trend = jp_dict['data'][0]['trend']
ind_trend = ind_dict['data'][0]['trend']


# 日期
x_data_us = us_trend['updateDate'][:314]
x_data_jp = jp_trend['updateDate'][:314]
x_data_ind = ind_trend['updateDate'][:314]


# 确诊
y_data_us = us_trend['list'][0]['data'][:314]
y_data_jp = jp_trend['list'][0]['data'][:314]
y_data_ind = ind_trend['list'][0]['data'][:314]

# 折线图对象
line = Line()

# X轴数据
line.add_xaxis(x_data_us)
# Y轴数据
line.add_yaxis('美国确诊人数', y_data_us, label_opts=LabelOpts(is_show=False))
line.add_yaxis('小日本确诊人数', y_data_jp, label_opts=LabelOpts(is_show=False))
line.add_yaxis('阿三确诊人数', y_data_ind, label_opts=LabelOpts(is_show=False))

# 生成图表
line.render()
f_ind.close()
f_jp.close()
f_usa.close()
