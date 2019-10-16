from Lib import spatially_filtered_fast, Kernel
from PGM import PGMImage


def high_boost_filter_kernel(A):
    return Kernel(mask=[[-1, -1, -1], [-1, (9 * A - 1), -1], [-1, -1, -1]])


def do_high_boost_filtering(pgm_filename, A):
    high_boost_filtered = spatially_filtered_fast(
        pgm_filename, high_boost_filter_kernel(A)
    )

    p1 = PGMImage(pgm_filename)

    high_boost_filtered.save(f"highboost-filtered-A{A}-{p1.name}")


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/f_16.pgm"):
        for A in (1, 1.4, 1.9, 2):
            do_high_boost_filtering(img, A)
