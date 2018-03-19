###
#	Author: Carolina Dunbar
#	Description: Python script that gives points from cell number.
###

#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to .txt file
path = pjoin('/','Users','Path','To','File','Cells','Cell_Segments')

path2 = pjoin('/','Users','Path','To','File_Segments')

## Enter .txt file
cseg=np.loadtxt(pjoin(path,'LV_Elems_15.txt'),dtype='int',delimiter=" , ")+1 			#enter node segement .txt

elementlist=np.loadtxt(pjoin(path2,'elems.txt'),dtype='int',delimiter=",")
np.sort(cseg)

# Searches where cell are in elems list
elementl = np.searchsorted(cseg,elementlist[:,0])         
elementl[elementl==cseg.size] = 0
elements = (elementlist[cseg[elementl] == elementlist[:,0]])[:,1:]-1

np.savetxt('/Users/Path/To/Files/VTK_files/LV_Nodes_1.txt',elements,'%i')	#enter name of node segement
