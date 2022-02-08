import cv2
import numpy as np

original = cv2.imread('/home/pi/image.png')

def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
display(original, 'original')
