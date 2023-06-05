import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_atom_data(atom_filename):
    atom_positions = []
    atom_colors = []
    atom_radii = []
    atom_labels = []

    with open(atom_filename, 'r', encoding='utf-8') as file:
        # 軸の比を読み取る
        axis_ratio_line = file.readline()
        axis_ratio = [float(value) for value in axis_ratio_line.split('\t')]

        for line in file:
            values = line.split('\t')
            position = [float(values[0]), float(values[1]), float(values[2])]
            color = [float(values[3]), float(values[4]), float(values[5])]
            radius = float(values[6])
            label = values[7].strip()
            atom_positions.append(position)
            atom_colors.append(color)
            atom_radii.append(radius)
            atom_labels.append(label)

    return np.array(atom_positions), np.array(atom_colors), np.array(atom_radii), atom_labels, axis_ratio

def read_bond_data(bond_filename):
    bond_indices = []
    bond_colors = []
    bond_thicknesses = []

    with open(bond_filename, 'r') as file:
        for line in file:
            values = line.split('\t')
            index1 = int(values[0])
            index2 = int(values[1])
            color = [float(values[2]), float(values[3]), float(values[4])]
            thickness = float(values[5])
            bond_indices.append([index1, index2])
            bond_colors.append(color)
            bond_thicknesses.append(thickness)

    return bond_indices, np.array(bond_colors), np.array(bond_thicknesses)

def plot_crystal_structure(atom_positions, atom_colors, atom_radii, atom_labels, bond_indices, bond_colors, bond_thicknesses, show_labels=True, axis_ratio=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 視点を調整
    ax.view_init(elev=30, azim=45)

    # 原子の位置、色、半径をプロット
    ax.scatter(atom_positions[:, 0], atom_positions[:, 1], atom_positions[:, 2],
               c=atom_colors, s=atom_radii, alpha=1.0)  # 透明度を設定

    # 光源の方向を調整
    ax.azim = 45

    # 原子ラベルを表示
    if show_labels:
        for i, label in enumerate(atom_labels):
            ax.text(atom_positions[i, 0], atom_positions[i, 1], atom_positions[i, 2],
                    label, color='k')

    # 原子間の線を引く
    for i, indices in enumerate(bond_indices):
        atom1 = atom_positions[indices[0]]
        atom2 = atom_positions[indices[1]]
        color = bond_colors[i] if i < len(bond_colors) else 'k'
        thickness = bond_thicknesses[i] if i < len(bond_thicknesses) else 1.0
        ax.plot([atom1[0], atom2[0]], [atom1[1], atom2[1]], [atom1[2], atom2[2]], color=color, linewidth=thickness)

    # 軸と軸ラベルを非表示にする
    ax.set_axis_off()

    # 軸の比を調整
    if axis_ratio is not None:
        ax.set_box_aspect(axis_ratio)

    # 表示
    plt.show()

# 原子データのテキストファイルと結合データのテキストファイルを指定
atom_filename = 'atom_Y124.txt'
bond_filename = 'bond_Y124.txt'

# テキストファイルから原子データと結合データを読み取る
atom_positions, atom_colors, atom_radii, atom_labels, axis_ratio = read_atom_data(atom_filename)
bond_indices, bond_colors, bond_thicknesses = read_bond_data(bond_filename)

# ラベルの表示を選択
show_labels = False

# 軸の比を指定
axis_ratio = axis_ratio

# 結晶構造をプロット
plot_crystal_structure(atom_positions, atom_colors, atom_radii, atom_labels, bond_indices, bond_colors, bond_thicknesses, show_labels, axis_ratio)
