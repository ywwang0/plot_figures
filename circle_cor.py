"""
The code to plot a correlation(PCC or MIC) matrix
Author: Yaowei Wang
Data: 2020-12-22
To be optimised: mask upper right cornor, nake the code is a class,如何写函数中的true或者false？
"""

import pandas as pd
from pylab import *

# 读取相关系数矩阵和特征符号
df = pd.read_csv('pccdata.csv')
features = df.columns.to_list()
n = len(features)
z = np.array(df)

# 画图设置
plt.figure(figsize=(12,10)) 
bwith = 3
plt.ylim([-.5,len(features)-.5])
plt.xlim([-.5,len(features)-.5])
ax=plt.gca()
ax.spines['bottom'].set_linewidth(bwith)    
ax.spines['top'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)  
ax.spines['right'].set_linewidth(bwith)
plt.xticks([i for i in range(len(features))] , features, rotation=0,size = 12)
plt.yticks([i for i in range(len(features))] , features[::-1], rotation=0,size = 12)
cm = plt.cm.RdBu

# 建立x，y坐标矩阵，注意scatter如果不是按照array输出会报错
x_pos = []
y_pos_temp = []
for i in range(n-1,-1,-1):
    x_pos.append([i]*n)
for i in range(n):    
    y_pos_temp.append(i)
y_pos  = []
for i in range(n):
    y_pos.append(y_pos_temp)

# 画散点图和分隔线
plt.scatter(x_pos,y_pos,s=abs(z)*780,c=z,vmin=-1,vmax=1,cmap = cm)
for i in range(n):
    plt.vlines(i+.5, -1, n,lw=.5,color='grey',alpha=0.6)
    plt.hlines(i+.5, -1, n,lw=.5,color='grey',alpha=0.6)
# 保存图片
plt.colorbar()
plt.tight_layout()
plt.savefig('circlepcc.pdf',dpi = 800)
