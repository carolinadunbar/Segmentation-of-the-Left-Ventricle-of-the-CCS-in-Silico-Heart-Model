###
#	Author: Joao Soares
#	Description: Python script that extracts planes and normal from paraview.
###


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'


cut_labels=['Clip1','Clip2','Clip3','Clip4']
folder_here='/Users/joaosoaresphd/Google Drive/CCS_heart-final_results/VTKs/cuts/'
filename='cube_2'

file_here=open(folder_here+filename+'.txt','w')
print >> file_here, len(cut_labels)


for label_here in cut_labels:
    clip_here = FindSource(label_here)
    print >> file_here, clip_here.ClipType.Origin[0],clip_here.ClipType.Origin[1],clip_here.ClipType.Origin[2]
    print >> file_here, clip_here.ClipType.Normal[0],clip_here.ClipType.Normal[1],clip_here.ClipType.Normal[2]

file_here.close()




'''
# find source
clip2 = FindSource('Clip2')

# find source
full_meshvtk = FindSource('full_mesh.vtk')

# get active source.
clip4 = GetActiveSource()

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [0.0786199765874474, 0.119570469020371, 0.108876643490853]
clip4.ClipType.Normal = [-0.910772155918562, -0.378447060940249, 0.0946385701010444]

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [0.0786199765874474, 0.119570469020371, 0.108876643490853]
clip4.ClipType.Normal = [-0.910772155918562, -0.378447060940249, 0.0946385701010444]

# find source
clip3 = FindSource('Clip3')

# find source
clip1 = FindSource('Clip1')

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

'''
