###
#	Author: Carolina Dunbar
#	Description: Python script that draws bulleye graph.
###

#### Import packages
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from os.path import join as pjoin

def segmentation_plot(ax, data, cmap=None, norm=None):

    linewidth = 2
    data = np.array(data).ravel()
    
    
    
    if norm is None:
        norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max())
        
    theta = np.linspace(0, 2*np.pi, 768)
    r = np.linspace(0.2, 1, 4)
    
    #Make circle borders
    for i in range(r.shape[0]):
        ax.plot(theta, np.repeat(r[i], theta.shape), '-k', lw=linewidth)

    #Lines that seperate segments 1-12
    for i in range(6):
        theta_i = i * 60 * np.pi/180
        ax.plot([theta_i, theta_i], [r[1], 1], '-k', lw=linewidth)

    #Lines that seperate segments 13-16
    for i in range(4):
        theta_i = i * 90 * np.pi/180 - 45*np.pi/180
        ax.plot([theta_i, theta_i], [r[0], r[1]], '-k', lw=linewidth)
        
        
        
    # Fill the segments 1-6
    r0 = r[2:4]
    r0 = np.repeat(r0[:, np.newaxis], 128, axis=1).T
    for i in range(6):
        # First segment start at 60 degrees
        theta0 = theta[i*128:i*128+128] + 60*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((128, 2))*data[i]
        if i == 0:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 1:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 2:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 3:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i ==4:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i ==5:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)

        
    # Fill the segments 7-12
    r0 = r[1:3]
    r0 = np.repeat(r0[:, np.newaxis], 128, axis=1).T
    for i in range(6):
        # First segment start at 60 degrees
        theta0 = theta[i*128:i*128+128] + 60*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((128, 2))*data[i+6]
        if i == 0:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 1:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 2:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 3:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 4:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 5:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)

        
    # Fill the segments 13-16
    r0 = r[0:2]
    r0 = np.repeat(r0[:, np.newaxis], 192, axis=1).T
    for i in range(4):
        # First segment start at 45 degrees
        theta0 = theta[i*192:i*192+192] + 45*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((192, 2))*data[i+12]
        if i == 0:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 1:
             ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 2:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i == 3:
            ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        
        
    # Fill the segments 17
    for i in data == 17:
        r0 = np.array([0, r[0]])
        r0 = np.repeat(r0[:, np.newaxis], theta.size, axis=1).T
        theta0 = np.repeat(theta[:, np.newaxis], 2, axis=1)
        z = np.ones((theta.size, 2))*data[16]
        ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        
        
    ax.set_ylim([0, 1])
    ax.set_yticklabels([])
    ax.set_xticklabels([])

#### Import Segments and Data 
path0 = pjoin('/','Users','Path','To','File')
mydata = np.load(pjoin(path0,'my_data.npy'))

path1 = pjoin('/','Users','Path','To','File')
segm1 = np.loadtxt(pjoin(path1,'LV_Elems+1_1.txt'),dtype='int',delimiter=",")[1:]-1

path2 = pjoin('/','Users','Path','To','File')
segm2 = np.loadtxt(pjoin(path2,'LV_Elems+1_2.txt'),dtype='int',delimiter=",")[1:]-1

path3 = pjoin('/','Users','Path','To','File')
segm3 = np.loadtxt(pjoin(path3,'LV_Elems+1_3.txt'),dtype='int',delimiter=",")[1:]-1

path4 = pjoin('/','Users','Path','To','File')
segm4 = np.loadtxt(pjoin(path4,'LV_Elems+1_4.txt'),dtype='int',delimiter=",")[1:]-1

path5 = pjoin('/','Users','Path','To','File')
segm5 = np.loadtxt(pjoin(path5,'LV_Elems+1_5.txt'),dtype='int',delimiter=",")[1:]-1

path6 = pjoin('/','Users','Path','To','File')
segm6 = np.loadtxt(pjoin(path6,'LV_Elems+1_6.txt'),dtype='int',delimiter=",")[1:]-1

path7 = pjoin('/','Users','Path','To','File')
segm7 = np.loadtxt(pjoin(path7,'LV_Elems+1_7.txt'),dtype='int',delimiter=",")[1:]-1

path8 = pjoin('/','Users','Path','To','File')
segm8 = np.loadtxt(pjoin(path8,'LV_Elems+1_8.txt'),dtype='int',delimiter=",")[1:]-1

path9 = pjoin('/','Users','Path','To','File')
segm9 = np.loadtxt(pjoin(path9,'LV_Elems+1_9.txt'),dtype='int',delimiter=",")[1:]-1

path10 = pjoin('/','Users','Path','To','File')
segm10 = np.loadtxt(pjoin(path10,'LV_Elems+1_10.txt'),dtype='int',delimiter=",")[1:]-1

path11 = pjoin('/','Users','Path','To','File')
segm11 = np.loadtxt(pjoin(path11,'LV_Elems+1_11.txt'),dtype='int',delimiter=",")[1:]-1

path12 = pjoin('/','Users','Path','To','File')
segm12 = np.loadtxt(pjoin(path12,'LV_Elems+1_12.txt'),dtype='int',delimiter=",")[1:]-1

path13 = pjoin('/','Users','Path','To','File')
segm13 = np.loadtxt(pjoin(path13,'LV_Elems+1_13.txt'),dtype='int',delimiter=",")[1:]-1

path14 = pjoin('/','Users','Path','To','File')
segm14 = np.loadtxt(pjoin(path14,'LV_Elems+1_14.txt'),dtype='int',delimiter=",")[1:]-1

path15 = pjoin('/','Users','Path','To','File')
segm15 = np.loadtxt(pjoin(path15,'LV_Elems+1_15.txt'),dtype='int',delimiter=",")[1:]-1

path16 = pjoin('/','Users','Path','To','File')
segm16 = np.loadtxt(pjoin(path16,'LV_Elems+1_16.txt'),dtype='int',delimiter=",")[1:]-1

path17 = pjoin('/','Users','Path','To','File')
segm17 = np.loadtxt(pjoin(path17,'LV_Elems+1_17.txt'),dtype='int',delimiter=",")[1:]-1

####
newdata1 = np.zeros(shape=(len(segm1)))
newdata1 = mydataa[segm1]

newdata2 = np.zeros(shape=(len(segm2)))
newdata2 = mydataa[segm2]

newdata3 = np.zeros(shape=(len(segm3)))
newdata3 = mydataa[segm3]

newdata4 = np.zeros(shape=(len(segm4)))
newdata4 = mydataa[segm4]

newdata5 = np.zeros(shape=(len(segm5)))
newdata5 = mydataa[segm5]

newdata6 = np.zeros(shape=(len(segm6)))
newdata6 = mydataa[segm6]

newdata7 = np.zeros(shape=(len(segm7)))
newdata7 = mydataa[segm7]

newdata8 = np.zeros(shape=(len(segm8)))
newdata8 = mydataa[segm8]

newdata9 = np.zeros(shape=(len(segm9)))
newdata9 = mydataa[segm9]

newdata10 = np.zeros(shape=(len(segm10)))
newdata10 = mydataa[segm10]

newdata11 = np.zeros(shape=(len(segm11)))
newdata11 = mydataa[segm11]

newdata12 = np.zeros(shape=(len(segm12)))
newdata12 = mydataa[segm12]

newdata13 = np.zeros(shape=(len(segm13)))
newdata13 = mydataa[segm13]

newdata14 = np.zeros(shape=(len(segm14)))
newdata14 = mydataa[segm14]

newdata15 = np.zeros(shape=(len(segm15)))
newdata15 = mydataa[segm15]

newdata16 = np.zeros(shape=(len(segm16)))
newdata16 = mydataa[segm16]

newdata17 = np.zeros(shape=(len(segm17)))
newdata17 = mydataa[segm17]

#### Take Average of Each Segment
average1 = np.average(newdata1)
average2 = np.average(newdata2)
average3 = np.average(newdata3)
average4 = np.average(newdata4)
average5 = np.average(newdata5)
average6 = np.average(newdata6)
average7 = np.average(newdata7)
average8 = np.average(newdata8)
average9 = np.average(newdata9)
average10 = np.average(newdata10)
average11 = np.average(newdata11)
average12 = np.average(newdata12)
average13 = np.average(newdata13)
average14 = np.average(newdata14)
average15 = np.average(newdata15)
average16 = np.average(newdata16)
average17 = np.average(newdata17)

#### Round average to desired decimal point
av1 = round(average1,3)
av2 = round(average2,3)
av3 = round(average3,3)
av4 = round(average4,3)
av5 = round(average5,3)
av6 = round(average6,3)
av7 = round(average7,3)
av8 = round(average8,3)
av9 = round(average9,3)
av10 = round(average10,3)
av11 = round(average11,3)
av12 = round(average12,3)
av13 = round(average13,4)
av14 = round(average14,4)
av15 = round(average15,4)
av16 = round(average16,4)
av17 = round(average17,4)


# Sets Data for graph
data = np.array([average1, average2, average3, average4, average5, average6, average7, average8, average9, average10, average11, average12, average13, average14, average15, average16, average17])


# Make a figure and axes with dimensions as desired.
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(projection='polar'))
fig.canvas.set_window_title('LV Volume Reduction Bullseyes')

# Sets location of legend
axl3 = fig.add_axes([0.42, 0.06, 0.2, 0.05])


# Set max and min of color map
cmap = mpl.cm.jet
norm = mpl.colors.Normalize(vmin=average9, vmax=0.962)

# Set Units
cb = mpl.colorbar.ColorbarBase(axl3, cmap=cmap, norm=norm,orientation='horizontal')
cb.set_label('kilopascals (kPa)')

# Set Annotation
ax.annotate(av1, xy=(3.14/1.95, 0.85),textcoords='data', weight='bold',color='white') #1
ax.annotate(av2, xy=(3*3.14/3.5, 0.95),textcoords='data', weight='bold') #2
ax.annotate(av3, xy=(5*3.14/4.35, 0.95),textcoords='data', weight='bold') #3
ax.annotate(av4, xy=((2.94*3.14)/2, 0.87),textcoords='data', weight='bold') #4
ax.annotate(av5, xy=(7*3.14/3.85, 0.8),textcoords='data', weight='bold') #5
ax.annotate(av6, xy=(3.14/5.5, 0.78),textcoords='data', weight='bold') #6
ax.annotate(av7, xy=(3.14/1.9, 0.55),textcoords='data', weight='bold') #7
ax.annotate(av8, xy=(3*3.14/3.5, 0.67),textcoords='data', weight='bold') #8
ax.annotate(av9, xy=(5*3.14/4.4, 0.68),textcoords='data', weight='bold', color='white') #9
ax.annotate(av10, xy=((2.909*3.14)/2, 0.6),textcoords='data', weight='bold') #10
ax.annotate(av11, xy=(7*3.14/3.85, 0.54),textcoords='data', weight='bold') #11
ax.annotate(av12, xy=(3.14/5.5, 0.52),textcoords='data', weight='bold') #12
ax.annotate(av13, xy=(3.14/1.7, 0.3),textcoords='data', weight='bold') #13
ax.annotate(av14, xy=(3.14, 0.425),textcoords='data', weight='bold') #14
ax.annotate(av15, xy=((3*3.14)/2.12, 0.35),textcoords='data', weight='bold',color='white') #15
ax.annotate(av16, xy=(0, 0.24),textcoords='data', weight='bold',color='white') #16
ax.annotate(av17, xy=(3.14, 0.085),textcoords='data', weight='bold') #17

#Call Function
segmentation_plot(ax, data, cmap=cmap, norm=norm)
#Set Graph Title
ax.set_title('LV Volume Reduction Bullseyes')

#Saves Graph
plt.savefig('/Users/Path/To/File/LVseg_Graph.png')

plt.show()
