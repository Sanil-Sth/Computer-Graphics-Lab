#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

void drawCircleRaster(int cx, int cy, int r, int color) {
    int x = cx - r;

    while (x <= cx + r) {
        // Calculate y using circle equation: x² + y² = r²
        double y = sqrt((double)(r * r) - (double)((x - cx) * (x - cx)));

        // Plot upper and lower halves
        putpixel(x, cy + (int)round(y), color);
        putpixel(x, cy - (int)round(y), color);

        x++;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    int cx, cy, r;

    printf("Enter center (cx cy): ");
    scanf("%d %d", &cx, &cy);
    printf("Enter radius r: ");
    scanf("%d", &r);

    drawCircleRaster(cx, cy, r, WHITE);

    getch();
    closegraph();
    return 0;
}
