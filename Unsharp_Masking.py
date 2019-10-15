from Lib import spatially_filtered_fast, Kernel
from PGM import PGMImage

smoothing_mask = [
    [1, 1, 2, 2, 2, 1, 1],
    [1, 2, 2, 4, 2, 2, 1],
    [2, 2, 4, 8, 4, 2, 2],
    [2, 4, 8, 16, 8, 4, 2],
    [2, 2, 4, 8, 4, 2, 2],
    [1, 2, 2, 4, 2, 2, 1],
    [1, 1, 2, 2, 2, 1, 1],
]


norm = sum(sum(row) for row in smoothing_mask)

normed_smoothing_mask = [[elem / norm for elem in row] for row in smoothing_mask]

smoothing_kernel = Kernel(normed_smoothing_mask)


def do_unsharp_masking(pgm_filename: str) -> PGMImage:
    p_orig = PGMImage(pgm_filename)
    p_lowpass = spatially_filtered_fast(pgm_filename, smoothing_kernel)
    p_lowpass.save(f"lowpass-{p_lowpass.name}")

    p_highpass = p_orig - p_lowpass
    p_highpass.save(f"highpass-{p_highpass.name}")

    return p_highpass


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/f_16.pgm"):
        do_unsharp_masking(img)
