import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_crystal_structure(atom_filename, bond_filename, show_labels=True):
    # 軸の比を初期化
    axis_ratio = [1.0, 1.0, 1.0]

    # 原子データの読み込み
    with open(atom_filename, 'r', encoding='utf-8') as atom_file:
        lines = atom_file.readlines()
        # 軸の比を取得
        axis_ratio = [float(val) for val in lines[0].strip().split('\t')]
        # 原子データを読み込み
        atom_data = [line.strip().split('\t') for line in lines[1:]]

    # 結合データの読み込み
    with open(bond_filename, 'r', encoding='utf-8') as bond_file:
        bond_data = [line.strip().split('\t') for line in bond_file.readlines()]

    # 3Dプロットの設定
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect(axis_ratio)
    ax.axis('off')  # 軸を非表示にする

    # 原子のプロット
    for data in atom_data:
        x, y, z, r, g, b, radius = map(float, data[:7])
        label = str(data[7])  # ラベルを文字列に変換
        ax.scatter(x, y, z, s=radius**2, c=(r, g, b))

        if show_labels:
            ax.text(x, y, z, label)

    # 結合のプロット
    for data in bond_data:
        atom1, atom2, r, g, b, line_width = map(float, data[:6])
        x = [float(atom_data[int(atom1) - 1][0]), float(atom_data[int(atom2) - 1][0])]
        y = [float(atom_data[int(atom1) - 1][1]), float(atom_data[int(atom2) - 1][1])]
        z = [float(atom_data[int(atom1) - 1][2]), float(atom_data[int(atom2) - 1][2])]
        ax.plot(x, y, z, color=(r, g, b), linewidth=line_width)

    # グラフの表示
    plt.show()

# テスト用のファイルパス
atom_filename = 'atom_Y123.txt'
bond_filename = 'bond_Y123.txt'

# 原子構造のプロット
plot_crystal_structure(atom_filename, bond_filename, show_labels=False)
