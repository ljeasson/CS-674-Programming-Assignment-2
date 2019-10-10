from Lib import spatially_filtered, Kernel
from PGM import PGMImage


def do_correlation(pgm_filename, mask_filename):
    pmask = PGMImage(mask_filename)

    def correlation_kernel(p: PGMImage):
        mask = []
        for row in p.pixels:
            mask.append([b for b in row])
        return Kernel(mask)

    k = correlation_kernel(pmask)

    p2: PGMImage = spatially_filtered(pgm_filename, k)

    p2.save(f"correlated-to-{pmask.name}-{p2.name}")


if __name__ == "__main__":
    do_correlation(
        pgm_filename="images/shapes.pgm", mask_filename="images/small-shape.pgm"
    )
