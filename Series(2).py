# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:23:14 2017

@author: gxk19
"""

import pandas as pd
import numpy as np

a=pd.Series([4,4,7],['c','d','e']).astype(np.int64)
b=pd.Series([9,8,7,6],['a','b','c','d']).astype(np.int64)
c=a+b
print(c.drop(['a','b','e']))
print(b.add(a,fill_value=0)-10)
print(c)
print(c-10==1)