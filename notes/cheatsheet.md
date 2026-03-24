# Manim API 快速手册 (Cheatsheet)

> 学到一个 API 就记录一个，逐渐积累成个人参考手册

---

## 📦 基础导入

```python
from manim import *
```

---

## 🔷 基本图形（Mobjects）

| 类名 | 说明 | 示例 |
|------|------|------|
| `Circle` | 圆形 | `Circle(radius=1, color=BLUE)` |
| `Square` | 正方形 | `Square(side_length=2)` |
| `Rectangle` | 矩形 | `Rectangle(width=3, height=2)` |
| `Triangle` | 三角形 | `Triangle()` |
| `Line` | 直线 | `Line(start=LEFT, end=RIGHT)` |
| `Arrow` | 箭头 | `Arrow(start=ORIGIN, end=UP)` |
| `Dot` | 点 | `Dot(point=ORIGIN)` |
| `Arc` | 弧线 | `Arc(radius=1, angle=PI/2)` |
| `Ellipse` | 椭圆 | `Ellipse(width=3, height=2)` |
| `Polygon` | 多边形 | `Polygon(p1, p2, p3)` |

---

## 📝 文字

| 类名 | 说明 | 示例 |
|------|------|------|
| `Text` | 普通文字 | `Text("Hello", font_size=48)` |
| `Tex` | LaTeX（行内） | `Tex(r"$e^{i\pi}+1=0$")` |
| `MathTex` | LaTeX 数学 | `MathTex(r"\sum", substrings_to_isolate=["x"])` |
| `MarkupText` | Pango 标记文字 | `MarkupText("<b>Bold</b>")` |

> [!TIP]
> 使用 `substrings_to_isolate` 可以让 MathTex 识别子对象，从而支持 `set_color_by_tex` 和平滑变换。

---

## 🎨 颜色常量

```python
# 常用颜色
RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK, WHITE, BLACK, GRAY

# 带深浅的颜色
RED_A (浅) → RED_B → RED_C → RED_D → RED_E (深)
BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E

# 特殊颜色
GOLD, MAROON, TEAL, LIGHT_BROWN, DARK_BROWN
```

---

## 🎬 核心动画

| 动画名 | 说明 |
|--------|------|
| `Create(mob)` | 绘制创建对象 |
| `Write(mob)` | 书写效果（文字常用） |
| `FadeIn(mob)` | 淡入 |
| `FadeOut(mob)` | 淡出 |
| `Transform(mob1, mob2)` | 形状变换 |
| `ReplacementTransform(m1, m2)` | 替换变换（m1 变成 m2） |
| `TransformMatchingTex(m1, m2)` | 智能公式变换（自动匹配相同 LaTeX） |
| `GrowFromCenter(mob)` | 从中心长出 |
| `DrawBorderThenFill(mob)` | 先画边框再填色 |
| `Rotate(mob, angle)` | 旋转 |
| `ScaleInPlace(mob, scale)` | 原地缩放 |
| `MoveToTarget(mob)` | 移动到目标位置 |
| `Indicate(mob)` | 高亮提示效果 |
| `Flash(point)` | 闪光效果 |
| `ApplyMatrix(matrix, mob)` | 矩阵变换 |

---

## 🎯 位置与对齐

```python
# 绝对位置
obj.move_to(ORIGIN)          # 移到原点
obj.move_to([1, 2, 0])       # 移到坐标

# 相对位置
obj.next_to(other, RIGHT)    # 在 other 右边
obj.next_to(other, UP, buff=0.5)  # 间距 0.5
obj.shift(RIGHT * 2)         # 向右移动 2 单位

# 对齐边缘
obj.to_edge(UP)              # 移到上边缘
obj.to_corner(UR)            # 移到右上角
obj.align_to(other, LEFT)    # 与 other 左对齐
```

---

## ⏱️ 常用方法

```python
# 播放动画
self.play(Create(circle))
self.play(Create(c1), Create(c2))  # 并行播放
self.play(Succession(a1, a2))      # 顺序播放

# 控制时间
self.wait(1)                 # 等待1秒
self.play(anim, run_time=2)  # 指定持续时间

# 直接添加/移除（无动画）
self.add(mob)
self.remove(mob)

# 相机相关（3D）
self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
```

---

## 📐 方向常量

```python
UP, DOWN, LEFT, RIGHT          # 四个方向
UL, UR, DL, DR                 # 四个角
IN, OUT                        # 3D 纵深方向
ORIGIN = [0, 0, 0]             # 原点
```

---

*持续更新中...*
