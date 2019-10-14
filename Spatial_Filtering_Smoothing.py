from PGM import PGMImage
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

gaussian_matrix_7 = [ [1,1,2,2,2,1,1], 
                      [1,2,2,4,2,2,1], 
                      [2,2,4,8,4,2,2], 
                      [2,4,8,16,8,4,2], 
                      [2,2,4,8,4,2,2], 
                      [1,2,2,4,2,2,1], 
                      [1,1,2,2,2,1,1] ] 

def make_averaging_filter(size):
    matrix = np.ones((size,size), dtype=float)
    avg_matrix = (1/size) * matrix
    return avg_matrix

def make_gaussian_filter(sigma):
    x, y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
    d = np.sqrt(pow(x,2) + pow(y,2))
    mu = 0.0
    gaussian_matrix = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
    return gaussian_matrix
    

def smooth_image_averaging(image, sigma):
    img = cv2.imread(image)
    blur = cv2.blur(img,(5,5))
    
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

def smooth_image_gaussian(image, sigma):
    img = cv2.imread(image)
    blur = cv2.GaussianBlur(img,(5,5),0)
    
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        for i in (7, 15):
            smooth_image_averaging(img, i)
        for j in (7, 15):
            smooth_image_gaussian(img, j)