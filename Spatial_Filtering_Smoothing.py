from Lib import spatially_filtered, Kernel
from PGM import PGMImage

average_matrix_7 = Kernel(mask = [[(1/49)] * 7] * 7)

average_matrix_15 = Kernel(mask = [[(1/225)] * 15] * 15)

gaussian_matrix_7 = Kernel(mask = [ [1,1,2,2,2,1,1], 
                                  [1,2,2,4,2,2,1], 
                                  [2,2,4,8,4,2,2], 
                                  [2,4,8,16,8,4,2], 
                                  [2,2,4,8,4,2,2], 
                                  [1,2,2,4,2,2,1], 
                                  [1,1,2,2,2,1,1] ])

gaussian_matrix_15 = Kernel(mask = [ [2,2,3,4,5,5,6,6,6,5,5,4,3,2,2],
                                     [2,3,4,5,7,7,8,8,8,7,7,5,4,3,2],
                                     [3,4,6,7,9,10,10,11,10,10,9,7,6,4,3],
                                     [4,5,7,9,10,12,13,13,13,12,10,9,7,5,4],
                                     [5,7,9,11,13,14,15,16,15,14,13,11,9,7,5],
                                     [5,7,10,12,14,16,17,18,17,16,14,12,10,7,5],
                                     [6,8,10,13,15,17,19,19,19,17,15,13,10,8,6],
                                     [6,8,11,13,16,18,19,20,19,18,16,13,11,8,6],
                                     [6,8,10,13,15,17,19,19,19,17,15,13,10,8,6],
                                     [5,7,10,12,14,16,17,18,17,16,14,12,10,7,5],
                                     [5,7,9,11,13,14,15,16,15,14,13,11,9,7,5],
                                     [4,5,7,9,10,12,13,13,13,12,10,9,7,5,4],
                                     [3,4,6,7,9,10,10,11,10,10,9,7,6,4,3],
                                     [2,3,4,5,7,7,8,8,8,7,7,5,4,3,2],
                                     [2,2,3,4,5,5,6,6,6,5,5,4,3,2,2] ])

def smooth_image_averaging(pgm_filename):
    p = PGMImage(pgm_filename)
    
    p_average_7 = spatially_filtered(pgm_filename, average_matrix_7, truncate=True)
    p_average_7.save(f"smoothed_averaging-7-{p.name}")

    p_average_15 = spatially_filtered(pgm_filename, average_matrix_15, truncate=True)
    p_average_15.save(f"smoothed_averaging-15-{p.name}")
    
def smooth_image_gaussian(pgm_filename):
    p = PGMImage(pgm_filename)

    p_gaussian = spatially_filtered(pgm_filename, gaussian_matrix_7, normalize=True, truncate=False)
    p_gaussian.save(f"smoothed_gaussian-7-{p.name}") 

    p_gaussian = spatially_filtered(pgm_filename, gaussian_matrix_15, normalize=True, truncate=False)
    p_gaussian.save(f"smoothed_gaussian-15-{p.name}")    


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        smooth_image_averaging(img)
        smooth_image_gaussian(img)