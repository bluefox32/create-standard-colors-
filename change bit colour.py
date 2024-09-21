import numpy as np

def convert_rgb_bit_depth(r, g, b, original_depth=8, target_depth=48):
    """
    RGB値のビット深度を変更する関数
    r, g, b: 入力のRGB値（0〜1の範囲で表現されることを前提）
    original_depth: 元のビット深度（デフォルトは8ビット）
    target_depth: 変更後のビット深度（例：16ビットなど）
    """
    # 最大値を計算 (例えば8ビットなら255、16ビットなら65535)
    original_max_value = (2 ** original_depth) - 1
    target_max_value = (2 ** target_depth) - 1
    
    # RGB値を元のビット深度の最大値からスケーリング
    r_scaled = int(r * target_max_value / original_max_value)
    g_scaled = int(g * target_max_value / original_max_value)
    b_scaled = int(b * target_max_value / original_max_value)
    
    return r_scaled, g_scaled, b_scaled

# 8ビットRGB値を16ビットに変換する例
r, g, b = 255, 128, 64  # 8ビットのRGB値（0〜255）
r_16bit, g_16bit, b_16bit = convert_rgb_bit_depth(r, g, b, original_depth=8, target_depth=48)

print(f"48ビットRGB値: R={r_16bit}, G={g_16bit}, B={b_16bit}")