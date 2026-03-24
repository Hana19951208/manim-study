# Day 03：颜色与渐变

## 📚 今日学习目标

- [ ] 掌握 Manim 的颜色系统（核心颜色与深浅变化）
- [ ] 学会使用 `.set_color()` 和 `.set_fill()`
- [ ] 掌握颜色渐变：`set_color_gradient()`
- [ ] 学习使用自定义十六进制（Hex）颜色和 RGB
- [ ] 制作一个流光溢彩的渐变动画

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

- [ ] 成功运行 Day03ColorDemo
- [ ] 学会自定义 Hex 颜色
- [ ] 掌握了多色渐变技巧
- [ ] 完成课后练习
