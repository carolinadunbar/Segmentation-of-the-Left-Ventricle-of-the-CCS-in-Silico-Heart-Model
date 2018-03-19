###
#	Author: Carolina Dunbar
#	Description: Python script that adds 10 infront of element list for VTK files.
###

#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to .txt file
path = pjoin('/','Users','Path','To','File','VTK_files')
cells=np.loadtxt(pjoin(path,'LV_Nodes_15.txt'),dtype='int')

## Add 10
a=np.insert(cells, 0, 10, axis=1)

## Enter path to save .txt file
np.savetxt('/Users/Path/To/File/VTK_files/ToWriteVTK/LV_Nodes_1_with_10s.txt',a,'%i')
