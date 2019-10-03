from Lib import spatially_filtered, Kernel
from PGM import PGMImage


def high_boost_filter_kernel(A):
    return Kernel(mask=[[-1, -1, -1], [-1, (9 * A - 1), -1], [-1, -1, 1]])


def do_high_boost_filtering(pgm_filename, A):
    high_boost_filtered = spatially_filtered(pgm_filename, high_boost_filter_kernel(A))


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/f_16.pgm"):
        for A in (1, 1.4, 1.9, 2):
            do_unsharp_masking(img, A)
