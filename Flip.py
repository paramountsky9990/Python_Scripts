import os
import cv2

directory = ''

for file in os.listdir(directory):
    img = cv2.imread(directory + file)
    horizontal_img = cv2.flip( img, 0 )

    #saving now
    cv2.imwrite(file + '_flip' + '.jpg', horizontal_img)
