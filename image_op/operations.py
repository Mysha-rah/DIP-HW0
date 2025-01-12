import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
          Perform image flipping along horizontal or vertical direction

          image: the input image to flip
          direction: direction along which to flip

          return: output_image
          """
        #print("hello: merge funtion!")
       #....
        # Flipping Solved
        lenght, width, bgr =image.shape 
        
        output_image = zeros((lenght, width, bgr), dtype=image.dtype)
        for y in range(lenght):
             for x in range(width): 
                if direction =="horizontal":
                    #flip horizontally by copying each row in reverse 
                    output_image[y,x] =image[y, width - x - 1]
                elif direction =="vertical":
                    #flip vertically by copying each column in reverse 
                    output_image[y,x] =image[lenght - y - 1, x]
                    
        return output_image

        #return image

    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """

        # add your code here
        # Please do not change the structure

        #for getting shape of foreground_img
        lenght_counts =foreground.shape[0]
        width_counts =foreground.shape[1]

        #3 is the channels or bgr
        #also output the same foreground_img using zeros
        output_img = zeros((lenght_counts, width_counts, 3))


        #pixel of foreground_img

        for i in range(lenght_counts):
            for j in range(width_counts):
                color_dist = sqrt(sum((foreground[i, j] - target_color) **2))

                if color_dist < threshold:
                    output_img[i, j] =background[i, j]
                else:
                    output_img[i, j] =foreground[i, j]
        
        return  output_img # Currently the input image is returned, please replace this with the color extracted image

   