from Lib import spatially_filtered, Kernel
from PGM import PGMImage
import random

def distort_image(p, percentage):
    # Percentage of the total pixels
    pixel_percentage = p.n_pixels * percentage

    # Set random percentage of pixels
    # to white or black
    i = 0
    while i < pixel_percentage:
        white_or_black = random.randint(0,1)

        if white_or_black == 1:
            p.pixels[random.randint(0,p.rows)][random.randint(0,p.cols)] = 255
        else:
            p.pixels[random.randint(0,p.rows)][random.randint(0,p.cols)] = 0
        i += 1
    
    return p

def median_filtering(pgm_filename, mask_size):
    p = PGMImage(pgm_filename)
    
    p_1 = distort_image(p, .50)
    p_2 = distort_image(p, .70)


    
def median_averaging(pgm_filename, mask_size):
    p = PGMImage(pgm_filename)
    
    p_1 = distort_image(p, .50)
    p_2 = distort_image(p, .70)

    
    
if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/boat.pgm"):
        for i in (7, 15):
            median_filtering(img, i)
        for j in (7, 15):
            median_averaging(img, j)