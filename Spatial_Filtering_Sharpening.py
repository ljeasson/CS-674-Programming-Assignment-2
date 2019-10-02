from Lib import spatially_filtered, Kernel
from PGM import PGMImage


class PrewittKernelX(Kernel):
    mask = [[-1, 0, 1]] * 3


class PrewittKernelY(Kernel):
    mask = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]


class SobelKernelX(Kernel):
    mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]


class SobelKernelY(Kernel):
    mask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]


class LaplacianKernel(Kernel):
    mask = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]


def do_sharpening(pgm_filename):
    p1 = PGMImage(pgm_filename)
    p2 = (
        spatially_filtered(pgm_filename, PrewittKernelX)
        + spatially_filtered(pgm_filename, PrewittKernelY)
        - p1
    )

    p2.save("prewitt-sharpened-{p2.name}")

    p3 = (
        spatially_filtered(pgm_filename, SobelKernelX)
        + spatially_filtered(pgm_filename, SobelKernelY)
        - p1
    )

    p3.save("sobel-sharpened-{p2.name}")

    p4 = spatially_filtered(pgm_filename, LaplacianKernel)

    p4.save("laplacian-sharpened-{p2.name}")


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/sf.pgm"):
        do_sharpening(img)
