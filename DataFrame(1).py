# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:37:51 2017

@author: gxk19
"""

import pandas as pd
import numpy as np

d=pd.DataFrame(np.arange(1,12+1).reshape(3,4))

print(d[d>d.median()])