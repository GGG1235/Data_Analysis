# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:03:59 2017

@author: gxk19
"""

import pandas as pd

d1={'城市':['北京','上海','广州','深圳','沈阳'],
    '环比':[101.5,101.2,101.3,102.0,100.1],
    '同比':[120.7,127.3,119.4,140.9,101.4],
    '定基':[121.4,127.8,120.0,145.5,101.6]
    }

d=pd.DataFrame(d1,index=['c1','c2','c3','c4','c5'])
d.name='2016年7月部分大中城市新建住宅价格指数'
d=d.reindex(index=['c5','c4','c3','c2','c1'])

print(d.drop('c5'))
print(d.drop('环比',axis=1))
print(d)
