import pandas as pd
import numpy as np
import math
from bin import Bin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
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
        x = bin.dimension[0] 
        y = bin.dimension[1] 
        z = bin.dimension[2] 
        # x = chromosome.max_dimension[0] - chromosome.position[0]
        # y = chromosome.max_dimension[1] - chromosome.position[1]
        # z = chromosome.max_dimension[2] - chromosome.position[2]

        positions:list[int] = [[0,0,0]]
        # pcx,pcy,pcz = chromosome.position
        sizes = [[bdx,bdy,bdz]]
        list_colors = ["limegreen"]

        for item in bin.items:
            positions.append(item.position)
            sizes.append(item.get_dimension())
            list_colors.append("crimson")

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # ax.set_aspect('auto')
        # print(list_colors)
        # for p in positions:
        #     p[0] -= pcx
        #     p[1] -= pcy
        #     p[2] -= pcz
        # print(positions)

        pc = self.plot(positions,sizes,colors=list_colors, edgecolor="k",alpha = 0.25)
        ax.add_collection3d(pc)    

        box = bin
        ax.set_xlim([0,MAX_DIMENSION[0]])
        ax.set_ylim([0,MAX_DIMENSION[1]])
        ax.set_zlim([0,MAX_DIMENSION[2]])
        # ax.set_xlim([0,box.dimension[0]])
        # ax.set_ylim([0,box.dimension[1]])
        # ax.set_zlim([0,box.dimension[2]])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(box.size + " " + str(box.dimension))
        
        plt.show()

    # def testFn(self,bestChromosome,title:str):
    #     genCount = list(range(1,MAX_GENERATION+1))
    #     # Data = {'Generation': genCount, 'Fitness Value': bestChromosome}
    #     # df = pd.DataFrame(Data,columns=['Generation','Fitness Value'])
    #     # plt.plot(df['Generation'], df['Fitness Value'], color='red', marker='.',markersize = 5)
    #     # plt.title('Fitness Value progress', fontsize=14)
    #     # plt.xlabel('Fitness Value', fontsize=14)
    #     # plt.ylabel('Generation', fontsize=14)
    #     # plt.grid(True)
    #     plt.figure(figsize=(20, 10))
    #     plot1 = plt.subplot2grid((1, 1), (0, 0),rowspan = 2, colspan=1)
    #     plot1.plot(genCount, bestChromosome)
    #     for g, c in zip(genCount,bestChromosome):
    #         plot1.annotate(c, (g,c))
    #     plot1.set_title(title)
    #     plt.show()
    
    # def plotFV(self,chromosomes:list[Chromosome]):
    #     genCount = list(range(1,MAX_GENERATION+1))
    #     plt.figure(figsize=(20, 10))
    #     plot1 = plt.subplot2grid((1, 1), (0, 0),rowspan = 2, colspan=1)
    #     fv = []
    #     box = []
    #     for chromosome in chromosomes:
    #         fv.append(chromosome.fitness_value)
    #         box.append(chromosome.box.size)
    #     plot1.plot(genCount, fv)
    #     for g, c,box in zip(genCount,fv,box):
    #         plot1.annotate(box, (g,c))
    #     plot1.set_title("Best Chromosome in each generation")
    #     plt.show()
