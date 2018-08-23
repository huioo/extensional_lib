import pandas as pd
import numpy as np
import datetime
import openpyxl


df = pd.read_csv('gain_and_loss.csv')
df_a = df.values
# 最大盈利
indices1 = df_a.argmax(axis=0)[1]
date1 = df.iat[indices1, 0]
money1 = df.iat[indices1, 1]
print('最大盈利', money1, '时间', date1)

# 最大亏损
indices2 = df_a.argmin(axis=0)[1]
date2 = df.iat[indices2, 0]
money2 = df.iat[indices2, 1]
print('最大亏损', money2, '时间', date2)

# 最大持续盈利
df1 = df[df.realized_gain_and_loss >= 0]
temp = None
# temp_date = None
temp_count = 0
temp_start = None
temp_end = None

count1 = []
for indices in df1.index:
    if temp is None:
        temp = indices
    # if temp_date is None:
    #     temp_date_start = datetime.datetime.strptime(df1.loc[indices].date, '%Y%m%d')
    if temp_start is None:
        temp_start = df1.loc[indices].date
    
    temp_end = df1.loc[indices].date
    if indices == temp:
        temp_count += 1
    else:
        count1.append([temp_count, temp_start, temp_end])
        temp_start = df1.loc[indices].date
        temp_count = 1

    temp += 1

temp_duration1 = max(count1, key=lambda x: x[0])
print('最大持续盈利次数', temp_duration1[0], '时间段', temp_duration1[1], temp_duration1[2])


# 最大亏损时间
df2 = df[df.realized_gain_and_loss <= 0]
temp = None
# temp_date = None
temp_count = 0
temp_start = None
temp_end = None

count2 = []
for indices in df2.index:
    if temp is None:
        temp = indices
    # if temp_date is None:
    #     temp_date_start = datetime.datetime.strptime(df2.loc[indices].date, '%Y%m%d')
    if temp_start is None:
        temp_start = df2.loc[indices].date
    
    temp_end = df2.loc[indices].date
    if indices == temp:
        temp_count += 1
    else:
        count2.append([temp_count, temp_start, temp_end])
        temp_start = df2.loc[indices].date
        temp_count = 1
    
    temp += 1

temp_duration2 = max(count2, key=lambda x: x[0])
print('最大持续亏损次数', temp_duration2[0], '时间段', temp_duration2[1], temp_duration2[2])


money = df.sum(axis=0).realized_gain_and_loss
all_money = 500000 + money
# n = abs((datetime.datetime.strptime('20130104', '%Y%m%d') - datetime.datetime.strptime('20171211', '%Y%m%d')).days)
# 年化复利收益率
rate1 = (all_money/500000)**(1/500) -1

# 年化单利收益率
rate2 = money/5/500000


# 表格
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['最大盈利（数值）', '最大亏损（数值）', '最大盈利时间（时间）', '最大亏损时间（时间）', '最大持续盈利次数（数值）',
              '最大持续盈利时间（时间段）', '最大持续亏损次数（数值）', '最大持续亏损时间（时间段）', '年化单利收益率', '年化复利收益率'])
sheet.append([money1, money2, date1, date2, temp_duration1[0], temp_duration1[1]+'~'+temp_duration1[2],
             temp_duration2[0], temp_duration2[1]+'~'+temp_duration2[2], '%.5f' % rate2, '%.5f' % rate1])

wb.save('result.xlsx')



