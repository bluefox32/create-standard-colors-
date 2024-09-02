import numpy as np
import matplotlib.pyplot as plt

def rgb_to_unit_circle(R, G, B):
    """
    RGB値を単位円上の角度に変換
    R -> cosθ, G -> sinθ, B -> 調整係数
    """
    theta = np.arccos(R)  # Rに応じて角度θを計算
    x = np.cos(theta)
    y = np.sin(theta) * G  # Gがsinθのスケールを決定
    z = B  # Bをz軸とする
    
    return x, y, z

def plot_unit_circle_with_rgb(sample_density=100):
    """
    単位円を用いてRGBグラデーションをプロット
    """
    r_values = np.linspace(0, 1, sample_density)
    g_values = np.linspace(0, 1, sample_density)
    b_values = np.linspace(0, 1, sample_density)

    x_coords = []
    y_coords = []
    z_coords = []
    colors = []

    for R in r_values:
        for G in g_values:
            for B in b_values:
                x, y, z = rgb_to_unit_circle(R, G, B)
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)
                colors.append((R, G, B))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # プロット
    ax.scatter(x_coords, y_coords, z_coords, c=colors, marker='o')

    ax.set_xlabel('Cosine')
    ax.set_ylabel('Sine')
    ax.set_zlabel('B value')

    plt.title('RGB Values on Unit Circle')
    plt.show()

# メインの実行
plot_unit_circle_with_rgb()