# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:53:34 2017

@author: gxk19
"""

import numpy as np
import matplotlib.pyplot as plt

a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')

plt.xlabel('横轴:时间',fontproperties='SimHei',fontsize=25,color='green')
plt.ylabel('纵轴:振幅',fontproperties='SimHei',fontsize=25)
plt.annotate(r'$mu=100$',xy=(2,1),xytext=(3,1.5),
             arrowprops=dict(facecolor='black',shrink=0.1,width=2))

plt.axis([-1,6,-2,2])
plt.grid(True)
plt.savefig('5',dpi=600)
plt.show()