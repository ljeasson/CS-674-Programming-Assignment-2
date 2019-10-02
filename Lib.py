from PGM import PGMImage

from dataclasses import dataclass
from math import e, pi
from typing import List


@dataclass
class Kernel:
    mask: List[List[int]]

    @property
    def sz(self) -> int:
        return len(self.mask)


def spatially_filtered(pgm_filename: str, k: Kernel) -> PGMImage:
    """
    Return an image with the spatial filter `k` applied to it.

    :param pgm_filename file name of image to perform filter on
    :param k a kernel of the spatial filter we want to apply
    """
    p1, p2 = PGMImage(pgm_filename), PGMImage(pgm_filename)

    for i in range(p1.rows):
        new_row = []
        old_row = [b for b in p1.pixels[i]]
        for j in range(p1.cols):

            pxl = 0
            for s in range(k.sz):
                for t in range(k.sz):
                    x, y = i - int(k.sz / 2) + s, j - int(k.sz / 2) + t
                    # Pad edges of the image with zeros
                    if x < 0 or x >= p1.rows:
                        x = 0
                    if y < 0 or y >= p1.cols:
                        y = 0
                    # print(f"i = {i} j = {j} s = {s} t = {t} x = {x} y = {y}")
                    pxl += p1.pixels[x][y] * k.mask[s][t]

            new_row.append(pxl)

        def coerce(b):
            """ Force values to fall between 0, 255 for PGM images. """
            b = max(b, 0)
            b = min(b, 255)
            return b

        p2.pixels[i] = b"".join([bytes([coerce(b)]) for b in new_row])

    return p2


def run_tests():
    def test_1_identity_filter():
        identity_filter = Kernel(mask=[[1]])
        pgm_filename = "images/lenna.pgm"

        expected = PGMImage(pgm_filename)

        actual = spatially_filtered(pgm_filename, identity_filter)

        assert expected.pixels == actual.pixels

    test_1_identity_filter()


if __name__ == "__main__":
    run_tests()
