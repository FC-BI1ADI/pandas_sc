# 本文件包括使用pandas的标准代码Standard Code（简称sc）
# 导入numpy模块
import numpy as np
# 导入pandas模块
import pandas as pd

# 导入matplotlib 包
import matplotlib.pyplot as plt
# 解决中文显示问题
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']


# pandas使用NaN（Not a Number）表示数据缺失

# 基本数据结构Series、DataFrame
# (1)Series
# 调用 pd.Series 函数即可创建 Series, Index与Data必须对应
# s = pd.Series(data, index=index_list)
# e.g.1 使用字典创建
s1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
# e.g.2 使用列表创建
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# Series常用属性和方法
# Series.index 返回Series的INDEX列表
# e.g.3 print(s1.index)

# (2)DataFrame
# 调用 pd.DataFrame 函数即可创建 DataFrame
# 创建方法可以有以列的方式和以行的方式
# 方法1：用 Series 字典或字典生成 DataFram（列方式）
# 方法2：用多维数组字典、列表字典生成 DataFram（行方式）

#操作	        句法	            结果
# 选择列	        df[col]	            Series
# 用标签选择行	    df.loc[label]	    Series
# 用整数位置选择行	df.iloc[loc]	    Series
# 行切片	        df[5:10]	        DataFrame
# 用布尔向量选择行	df[bool_vec]	    DataFrame

# df = pd.read_excel('PATH', header=n, index_col='INDEX_COLUMN')
# header指定列名起始行，pandas可以自动忽略表首的空行
# 无header可以设置header=None,可以人为设置列名
# df.columns = ['name1','name2'……，'nameN']
# index_col可以指定INDEX列

df = pd.read_excel('d:/proc/students1.xlsx')
df.plot.bar(x='Name',y=['Age','Score'],title='学生年龄/成绩表')
plt.show()
# df = df.set_index('INDEX_COLUMN')
#
# df.shape
# 返回（行数、列数）元组
# df.columns
# 返回列XX
# df.head(N)
# 返回头N行
# df.tail(N)
# 返回尾N行
