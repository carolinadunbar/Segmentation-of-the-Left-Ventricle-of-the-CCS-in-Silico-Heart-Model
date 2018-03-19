##
#	Author: Carolina Dunbar
#	Description: Python script that writes VTK files.
###

#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to Nodes .txt file
path = pjoin('/','Users','Path','To','File')
points=np.loadtxt(pjoin(path,'nodes.txt'),dtype='float',delimiter=",")[:,1:]


## Enter path to Nodes to write VTK file
path2 = pjoin('/','Users','Path','To','File')
cell=np.loadtxt(pjoin(path2,'LV_Nodes_1.txt'),dtype='int',delimiter=" ")

#### Import packages
import os

## Adds 10's infront of cells
cells=np.insert(cell, 0, 10, axis=1)

ncells=len(cells)

## Enter path to VTK file to be written
VTK_here=open('/Users/CarolinaDunbar/Documents/ICES/LV_Segment_1.vtk','w+')

print('# vtk DataFile Version 3.0', file=VTK_here)
print('vtk output', file=VTK_here)
print('ASCII', file=VTK_here)
print('DATASET UNSTRUCTURED_GRID', file=VTK_here)
print('POINTS 80791 float', file=VTK_here)
for i in points:
    print(' '.join(map(str, i)), file=VTK_here)
print('CELLS ' + str(ncells) + ' ' + str(ncells * 11), file=VTK_here)
for x in cells:
    print(' '.join(map(str, x)), file=VTK_here)
print('CELL_TYPES '+str(ncells), file=VTK_here)
for z in range(0,ncells):
    print('24', file=VTK_here)
        
VTK_here.close()
