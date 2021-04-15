import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pylab import *

import matplotlib.pyplot as plt
plt.rc('font',family='Arial')

# Do not need modification #
plt.figure(figsize=(8.3,6))
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.yticks(size = 20)
plt.xticks(size = 20)
tick_params(which='major',width=2,length=8)
tick_params(which='minor',width=1,length=4)
ax=plt.gca()
bwith = 2
ax.spines['bottom'].set_linewidth(bwith)    
ax.spines['top'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)  
ax.spines['right'].set_linewidth(bwith)
# Do not need modification #

# Additional setting
plt.xlabel('Reaction coordinate',{'weight':'normal','size':25},labelpad=12)
plt.ylabel('Free energy(eV)',{'weight':'normal','size':25},labelpad=15)
plt.scatter(np.arange(10),np.arange(10),label='test')

plt.legend(loc='best',prop ={'weight':'normal','size':25},fancybox=False,edgecolor='black')
plt.tight_layout()
plt.savefig('barrier.pdf',dpi=900)
