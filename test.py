import ctypes

from ctypes import byref, c_char, c_char_p, pointer, POINTER as PointerT

from PGM import PGMImage

p = PGMImage("images/lenna.pgm")

PGMRowT = c_char * p.cols
PGMImageT = PointerT(PGMRowT) * p.rows

c_pixels = PGMImageT()

for i in range(p.rows):
    row = PGMRowT()
    for j in range(p.cols):
        row[j] = p.pixels[i][j]
    c_pixels[i] = pointer(row)

test = ctypes.cdll.LoadLibrary("./test.so")

test.print_stuff(byref(c_pixels))
