###
#	Author: Carolina Dunbar
#	Description: Python script that finds centroid of cells using verticies.
#
#	Caution:
#	Does not use all nodes, just vertices (first 4 nodes listed).
###

#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to .txt file
path = pjoin('/','Users','Path','To','File')

path2 = pjoin('/','Users','Path','To','File')

## Enter .txt file
elems=np.loadtxt(pjoin(path,'elems.txt'),dtype='int',delimiter=",")[:,1:5]			#enter elms .txt

nodes=np.loadtxt(pjoin(path2,'nodes.txt'),delimiter=",")[:,1:4]			#enter nodes .txt

cell_vert=elems-1

cent=np.zeros(shape=(len(cell_vert),3))

# Get coordinates of verticies
for i in range(len(cell_vert)):
    cent[i]=(nodes[cell_vert[i][0]]+nodes[cell_vert[i][1]]+nodes[cell_vert[i][2]]+nodes[cell_vert[i][3]])/4 
    
    
#### Enter origin of plane
o = np.array([0.0858948193821, 0.10581589403, 0.11301537174])

#### Enter normal
plane_norm = np.array([0, 0, 1])

# Subtract point from origin
node_vect = (cent-o)

decision=node_vect.dot(plane_norm)

#(a>0)is a booelan which is 0 for false and 1 for true, nonzero fetches indeces of the non zero elements of the array 
labels=(decision>=0.0).nonzero() 


# Save .txt file
np.savetxt('/Users/Path/To/File/Cells/Cell_Segments/All_Elems_17.txt',label,'%i',delimiter=',') 			#enter name of node segement
