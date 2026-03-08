#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

void drawDDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = (abs(dx) >= abs(dy)) ? abs(dx) : abs(dy);

    float xInc = (float)dx / steps;
    float yInc = (float)dy / steps;

    float x = x1, y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel((int)round(x), (int)round(y), WHITE);
        x += xInc;
        y += yInc;
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int x1, y1, x2, y2;
    printf("Enter starting point (x1 y1): ");
    scanf("%d %d", &x1, &y1);
    printf("Enter ending point  (x2 y2): ");
    scanf("%d %d", &x2, &y2);

    drawDDA(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}
