# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:59:19 2017

@author: gxk19
"""

import matplotlib.pyplot as plt

labels='Frogs','Hogs','Dogs','Logs'
sizes=[15,30,45,10]
explode=(0,0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.savefig('6',dpi=600)

plt.show()