#include <inttypes.h>

void apply_spatial_filter(unsigned char **image, uint16_t width, uint16_t height,
                          float **kernel, uint16_t k_rows, uint16_t k_cols);

void apply_spatial_filter(unsigned char **image, uint16_t width, uint16_t height,
                          float **kernel, uint16_t k_rows, uint16_t k_cols) {
  uint8_t half_k_rows = (uint8_t)(k_rows / 2);
  uint8_t half_k_cols = (uint8_t)(k_cols / 2);
  for (uint16_t i = 0; i < height; i++) {
    for (uint16_t j = 0; j < width; j++) {
      unsigned char pxl = 0;

      for (uint8_t s = 0; s < k_rows; s++) {
        for (uint8_t t = 0; t < k_cols; t++) {
          uint16_t x = i - half_k_rows + s;
          uint16_t y = j - half_k_cols + t;

          if (x < 0 || x >= height)
            x = 0;
          if (y < 0 || y >= width)
            y = 0;

          float weighted_pxl = image[x][y] * kernel[s][t];
          if (weighted_pxl > 255)
            weighted_pxl = 255;
          if (weighted_pxl < 0)
            weighted_pxl = 0;

          pxl += (unsigned char) weighted_pxl;
        }
      }

      image[i][j] = pxl;
    }
  }
}

int main() {}
