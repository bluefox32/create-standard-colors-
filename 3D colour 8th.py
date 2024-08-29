import numpy as np
import matplotlib.pyplot as plt

# 解像度の設定
resolution = 50000  # ドットの数を増やす

# ランダムな半径と角度を生成
r = np.sqrt(np.random.rand(resolution))
theta = np.random.rand(resolution) * 2 * np.pi

# カートesian座標に変換
X = r * np.cos(theta)
Y = r * np.sin(theta)

# 色成分に対応する色を生成
colors = np.zeros((resolution, 3))
colors[:, 0] = r  # Red channel
colors[:, 1] = np.abs(np.sin(theta))  # Green channel
colors[:, 2] = np.abs(np.cos(theta))  # Blue channel

# ドットサイズを設定
dot_size = 1  # これを調整してドットを大きくします

# プロットを作成
plt.figure(figsize=(6, 6))
plt.scatter(X, Y, c=colors, s=dot_size, edgecolor='none')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Color Gradient on a Circular Area')
plt.axis('equal')  # 円形を保つために軸を等しく設定
plt.show()