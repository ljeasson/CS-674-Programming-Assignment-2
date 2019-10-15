from Lib import spatially_filtered, Kernel
from PGM import PGMImage

import numpy as np

average_matrix_7 = Kernel(mask = [ [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1],
                                   [1,1,1,1,1,1,1] ] * (1/7))

average_matrix_15 = Kernel(mask = [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ] * (1/7))

gaussian_matrix_7 = Kernel(mask=[ [1,1,2,2,2,1,1], 
                                  [1,2,2,4,2,2,1], 
                                  [2,2,4,8,4,2,2], 
                                  [2,4,8,16,8,4,2], 
                                  [2,2,4,8,4,2,2], 
                                  [1,2,2,4,2,2,1], 
                                  [1,1,2,2,2,1,1] ])

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
    

def smooth_image_averaging(pgm_filename, sigma):
    p = PGMImage(pgm_filename)
    
    p_average_7 = spatially_filtered(pgm_filename, average_matrix_7)
    p_average_7.save(f"smoothed_averaging-sigma{sigma}-{p.name}")

    p_average_15 = spatially_filtered(pgm_filename, average_matrix_15)
    p_average_15.save(f"smoothed_averaging-sigma{sigma}-{p.name}")
    
def smooth_image_gaussian(pgm_filename, sigma):
    p = PGMImage(pgm_filename)
    p_gaussian = spatially_filtered(pgm_filename, gaussian_matrix_7)
    p_gaussian.save(f"smoothed_gaussian-sigma{sigma}-{p.name}")    


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        for i in (7, 15):
            smooth_image_averaging(img, i)
        for j in (7, 15):
            smooth_image_gaussian(img, j)

'''
img = cv2.imread(image)
blur = cv2.blur(img,(5,5))

img = cv2.imread(image)
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
'''