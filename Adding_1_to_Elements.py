###
#	Author: Carolina Dunbar
#	Description: Python script that that adds 1 to all elements and saves as .txt file.
###

#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to .txt file
path = pjoin('/','Users','Path','Path','Segmentation','Cells','Cell_Segments') #enter path to Cell_Segments
elem=np.loadtxt(pjoin(path,'LV_Elems_17.txt'),dtype='int',delimiter=",")

## Add 1
elems = elem +1

## Enter path to save .txt file
np.savetxt('path/NameOfNodeSegment',elems,'%2i',delimiter=' , ')  #enter path & name of node segement

## To check shapes
print np.count_nonzero(elems)
print len(elems)
elems.shape
