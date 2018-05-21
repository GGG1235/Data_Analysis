# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:40:41 2017

@author: gxk19
"""

import pandas as pd
import numpy as np

arr=[chr(i) for i in range(ord('a'),ord('j')+1)]
d=pd.Series(range(1,10+1),index=arr).astype(np.int64)
d.name="Series"
d.index.name='abc'
'''
print('k' in d)

'''
print(d[d%5==0])
'''
print(d[['a','c','j']])

print(d.cumsum())
'''