from Lib import spatially_filtered_fast, Kernel
from PGM import PGMImage


prewitt_kernel_x = Kernel(mask=[[-1, 0, 1]] * 3)


prewitt_kernel_y = Kernel(mask=[[-1, -1, -1], [0, 0, 0], [1, 1, 1]])


sobel_kernel_x = Kernel(mask=[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])


sobel_kernel_y = Kernel(mask=[[-1, -2, -1], [0, 0, 0], [1, 2, 1]])


laplacian_kernel = Kernel(mask=[[0, 1, 0], [1, -4, 1], [0, 1, 0]])


def do_sharpening(pgm_filename):
    p1 = PGMImage(pgm_filename)

    # Prewitt filtering
    p1_x_filtered_prewitt = spatially_filtered_fast(pgm_filename, prewitt_kernel_x)
    p1_x_filtered_prewitt.save(f"gradient-magnitude-prewitt-x-{p1.name}")

    p1_y_filtered_prewitt = spatially_filtered_fast(pgm_filename, prewitt_kernel_y)
    p1_y_filtered_prewitt.save(f"gradient-magnitude-prewitt-y-{p1.name}")

    p2 = p1_x_filtered_prewitt + p1_y_filtered_prewitt
    p2.save(f"isotropic-gradient-magnitude-prewitt-{p1.name}")

    p3 = p1 - p2
    p3.save(f"prewitt-sharpened-{p1.name}")

    # Sobel filtering
    p1_x_filtered_sobel = spatially_filtered_fast(pgm_filename, sobel_kernel_x)
    p1_x_filtered_sobel.save(f"gradient-magnitude-sobel-x-{p1.name}")

    p1_y_filtered_sobel = spatially_filtered_fast(pgm_filename, sobel_kernel_y)
    p1_y_filtered_sobel.save(f"gradient-magnitude-sobel-y-{p1.name}")

    p2 = p1_x_filtered_sobel + p1_y_filtered_sobel
    p2.save(f"isotropic-gradient-magnitude-sobel-{p1.name}")
    p3 = p1 - p2
    p3.save(f"sobel-sharpened-{p1.name}")

    # Laplace filtering
    p1_laplace_filtered = spatially_filtered_fast(pgm_filename, laplacian_kernel)
    p1_laplace_filtered.save(f"laplacian-gradient-magnitude-{p1.name}")

    p2 = p1 - p1_laplace_filtered

    p2.save(f"laplacian-sharpened-{p1.name}")


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        do_sharpening(img)
