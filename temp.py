import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.random.randn(1000)
y = np.random.randn(1000)

# 创建二维直方图(即密度图)
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# 绘制云图
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot')
plt.colorbar()
plt.title('2D Density Cloud Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()