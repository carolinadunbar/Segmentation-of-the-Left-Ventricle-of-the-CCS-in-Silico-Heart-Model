# Myocardium Left Ventricle Segmentation of the CCS in Silico Heart Model



This summer I worked on the 17-segment segmentation of Left Ventricle
of the CCS in Silico Heart Model. This paper will serve as a documentation of the methodology
and thought process that went into making the segmentations as well as the bullseye plot.
I began with the 3-Dimensional original mesh of the full heart model which is constructed from 80,791 points forming 55,241 tetrahedral shaped cells. The cells, points and elements are written as a Visualization Toolkit (VTK) file which is then read and interpreted by Paraview to obtain the 3-Dimensional original mesh of the heart. The cells that make up the original mesh contain 10 points each: 4 points that make up the vertices as well as 6 points at the midpoints between vertices.
To obtain the segmented model I first applied cut filters to the original mesh using planes orthogonal to the long axis as well as planes along the long axis which were bounded by specific anatomical structures to each segment. The original mesh was segmented into 17- segments to make the model since this segmentation number best fits anatomic data. The segments are also 35% Basal, 35% Mid-Cavity and 30% for the Apical and Apical Cap to be closest to the true mass-segment ratio. After applying the cut filter on Paraview, I saved the states of each individual segment with the applied cut segments and then ran the script “extract_planes.py” on Paraview to extract a list for each segment containing all of the planes and the normal to the planes that make up each segment. From the lists created I Imputed the Normal and Origin into “Checking_Segmentations.py” to obtain all of the elements bounded by the planes for a specific segment. Then I ran “Subtracting_Cell_Segments.py” for all of the elements bounded by the planes to find the elements that are intersected by all of the planes. I then I ran “Element_to_Nodes.py” which returned all of the nodes of the elements within each segment. Then, I ran “Adding_10_to_Cells.py” to add a 10 in front of each row of cells to be written into the VTK file. I then ran “Writing_VTK_files.py” to write the VTK file for each segment.
To make the bullseye plot I ran “Bullseye Data Graph” which drew a polar graph of the 17-segmentation model. This script checked to see where individual data points where located in the segmentation model and then averaged the data for each segment and displayed this average on that segment as well as filled each segment based on a color map.
 
Scripts:

    • extract_planes.py :
        Extracted the origin and normal from the cut filters applied on Paraview.

    • Checking_Segmentations.py :
        You input the origin and normal and it gives the elements above the plane. This was repeated for all the planes. For example, if there were 4 planes being checked for segment 17, you would get Segment_17_1_4.txt, Segment_17_2_4.txt, Segment_17_3_4.txt and Segment_17_4_4.txt.

    • Subtracting_Cell_Segments.py :
        You input each list of elements you get from “checking_segmentations.py” and it finds the elements intersected by all planes to give the list of elements in each segmentation. For example, you would first plug in Segment_17_1_4.txt and Segment_17_2_4.txt and it would give you Segment_17_1_2_4.txt. You would then check Segment_17_1_2_4.txt and Segment_17_3_4.txt and get Segment_17_1_2_3_4.txt. Then check Segment_17_1_2_3_4.txt and Segment_17_1_4.txt to finally obtain Elements_17.txt.

    • Element_to_Nodes.py :
        You input the specific element list for each segment and it returns the nodes for the elements in that segment.

    • Adding_10_to_Cells.py :
        You input the nodes list for each segment and it adds a 10 to the beginning of every row for the VTK file to be written.

    • Writing_VTK_files.py :
        You input the text file with the nodes with the 10’s in front of them and it writes the VTK file for each segment with the number of points, points, number of cells, cells, number of cell types and cell types(24’s).

    • Bullseye Data Graph.py :
        This script drew a polar graph with segment 17 in the middle, segment 16, 15, 14 and 13 all at 90 degree angles and segments 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 and 1 at 90 degrees. Then found where data points were in each individual segment and averaged the data points in each segment and displayed this average on the segment as well as filled each segment in accordance to the data and color map.
