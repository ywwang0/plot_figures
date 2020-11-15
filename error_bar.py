plt.errorbar(x, 
	y, 
	yerr=None, 
	xerr=None, 
	fmt='', 
	ecolor=None, 
	elinewidth=None, 
	capsize=None, 
	capthick=None
)

'''
x,y: 数据点的位置坐标
xerr,yerr: 数据的误差范围
fmt: 数据点的标记样式以及相互之间连接线样式,' ' 'o' ',' '.' 'x' '+' 'v' '^' '<' '>' 's' 'd' 'p'
ecolor: 误差棒的线条颜色
elinewidth: 误差棒的线条粗细
capsize: 误差棒边界横杠的大小
capthick: 误差棒边界横杠的厚度
ms: 数据点的大小
mfc: 数据点的颜色
mec: 数据点边缘的颜色
'''
# 实际例子
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.1,0.5,10) # 生成[0.1,0.5]等间隔的十个数据
y=np.exp(x)

error=x # 误差范围函数
error_range=[error+0.1,error] # 下置信度和上置信度

plt.errorbar(x,y,yerr=error_range,fmt='o:',ecolor='hotpink',
             elinewidth=3,ms=5,mfc='wheat',mec='salmon',capsize=3)
plt.show()
