# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:31:21 2017

@author: gxk19
"""

import matplotlib.pyplot as plt
import numpy as np

a=np.arange(10)

plt.ylabel('y')
plt.xlabel('x')
plt.title("Grade")

plt.plot(a,a*1,'go-',a,a*2,'rx',a,a*3,'*',a,a*4,'b-.')
plt.savefig("4",dpi=600)
plt.show()