#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

void drawBresenham(int x1, int y1, int x2, int y2, int color) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);

    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;

    int p;

    putpixel(x1, y1, color);

    if (dx >= dy) {
        p = 2 * dy - dx;
        while (x1 != x2) {
            x1 += sx;
            if (p < 0) {
                p += 2 * dy;
            } else {
                y1 += sy;
                p += 2 * dy - 2 * dx;
            }
            putpixel(x1, y1, color);
        }
    } else {
        p = 2 * dx - dy;
        while (y1 != y2) {
            y1 += sy;
            if (p < 0) {
                p += 2 * dx;
            } else {
                x1 += sx;
                p += 2 * dx - 2 * dy;
            }
            putpixel(x1, y1, color);
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    int x1, y1, x2, y2;

    printf("Enter starting point (x1 y1): ");
    scanf("%d %d", &x1, &y1);
    printf("Enter ending point   (x2 y2): ");
    scanf("%d %d", &x2, &y2);

    drawBresenham(x1, y1, x2, y2, WHITE);

    getch();
    closegraph();
    return 0;
}
