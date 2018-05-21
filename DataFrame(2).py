# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:47:15 2017

@author: gxk19
"""

import pandas as pd

dt={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([9,8,7],index=['a','b','c'])}

d=pd.DataFrame(dt)

a=pd.DataFrame(d,index=['a','b'],columns=['one'])

d1={'one':[9,4,7,1],'two':[5,6,2,7]}
d1=pd.DataFrame(d1,index=['a','b','c','d'])

print(d1)

print(d)
print(a)