# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:07:35 2017

@author: gxk19
"""

import matplotlib.pyplot as plt
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel("Grade")
plt.axis([-1,10,0,6])
plt.savefig("2",dpi=600)
plt.show()