# 本文件包括使用pandas的标准代码Standard Code（简称sc）
# 导入numpy包
import numpy as np
# 导入pandas包
import pandas as pd

# 基本数据结构Series、DataFrame
# (1)Series
# 调用 pd.Series 函数即可创建 Series, Index与Data必须对应
# s = pd.Series(data, index=index_list)
# e.g.1 使用字典创建
s1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
# e.g.2 使用列表创建
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

print(s1)
print(s2)
# df = pd.read_excel('PATH', header=n, index_col='INDEX_COLUMN')
# header指定列名起始行，pandas可以自动忽略表首的空行
# 无header可以设置header=None,可以人为设置列名
# df.columns = ['name1','name2'……，'nameN']
# index_col可以指定INDEX列

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
