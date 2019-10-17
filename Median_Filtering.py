from Lib import median_filtered, averaging_filtered, Kernel
from PGM import PGMImage
import random

def distort_image(p, percentage):
    # Percentage of the total pixels
    pixel_percentage = p.n_pixels * percentage

    # Set random percentage of pixels
    # to white or black
    pix = []
    for row in p.pixels:
        pix.append([i for i in row])
    
    i = 0
    while i < pixel_percentage:
        white_or_black = random.randint(0,1)
        rand_row = random.randint(0,p.rows)
        rand_col = random.randint(0,p.cols)

                
        if white_or_black == 1:
            pix[rand_row-1][rand_col-1] = 255
        else:
            pix[rand_row-1][rand_col-1] = 0

        i += 1

    # Truncate pixel values
    p.pixels = pix
    p.truncate_intensity_values()

    return p

def median_filtering(pgm_filename, mask_size):
    p = PGMImage(pgm_filename)
    
    k = Kernel(mask = [[1] * mask_size] * mask_size)
    
    p_median_filtered = median_filtered(pgm_filename, k, normalize=True)
    p_median_filtered.save(f"median_filtered-{mask_size}-{p.name}")

def averaging_filtering(pgm_filename, mask_size):
    p = PGMImage(pgm_filename)
    
    k = Kernel(mask = [[1] * mask_size] * mask_size)
    
    p_averaging_filtered = averaging_filtered(pgm_filename, k, normalize=True)
    p_averaging_filtered.save(f"averaging_filtered-{mask_size}-{p.name}")

    
if __name__ == "__main__":
    for img in ("distorted-50-lenna.pgm", "distorted-70-lenna.pgm", "distorted-50-boat.pgm","distorted-70-boat.pgm"):
        for i in (7,15):
            median_filtering(img, i)
            averaging_filtering(img, i)
