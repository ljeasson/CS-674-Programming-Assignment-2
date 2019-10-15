import ctypes

from ctypes import c_char, c_double, pointer as c_pointer_to, POINTER as PointerT
from dataclasses import dataclass
from typing import List

from PGM import PGMImage


@dataclass
class Kernel:
    mask: List[List[int]]

    @property
    def rows(self) -> int:
        return len(self.mask)

    @property
    def cols(self) -> int:
        return len(self.mask[0]) if self.mask else 0


def spatially_filtered_fast(pgm_filename: str, k: Kernel) -> PGMImage:
    p = PGMImage(pgm_filename)

    def c_2d_arr_from_pyobj(pyobj: List[List[int]], arr_type, row_type):
        c_2d_arr = arr_type()
        for i in range(len(pyobj)):
            row = row_type()
            for j in range(len(pyobj[0])):
                row[j] = pyobj[i][j]
            c_2d_arr[i] = c_pointer_to(row)

        return c_2d_arr

    def c_2d_arr_empty(arr_type, row_type, rows, cols):
        c_2d_arr = arr_type()
        for i in range(rows):
            row = row_type()
            for j in range(cols):
                row[j] = 0
            c_2d_arr[i] = c_pointer_to(row)

        return c_2d_arr

    C_PGMRowT = c_char * p.cols
    C_PGMImageT = PointerT(C_PGMRowT) * p.rows

    C_KernelRowT = c_double * k.cols
    C_KernelT = PointerT(C_KernelRowT) * k.rows

    c_p = c_2d_arr_from_pyobj(p.pixels, C_PGMImageT, C_PGMRowT)
    c_p_2 = c_2d_arr_empty(
        PointerT(c_double * p.cols) * p.rows, c_double * p.cols, p.rows, p.cols
    )
    c_k = c_2d_arr_from_pyobj(k.mask, C_KernelT, C_KernelRowT)

    spatialfilter = ctypes.cdll.LoadLibrary("./spatialfilter.so")

    spatialfilter.apply_spatial_filter(c_p, c_p_2, p.cols, p.rows, c_k, k.rows, k.cols)

    p2 = PGMImage(pgm_filename)
    for i in range(p.rows):
        p2.pixels[i] = [c_p_2[i][0][j] for j in range(p2.cols)]

    p2.normalize_intensity_values()

    return p2


def spatially_filtered(pgm_filename: str, k: Kernel) -> PGMImage:
    """
    Return an image with the spatial filter `k` applied to it.

    :param pgm_filename file name of image to perform filter on
    :param k a kernel of the spatial filter we want to apply
    """
    p1, p2 = PGMImage(pgm_filename), PGMImage(pgm_filename)

    def coerce(b):
        """ Force values to fall between 0, 255 for PGM images. """
        b = max(b, 0)
        b = min(b, 255)
        b = int(b)
        return b

    half_k_rows = int(k.rows / 2)
    half_k_cols = int(k.cols / 2)
    for i in range(p1.rows):
        new_row = []
        for j in range(p1.cols):

            pxl = 0
            _x = i - half_k_rows
            _y = j - half_k_cols
            for s in range(k.rows):
                for t in range(k.cols):
                    x = _x + s
                    y = _y + t

                    # Pad edges of the image with zeros
                    if x < 0 or x >= p1.rows or y < 0 or y >= p1.cols:
                        orig_image_x_y = 0
                    else:
                        orig_image_x_y = p1.pixels[x][y]
                    weighted_pxl = orig_image_x_y * k.mask[s][t]

                    if False:
                        weighted_pxl = coerce(weighted_pxl)

                    pxl += weighted_pxl

            if False:
                pxl = coerce(pxl)
            new_row.append(pxl)

        p2.pixels[i] = [int(b) for b in new_row]

        p2.normalize_intensity_values()

    return p2


def run_tests():
    def test_1_identity_filter():
        identity_filter = Kernel(mask=[[1]])
        pgm_filename = "images/lenna.pgm"

        expected = PGMImage(pgm_filename)

        actual = spatially_filtered_fast(pgm_filename, identity_filter)

        assert expected.pixels == actual.pixels

    test_1_identity_filter()


if __name__ == "__main__":
    run_tests()
