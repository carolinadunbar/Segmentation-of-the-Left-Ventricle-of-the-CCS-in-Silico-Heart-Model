###
#	Author: Carolina Dunbar
#	Description: Python script that subtracts cells from different planes.
#
#	Caution:
#	Use intersect1d if both elements in planes interesect and setdiff1d if they do not #	intersect and must be subtracted.
###


#### Import packages
import numpy as np
from os.path import join as pjoin

## Enter path to .txt file
path = pjoin('/','Users','Path','To','File','Cells','Cell_Segments')

path2 = pjoin('/','Users','Path','To','File')

## Enter .txt file
c17=np.loadtxt(pjoin(path,'All_Elems_15.txt'),delimiter=",")			#enter elms .txt

an17=np.loadtxt(pjoin(path2,'LV_only.txt'),delimiter=",")-1			#enter nodes .txt

#apex=np.setdiff1d(an17, c17)

##np.count_nonzero(apex)

apex=np.intersect1d(an17,c17)

# Save .txt file

#np.savetxt('/Users/Path/To/File/cells/cells_12_plane_1_2_3_4_5.txt',apex,'%2i',delimiter=' , ') 			#enter name of node segement
np.savetxt('/Users/Path/To/File/cells/Cell_Segments/LV_Elems_17.txt',apex,'%2i',delimiter=' , ') 			#enter name of node segement
