# Day 03：颜色与渐变

## 📚 今日学习目标

- [x] 掌握 Manim 的颜色系统（核心颜色与深浅变化）
- [x] 学会使用 `.set_color()` 和 `.set_fill()`
- [x] 掌握颜色渐变：`set_color_gradient()`
- [x] 学习使用自定义十六进制（Hex）颜色和 RGB
- [x] 制作一个流光溢彩的渐变动画

### 🎯 今日总结
今天系统学习了 Manim 的颜色管理，掌握了渐变、光泽以及自定义 Hex 颜色的用法。此外，还重构并固化了项目的视频开场模板 `StudyScene`。

---

## 🗒️ 学习笔记

### 颜色设置
- `obj.set_color(RED)`：设置线条/整体颜色
- `obj.set_fill(BLUE, opacity=0.5)`：设置填充色及透明度

### 颜色列表
Manim 内置了丰富的颜色：
- 标准色：`RED`, `BLUE`, `GREEN`, `YELLOW` 等
- 深浅色：`BLUE_A` (浅) -> `BLUE_E` (深)
- 自定义：`"#FFFFFF"` (Hex) 或 `rgb_to_color([0.5, 0.5, 0.5])`

### 渐变效果
```python
# 将对象从红色渐变到黄色
obj.set_color_gradient(RED, YELLOW)
```

---

## 🚀 渲染命令

```bash
conda activate manim-study
python week01_basics/day03_color/main.py
```

---

## 📝 完成情况

- [x] 成功运行 Day03ColorDemo
- [x] 学会自定义 Hex 颜色
- [x] 掌握了多色渐变技巧
- [x] 完成课后练习 ([查看题目](exercise.py) | [参考答案](solution.py))

---

## 🛠️ 预览练习
```bash
conda activate manim-study
# 预览练习模板
manim -pql week01_basics/day03_color/exercise.py Day03Exercise1

# 预览参考答案
manim -pql week01_basics/day03_color/solution.py Day03Solution1
manim -pql week01_basics/day03_color/solution.py Day03Solution2
manim -pql week01_basics/day03_color/solution.py Day03Solution3
```
