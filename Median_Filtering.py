def median_filtering(image, mask_size):
    return

def median_averaging(image, mask_size):
    return

if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/boat.pgm"):
        for i in (7, 15):
            median_filtering(img, i)
        for j in (7, 15):
            median_averaging(img, j)
