import cv2
import os
import imutils

#Path to the rooot directory that is ./image
root_directory = "./body"

#Function to rotate images
def rotate_images(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        #Process subdirectories recursively
        if os.path.isdir(file_path):
            #then do recursively
            print("file_path", file_path[-5:])
            if((int(file_path[-5:]) <= 77010) and (int(file_path[-5:]) >= 77000)):             
                rotate_images(file_path)
        elif filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            if (filename.__contains__('-') == False) :                
                rotate_angle = 2
                rotate_range = range(0, 360, rotate_angle)
                print(rotate_range)
                print("directory:", directory)
                image_path = os.path.join(directory, filename)
                original_image = cv2.imread(image_path)
                for index, angle in enumerate(rotate_range):
                    file_name_tup = os.path.splitext(filename)
                    file_name = file_name_tup[0]
                    file_extension = file_name_tup[1]
                    rotated_file_name = file_name+"-"+f"{index}"+file_extension
                    rotated_file_name = os.path.join(directory, rotated_file_name)
                    print("rotated_angle:", angle)
                    rotated_image = imutils.rotate(original_image, angle= angle)
                    #save the rotated image in the same directory
                    cv2.imwrite(rotated_file_name, rotated_image)

#Start processing from the root directory
rotate_images(root_directory)