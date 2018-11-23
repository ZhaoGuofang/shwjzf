# -*- coding:utf-8 -*-

import numpy as np 
import pandas as pd 
from sklearn.utils import shuffle
import datetime as dt
import json 

'''
国家，罪名二个特征项分析
'''

#读取文件
df = pd.read_csv(r"./shwjzf_.csv", header=0, 
				delimiter='\t', index_col=0, dtype='object')

# print(df.head())

# 去重后
df = df.drop_duplicates()
#print(df.shape) # (688, 56)

#把'\N'值替换成NAN值
df[df == r'\N'] = np.nan

#查看是否有全部为空值的字段
# print(df.isnull().all().value_counts()) #False 56  True  1
# print(df.isnull().all()) # hunyinbiandong_hyzk   True

# 去掉全部为空值的字段 hunyinbiandong_hyzk
df = df.drop(['hunyinbiandong_hyzk'], axis=1)
print(df.shape) #(688, 55)

#删除那些国家地区为空值的罪犯信息
df = df.drop(df[df['gjdq'].isnull()].index, axis=0)

# 删除罪名为空的罪犯信息

df = df.drop(df[df['zm'].isnull()].index, axis=0)

#取字段组成新的数据集
df = df[['gjdq', 'zm']]


# 罪名处理，有多个罪名的取第一个值

# 取多重罪名的第一条罪名
zm_lst = []
for i in df['zm']:
		zm_lst.append(i.split(',')[0])

df['zm'] = zm_lst
# 转变数据格式为int型
# df['zm'] = df['zm'].astype('int')

# 保存至当前文件夹csv
df.to_csv('./shzf_gj_zm.csv')


