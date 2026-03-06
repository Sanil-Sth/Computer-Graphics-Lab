# Computer Graphics Lab — CSC209



![Language](https://img.shields.io/badge/Language-C-blue?style=flat-square)




![IDE](https://img.shields.io/badge/IDE-Dev%20C%2B%2B-orange?style=flat-square)




![Graphics](https://img.shields.io/badge/Graphics-BGI%20%2F%20graphics.h-green?style=flat-square)




![Semester](https://img.shields.io/badge/Semester-III-purple?style=flat-square)




![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)



> Lab programs for the **Computer Graphics (CSC209)** course — Semester III, B.Sc. CSIT.  
> All programs are written in **C using graphics.h (BGI)** and compiled with **Dev-C++** on Windows.

---

## Author

**Sanil Sthapit**  
🔗 [github.com/Sanil-Sth](https://github.com/Sanil-Sth)

---

## 🛠️ Setup & How to Run

### Requirements
- **Dev-C++** (with BGI/graphics.h support)
- **WinBGIm** library configured in Dev-C++
- **Windows OS**

### Steps to Configure Dev-C++ with graphics.h
1. Download and install [Dev-C++](https://sourceforge.net/projects/orwelldevcpp/)
2. Download the WinBGIm package and copy:
   - `graphics.h` → `C:\Dev-Cpp\include\`
   - `libbgi.a` → `C:\Dev-Cpp\lib\`
3. In Dev-C++, go to **Tools → Compiler Options → Linker**  
   Add: `-lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32`
4. Open any `.c` file from this repo and hit **F11** to compile & run

---

## 📋 Lab Index

| # | Lab Title | Topic | Status |
|---|-----------|-------|--------|
| 01 | [DDA Line Drawing](./Lab-01-DDA-Line/) | Scan Conversion | 🔄 Pending |
| 02 | [Bresenham's Line Drawing](./Lab-02-Bresenham-Line/) | Scan Conversion | 🔄 Pending |
| 03 | [Circle Drawing — Raster](./Lab-03-Circle-Raster/) | Scan Conversion | 🔄 Pending |
| 04 | [Midpoint Circle + Arc & Sector](./Lab-04-Midpoint-Circle/) | Scan Conversion | 🔄 Pending |
| 05 | [Rotate a Point about Origin](./Lab-05-Rotate-Point/) | 2D Transformation | 🔄 Pending |
| 06 | [Rotate a Triangle about Origin](./Lab-06-Rotate-Triangle/) | 2D Transformation | 🔄 Pending |
| 07 | [Scale a Triangle](./Lab-07-Scale-Triangle/) | 2D Transformation | 🔄 Pending |
| 08 | [Translate a Triangle](./Lab-08-Translate-Triangle/) | 2D Transformation | 🔄 Pending |
| 09 | [Reflect a Triangle](./Lab-09-Reflect-Triangle/) | 2D Transformation | 🔄 Pending |

---

## 📚 Syllabus Coverage

| Unit | Topic |
|------|-------|
| Unit 1 | Introduction to Computer Graphics |
| Unit 2 | Scan Conversion Algorithms ← *Labs 1–4* |
| Unit 3 | 2D Geometric Transformations ← *Labs 5–9* |

---

## 📁 Repository Structure

| Folder | Contents |
|--------|----------|
| `Lab-01-DDA-Line/` | README.md, dda_line.c, output.png |
| `Lab-02-Bresenham-Line/` | README.md, bresenham_line.c, output.png |
| `Lab-03-Circle-Raster/` | README.md, circle_raster.c, output.png |
| `Lab-04-Midpoint-Circle/` | README.md, midpoint_circle.c, output.png |
| `Lab-05-Rotate-Point/` | README.md, rotate_point.c, output.png |
| `Lab-06-Rotate-Triangle/` | README.md, rotate_triangle.c, output.png |
| `Lab-07-Scale-Triangle/` | README.md, scale_triangle.c, output.png |
| `Lab-08-Translate-Triangle/` | README.md, translate_triangle.c, output.png |
| `Lab-09-Reflect-Triangle/` | README.md, reflect_triangle.c, output.png |

> 📌 *Each lab folder contains a detailed README with theory, algorithm, source code, and output screenshot.*
