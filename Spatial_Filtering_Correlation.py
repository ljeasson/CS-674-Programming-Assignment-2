def do_correlation(pgm_filename, mask_filename):
    class CorrelationKernel(Kernel):
        @classmethod
        def from_pgm(cls, pgm_filename) -> Kernel:
            p = PGMImage(pgm_filename)
            mask = []
            for row in p.pixels:
                mask.append([b for b in row])
            return cls(mask)

        k = CorrelationKernel.from_pgm(mask_filename)

        p2: PGMImage = spatially_filtered(pgm_filename, k)

        p2.save(f"correlated-to-{mask_filename}-{pgm_filename}")


if __name__ == "__main__":
    do_correlation(
        pgm_filename="images/shapes.pgm", mask_filename="images/small-shape.pgm"
    )
