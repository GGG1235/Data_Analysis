# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:13:34 2017

@author: gxk19
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu,sigma=100,20
a=np.random.normal(mu,sigma,size=100)

plt.hist(a,50,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
plt.title('Histogram')

plt.savefig('7',dpi=600)
plt.show()
