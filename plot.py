import numpy as np
from bin import Bin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from constants import *

class Plot:
    def data(self,o, size=(1,1,1)):
        X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
            [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
            [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
            [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
            [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
            [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
        X = np.array(X).astype(float)
        for i in range(3):
            X[:,:,i] *= size[i]
        X += np.array(o)
        return X

    def plot(self,positions,sizes=None,colors=None, **kwargs):
        if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
        if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
        g = []
        for p,s,c in zip(positions,sizes,colors):
            g.append(self.data(p, size=s) )
        return Poly3DCollection(np.concatenate(g),facecolors=np.repeat(colors,6), **kwargs)
        
    def draw(self,bin:Bin):
        bdx,bdy,bdz = bin.dimension
        positions:list[int] = [[0,0,0]]
        sizes = [[bdx,bdy,bdz]]
        list_colors = ["limegreen"]
        list_name = ["Box"]

        for item in bin.items:
            positions.append(item.position)
            sizes.append(item.get_dimension())
            list_colors.append(item.color)
            list_name.append(item.name)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        pc = self.plot(positions,sizes,colors=list_colors, edgecolor="k",alpha = 0.25,)
        ax.add_collection3d(pc)    

        
        ax.set_xlim([0,MAX_DIMENSION[0]])
        ax.set_ylim([0,MAX_DIMENSION[1]])
        ax.set_zlim([0,MAX_DIMENSION[2]])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(bin.size + " " + str(bin.dimension))
        plt.show()