import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ビット深度を設定 (例: 8ビット)
bit_depth = 48
max_value = 2**bit_depth - 1

# sRGBのガンマ補正を適用する関数
def apply_srgb_gamma(color):
    return np.where(color <= 0.0031308,
                    12.92 * color,
                    1.055 * (color ** (1.0 / 2.4)) - 0.055)

# グラデーションを生成するための解像度を設定
resolution = 100  # 解像度を上げる

# 3D空間上のグリッドを生成
x = np.linspace(0, 1, resolution)  # 0から1に正規化
y = np.linspace(0, 1, resolution)  # 0から1に正規化
z = np.linspace(0, 1, resolution)  # 0から1に正規化
a = np.linspace(0, 1, resolution)  # アルファ値を0から1まで変化させる

# 3D座標をお椀型に変形
def transform_to_bowl(x, y, z):
    x, y, z = np.meshgrid(x, y, z, indexing='ij')  # 各軸に対してメッシュグリッドを生成
    r = np.sqrt(x**2 + y**2)  # 半径の計算
    theta = np.arctan2(y, x)  # 極座標の角度
    z_bowl = np.sin(np.pi * r)  # お椀型に変形
    return r * np.cos(theta), r * np.sin(theta), z_bowl

# 座標を変形
x_trans, y_trans, z_trans = transform_to_bowl(x, y, z)

# 色の成分にガンマ補正を適用
x_trans_srgb = apply_srgb_gamma(x_trans)
y_trans_srgb = apply_srgb_gamma(y_trans)
z_trans_srgb = apply_srgb_gamma(z_trans)

# RGB成分を0-1にクリップ
x_trans_srgb = np.clip(x_trans_srgb, 0, 1)
y_trans_srgb = np.clip(y_trans_srgb, 0, 1)
z_trans_srgb = np.clip(z_trans_srgb, 0, 1)

# 3Dプロットを作成
fig = plt.figure(figsize=(18, 6))

# 三次元プロット
ax = fig.add_subplot(131, projection='3d')
ax.set_facecolor((0.1, 0.1, 0.1))  # 背景色をダークグレーに設定

x_flat = x_trans_srgb.flatten()
y_flat = y_trans_srgb.flatten()
z_flat = z_trans_srgb.flatten()
colors = np.stack((x_flat, y_flat, z_flat), axis=-1)  # RGB 各成分の配列を作成

ax.scatter(x_flat, y_flat, z_flat, c=colors, s=5, alpha=0.7)
ax.set_xlabel('sRGB Red')
ax.set_ylabel('sRGB Green')
ax.set_zlabel('sRGB Blue')
ax.grid(True)

# XY平面への投影（XZ平面のグリーン成分）
ax2 = fig.add_subplot(132)
ax2.scatter(x_flat, y_flat, c=colors, s=5, alpha=0.7)
ax2.set_xlabel('sRGB Red')
ax2.set_ylabel('sRGB Green')
ax2.grid(True)

# XZ平面への投影（YZ平面のグリーン成分）
ax3 = fig.add_subplot(133)
ax3.scatter(x_flat, z_flat, c=colors, s=5, alpha=0.7)
ax3.set_xlabel('sRGB Red')
ax3.set_ylabel('sRGB Blue')
ax3.grid(True)

plt.show()