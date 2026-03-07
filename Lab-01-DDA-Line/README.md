# Lab 01 — 2D Line Drawing using DDA Algorithm

**Course:** Computer Graphics (CSC209)  
**Semester:** III  
**Author:** Sanil Sthapit | [github.com/Sanil-Sth](https://github.com/Sanil-Sth)

---

## 📌 Title
2D Line Drawing using the Digital Differential Analyzer (DDA) Algorithm

---

## 📖 Theory

A computer screen is made up of thousands of tiny dots called **pixels**, arranged in a grid. Every pixel sits at an integer coordinate like (2, 5) or (100, 200). There is no such thing as a pixel at (1.5, 3.7).

A mathematical line, however, is continuous — it passes through infinitely many points, most of which are decimals. So when we want to draw a line on screen, we face a fundamental question:

> *Which pixels do we turn on so that it looks like a straight line?*

The **DDA (Digital Differential Analyzer) Algorithm** answers this question. The core idea is:
- Calculate the total difference in X (`dx`) and Y (`dy`) between the two endpoints
- Determine the number of steps needed — which is `max(|dx|, |dy|)`
- At each step, increment X and Y by a small equal amount
- Round the result to the nearest integer and light up that pixel

### Advantages
- Simple to understand and implement
- Works for all slopes (steep, shallow, negative)

### Disadvantages
- Uses floating point arithmetic (slower than Bresenham's)
- Rounding errors can accumulate over long lines

---

## ❓ Question

Write a program to draw a 2D line using the DDA (Digital Differential Analyzer) Algorithm.

---

## 🔢 Algorithm
```
Step 1: Start
Step 2: Input the two endpoints: (x1, y1) and (x2, y2)
Step 3: Calculate dx = x2 - x1 and dy = y2 - y1
Step 4: If |dx| >= |dy|: steps = |dx|
        Else:            steps = |dy|
Step 5: xInc = dx / steps
        yInc = dy / steps
Step 6: Set x = x1, y = y1
Step 7: Plot pixel at (round(x), round(y))
Step 8: Repeat 'steps' times:
            x = x + xInc
            y = y + yInc
            Plot pixel at (round(x), round(y))
Step 9: Stop
```

---

## 💻 Source Code
```c
/*
 * Lab 01 — 2D Line Drawing using DDA Algorithm
 * Course : Computer Graphics (CSC209)
 * Author : Sanil Sthapit
 * IDE    : Dev-C++ with graphics.h (WinBGIm)
 * OS     : Windows
 */

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
```

---

## 🖼️ Output

![DDA Output](./output.png)

---

## ✅ Conclusion

In this lab, we successfully implemented the **DDA Line Drawing Algorithm** in C using `graphics.h`. The program accepts two endpoints from the user and draws a straight line by incrementally plotting pixels using floating point arithmetic.

The DDA algorithm is simple and works for all slopes. However, since it relies on floating point division and rounding, it is slightly slower than integer-based methods like Bresenham's algorithm — which we implement in the next lab.

---

*Next: [Lab 02 — Bresenham's Line Drawing Algorithm](../Lab-02-Bresenham-Line/)*
