from Lib import spatially_filtered, Kernel
from PGM import PGMImage


prewitt_kernel_x = Kernel(mask=[[-1, 0, 1]] * 3)


prewitt_kernel_y = Kernel(mask=[[-1, -1, -1], [0, 0, 0], [1, 1, 1]])


sobel_kernel_x = Kernel(mask=[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])


sobel_kernel_y = Kernel(mask=[[-1, -2, -1], [0, 0, 0], [1, 2, 1]])


laplacian_kernel = Kernel(mask=[[0, 1, 0], [1, -4, 1], [0, 1, 0]])


def do_sharpening(pgm_filename):
    p1 = PGMImage(pgm_filename)
    p2 = (
        spatially_filtered(pgm_filename, prewitt_kernel_x)
        + spatially_filtered(pgm_filename, prewitt_kernel_y)
        - p1
    )

    p2.save(f"prewitt-sharpened-{p2.name}")

    p3 = (
        spatially_filtered(pgm_filename, sobel_kernel_x)
        + spatially_filtered(pgm_filename, sobel_kernel_y)
        - p1
    )

    p3.save(f"sobel-sharpened-{p2.name}")

    p4 = spatially_filtered(pgm_filename, laplacian_kernel)

    p4.save(f"laplacian-sharpened-{p2.name}")


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        do_sharpening(img)
