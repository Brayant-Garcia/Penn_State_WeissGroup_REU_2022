import matplotlib as plt
from matplotlib import pyplot as plt
import numpy as np 
from PIL import Image

#For this File, I don't think the tracking is working as intended; it tries to search for a maxmium value 
#but it isn't a good method of searching for the individual beams. If you want to try and develop a new tracking algorithm,
#try using a library called trackpy
#Information on the Library is linked here: http://soft-matter.github.io/trackpy/v0.5.0/

sample_photo=Image.open("Group_Of_7_Simplified.tiff") #can also input the directory of the photo that you wanna open here
sample_array=np.asarray(sample_photo)

#implementing_reduction_of_camera_photos


print(sample_array.shape)
print(np.amax(sample_array))
(rows,columns)=sample_array.shape
#finding where the maximum points are 
where_max=np.where(sample_array==np.amax(sample_array))
list_max=list(where_max)
max_row=list(where_max[1])
max_column=list(where_max[0])
print("Max Index:", str(max_row),str(max_column))



#looping should go from -99 to 99
#so now its properly working, we can try now and print out the matrix that has this largest intensity: 
#save this copy, and just append it somewhere else along the photo
#copy_target_spot=sample_matrix_array[int(largest_index[0])]


img=plt.imshow(sample_array)
plt.colorbar(img)
plt.xlabel("Horizontal Position (Pixels)")
plt.ylabel("Vertical Position (Pixel)")
plt.title("Intensity Map of Laser, June 20")
plt.savefig("First_Photo_For_Analysis_June_20.jpg")
plt.show() 

#Note; This code isn't working too well, as the the absolute maximum of intensity isn't a good way of tracking where the
#spots are,  if yo
#max _row contains the point which row has the peak, max_colum says where theres a height peak, now that we have those
#let's make a  150x150 square around this peak: 
sorting_space=np.zeros((7,100,100))

#saving the middle spot to the central peak
for selecting_x in range(100):
    for selecting_y in range(100): 
        sorting_space[2][selecting_x][selecting_y]= sample_array[selecting_x+ int(max_column[0]) - 49, selecting_y + int(max_row[0]) -49]

#making 4 little squares to the right of the central peak, only changing in the horizontal, not the vertical:
for shift_right in range(4): 
    for selecting_x in range(100):
        for selecting_y in range(100): 
            sorting_space[3+ shift_right][selecting_x][selecting_y]= sample_array[selecting_x+ int(max_column[0]) - 49, selecting_y + int(max_row[0])+ 100* (shift_right+1) -49]
             #print where we are at 
    
#making 2 squares to the left, same process as above:
for shift_left in range(2): 
    for selecting_x in range(100):
        for selecting_y in range(100): 
            sorting_space[1-shift_left][selecting_x][selecting_y]= sample_array[selecting_x+ int(max_column[0]) - 49,  selecting_y + int(max_row[0]) - 100* (shift_left+1) -49]


#let's now go ahead and check the profiles of each of these figures: going to take a cross section of the figure,
#then plot the horizontal and vertical; let's save the radii of each by saving it in a list

horizontal_radii=np.zeros((7,1))
vertical_radii=np.zeros((7,1))
where_are_we=0

#loop through each of the arrays
for checking_profile in range(7): 
    source_matrix=sorting_space[checking_profile][:][:]

    #now to do the processing here

    row_maxes=source_matrix.sum(axis=1)
    column_maxes=source_matrix.sum(axis=0)


    max_element_along_rows=np.amax(row_maxes)
    max_row=np.where(row_maxes==max_element_along_rows)

    max_element_along_columns=np.amax(column_maxes)
    max_column=np.where(column_maxes==max_element_along_columns)

    print("Highest value among Rows:" , str(max_element_along_rows))
    print("Target Row:" , str(max_row))


    print("Highest value among Columns:" , str(max_element_along_columns))
    print("Target Column:" , str(max_column))

    target_row=int(max_row[0])
    target_section_row=source_matrix[target_row,:]


    #now to do the same for collecting the columns 
    target_column=int(max_column[0])
    target_section_column=np.squeeze(source_matrix[:,max_column])



    sample_x=np.arange(0,100)*9.6 #translating pixel position to physical position
    sample_y=np.arange(0,100)* 9.6


    plt.subplot(1,2,1)
    plt.plot(sample_x, target_section_row,color="green")
    plt.xlabel("Position in Horizontal Direction")
    
    plt.subplot(1,2,2)
    plt.plot(sample_y, target_section_column, color="purple")
    plt.xlabel("Position in Vertical Direction")

    
    plt.show()

    where_are_we+=1


#now to make some plots  
#for subplot, subplot(abc): a is number of rows, b is number of columns,
#c is the linear index of the matrix
plt.subplot(771)
plt.imshow(sorting_space[0][:][:])

plt.subplot(772)
plt.imshow(sorting_space[1][:][:])



plt.subplot(773)
plt.imshow(sorting_space[2][:][:])

plt.subplot(774)
plt.imshow(sorting_space[3][:][:])


plt.subplot(775)
plt.imshow(sorting_space[4][:][:])

plt.subplot(776)
plt.imshow(sorting_space[5][:][:])

plt.subplot(777)
plt.imshow(sorting_space[6][:][:])


plt.show()
