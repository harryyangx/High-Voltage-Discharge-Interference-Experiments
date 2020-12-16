import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',  # 设置字体类型
    # "font.size": 10,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

data = pd.read_excel(r'Data.xlsx')
X,Y,Z = data['Order'], data['Number of falling edge trigger'],data['Circuit voltage']

para = np.polyfit(X,Y,3)
p = np.poly1d(para)

fig, ax1 = plt.subplots(figsize=(10, 4.5))  # 使用subplots()创建窗口
# 绘制折线图像1, 标签，线宽
ax1.plot(X,Y,'o',markersize=3)
ax1.plot(X, p(X), c='red', label='FET     ', linewidth=1)
ax2 = ax1.twinx()  # 创建第二个坐标轴
ax2.plot(X, Z, c='blue', label='Voltage', linewidth=1)  # 同上, 'o-'
ax1.legend(loc=1,bbox_to_anchor=[1,1])
plt.grid(True)  # 样式风格：网格型
ax1.set_xlabel('Time (10s)', size=18)
ax1.set_ylabel('FET', size=18)
ax2.set_ylabel('Voltage (v)', size=18)
ax2.legend(loc=1,bbox_to_anchor=[1,0.9])
ax2.annotate('Fitting curve of FET', xy=(1889,10.9), xytext=(1020,7.8),fontsize=16,bbox=dict(boxstyle="sawtooth", fc="0.8"),arrowprops=dict(arrowstyle="->"))
# plt.show()
plt.savefig(r'figure2.jpg',dpi=600)