import numpy as np
import math

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
    return

def smooth_image_gaussian(image, sigma):
    return

if __name__ == "__main__":
    print(make_averaging_filter(3))
    print()
    print(make_averaging_filter(5))
    print()
    print(make_averaging_filter(7))

    '''
    print(make_gaussian_filter(1.4))
    print()
    print(make_gaussian_filter(3))
    '''
    '''
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        for i in (7, 15):
            smooth_image_averaging(img, i)
        for j in (7, 15):
            smooth_image_gaussian(img, j)
    '''
