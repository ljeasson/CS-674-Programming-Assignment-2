#include <stdio.h>

void print_stuff(char **image) {
    printf("Reached\n");
    for (int i = 0; i < 256; i++) {
        for (int j = 0; j < 256; j++) {
            printf("%c\n", image[i][j]);
        }
    }
}

int main() {}
