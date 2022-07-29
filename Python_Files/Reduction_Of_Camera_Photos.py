import numpy as np  
from PIL import Image

sample_photo= Image.open("Group_Of_7_7_13.tiff")
print(sample_photo.format)
print(sample_photo.size)
print(sample_photo.mode)


    ##currently, our photo is saved as 3 2-d matrix, containing where [x,y,0] has red [x,y,1] has green, 
    ## and [x,y,2] has the blue intensity values; what I'm going to do is convert these values into a 
    ##greyscale image, where for a given pixel, we'll use this formula: 
    ## .299R[x,y] + 0.587G[x,y] + .114B[x,y]=Grey[x,y],
sample_photo_matrices=np.asarray(sample_photo)
print(sample_photo_matrices.shape)


    #conversion to greyscale, if the photo is saved as an RBG image instead of already greyscale; uncomment if you need
    # this section
    #  
#greyscale_map=np.zeros((2048,2592)) #image is originally 2048 x 2592, transposed 

##currently, our photo is saved as 3 2-d matrix, containing where [x,y,0] has red [x,y,1] has green, 
    ## and [x,y,2] has the blue intensity values; what I'm going to do is convert these values into a 
    ##greyscale image, where for a given pixel, we'll use this formula: 
    ## .299R[x,y] + 0.587G[x,y] + .114B[x,y]=Grey[x,y],


    #for preparing_x in range(2048):
        #for preparing_y in range (2592): 
        # greyscale_map[preparing_x][preparing_y]=.299*sample_photo_matrices[preparing_x][preparing_y][0] + .587* sample_photo_matrices[preparing_x][preparing_y][1]+ .114*sample_photo_matrices[preparing_x][preparing_y][2]
            

    ##show case the greyscale image
    #grey_photo=Image.fromarray(np.uint8(greyscale_map))
    #grey_photo.show()  

    #it's properly converted! lets now splice it with the other code, to see how it works



duplicate_matrix=np.zeros((2,2))


# The below loop is for downsizing our image, to 1024x1296. How we do this is that we divide our pixels into 4x4 chunks; 
# This chunk takes the average value of the pixels in the little region, and saves the result in a seperate matrix,
#called array_of_sums. array_of_sums is then transformed to be 1024x1296, which is saved as the output.



total_shift_x=1024 
total_shift_y=1296
sum_of_sample=0 
    #array that saves the sum of subgroups 
array_of_sums=[];  

for starting_x in range(0,total_shift_x):
    for starting_y in range(0,total_shift_y): 
        #this generates the result
        for sample_x in range (2): 
            for sample_y in range(2): 
                duplicate_matrix[sample_x][sample_y]=sample_photo_matrices[sample_x+ 2*starting_x][sample_y + 2*starting_y]
            #print(duplicate_matrix) 
            #this is the step where we get our desired matrix, we can do the operations 
        sum_of_sample= np.sum(duplicate_matrix)/(4)       
        array_of_sums.append(sum_of_sample)

    #once the array of sums is generate, we can reshape our array into a matrix         
array_of_sums=np.reshape(array_of_sums,(1024,1296))        
    ##let's print this photo out to see
simple_photo=Image.fromarray(np.uint16(array_of_sums))
simple_photo.show()
file_name_simple="Group_of_7_Simplified.tiff"
simple_photo.save(file_name_simple)
