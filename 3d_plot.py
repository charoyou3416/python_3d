import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import streamlit as st

def main():

    def read_atom_data(atom_file):
        atom_positions = []
        atom_colors = []
        atom_radii = []
        atom_labels = []
    
        lines = atom_file.readlines()
        axis_ratio = [float(val) for val in lines[0].decode().strip().split('\t')]
        atom_data = [line.decode().strip().split('\t') for line in lines[1:]]
        return atom_data, axis_ratio
    
    def read_bond_data(bond_file):
        bond_data = [line.decode().strip().split('\t') for line in bond_file.readlines()]
        return bond_data
    
    def plot_crystal_structure(atom_data, bond_data, show_labels=True, axis_ratio=[1.0, 1.0, 1.0]):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_box_aspect(axis_ratio)
        ax.axis('off')
    
        for data in atom_data:
            x, y, z, r, g, b, radius = map(float, data[:7])
            label = str(data[7])
            ax.scatter(x, y, z, s=radius**2, c=(r, g, b))

            if show_labels:
                ax.text(x, y, z, label)
    
        for data in bond_data:
            atom1, atom2, r, g, b, line_width = map(float, data[:6])
            x = [float(atom_data[int(atom1) - 1][0]), float(atom_data[int(atom2) - 1][0])]
            y = [float(atom_data[int(atom1) - 1][1]), float(atom_data[int(atom2) - 1][1])]
            z = [float(atom_data[int(atom1) - 1][2]), float(atom_data[int(atom2) - 1][2])]
            ax.plot(x, y, z, c=(r, g, b), linewidth=line_width)
    
        return fig
    
    st.title('Crystal Structure Plotting')
    
    atom_file = st.file_uploader('Upload atom data file', type=['txt'])
    bond_file = st.file_uploader('Upload bond data file', type=['txt'])
    
    if atom_file and bond_file:
        atom_data, axis_ratio = read_atom_data(atom_file)
        bond_data = read_bond_data(bond_file)
        show_labels = st.checkbox('Show atom labels')
    
        fig = plot_crystal_structure(atom_data, bond_data, show_labels, axis_ratio)
        st.pyplot(fig)
    else:
        st.info('Please upload the data files.')
        
if __name__ == "__main__":
    main()
