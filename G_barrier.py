import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pylab import *

# Do not need modification #
plt.figure(figsize=(8.3,6))
label_font = {'family':'Arial','weight':'normal','size':26}
legend_font = {'family':'Arial','weight':'normal','size':20}
plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内
plt.yticks(fontproperties = 'Arial', size = 25)
plt.xticks(fontproperties = 'Arial', size = 25)
plt.xlabel('Reaction coordinate',label_font)
plt.ylabel('Free energy(eV)',label_font)
tick_params(which='major',width=3,length=8)
ax=plt.gca()
bwith = 3
ax.spines['bottom'].set_linewidth(bwith)    
ax.spines['top'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)  
ax.spines['right'].set_linewidth(bwith)
plt.xticks([])
plt.xlim([-1.1,1.1])
plt.hlines(0,-5,5)
plt.hlines(0,-1,-.6,lw=4)
plt.hlines(0,.6,1,lw=4)
# Do not need modification #

plt.ylim([-.2,1.4])

# barriers = [0.279,1.15,0.174]
barriers = {'black':0.279,'green':0.174,'blue':1.15}
plt.text(-1,0.03,'$\mathregular{H^{+}+e^{-}}$',fontsize=22)
plt.text(.68,0.03,'$\mathregular{1/2H^{2}}$',fontsize=22)
plt.text(0,1.15+0.03,'$\mathregular{H{*}}$',fontsize=22,horizontalalignment="center")

for (c,barrier) in barriers.items():
    plt.hlines(barrier,-0.15,.15,lw=4,color = c)
    plt.plot([-.6,-0.15],[0,barrier],color = c)
    plt.plot([0.15,.6],[barrier,0],color = c)

plt.hlines(1.15,-0.15,.15,lw=4,color='blue')
    
# plt.legend(loc=[0.22,0.03],prop =legend_font,fancybox=False,edgecolor='black')
plt.tight_layout()
plt.savefig('barrier.pdf',dpi=300)
