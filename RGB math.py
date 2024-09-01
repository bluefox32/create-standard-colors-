import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rgb_to_spherical(r, g, b):
    """
    RGB値 (r, g, b) を球面座標 (r, theta, phi) に変換する関数
    """
    norm = np.sqrt(r**2 + g**2 + b**2)
    norm = norm if norm != 0 else 1  # ノルムがゼロの場合は1にする
    r = norm
    theta = np.arccos(b / norm)
    phi = np.arctan2(g, r)
    return r, theta, phi

def spherical_to_cartesian(r, theta, phi):
    """
    球面座標 (r, theta, phi) を直交座標 (x, y, z) に変換する関数
    """
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

def generate_rgb_colors(bit_depth=48, sample_density=50):
    """
    RGB空間の全ての色を生成し、ビット深度とサンプル密度を調整する関数
    """
    max_value = 2**bit_depth - 1
    r = np.linspace(0, max_value, sample_density) / max_value  # R軸のサンプル
    g = np.linspace(0, max_value, sample_density) / max_value  # G軸のサンプル
    b = np.linspace(0, max_value, sample_density) / max_value  # B軸のサンプル

    cartesian_coords = []
    for ri in r:
        for gi in g:
            for bi in b:
                norm = np.sqrt(ri**2 + gi**2 + bi**2)
                if norm != 0:
                    spherical = rgb_to_spherical(ri, gi, bi)
                    cartesian = spherical_to_cartesian(*spherical)
                    cartesian_coords.append((cartesian, (ri, gi, bi)))
    
    return np.array([c[0] for c in cartesian_coords]), np.array([c[1] for c in cartesian_coords])

def plot_rgb_gradient(bit_depth=8, sample_density=10):
    """
    RGBグラデーションを球面座標系に基づいて三次元空間にプロットする関数
    """
    # RGB色の生成
    cartesian_coords, rgb_colors = generate_rgb_colors(bit_depth, sample_density)

    # 三次元プロットの作成
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # RGB値を三次元空間の座標に変換しプロット
    scatter = ax.scatter(cartesian_coords[:, 0], cartesian_coords[:, 1], cartesian_coords[:, 2], 
                         c=rgb_colors, cmap='viridis', s=5, edgecolors='w')  # ノルムで色をスケーリング
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # 軸の範囲を設定
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    
    # カラーバーを表示
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('RGB values')
    
    # タイトルを設定
    ax.set_title(f'RGB Color Gradient in Spherical Coordinates\nBit Depth: {bit_depth}, Sample Density: {sample_density}')

    plt.show()

def main():
    # RGBグラデーションのプロット（ビット深度8、サンプル密度10）
    plot_rgb_gradient(bit_depth=48, sample_density=50)

if __name__ == "__main__":
    main()