# Day 01：基本几何图形

## 📚 今日学习目标

- [ ] 理解 Manim 场景（Scene）的基本结构
- [ ] 掌握创建基本图形：`Circle`、`Square`、`Triangle`
- [ ] 学会使用 `Create`、`FadeOut`、`Write` 等基础动画
- [ ] 了解并行动画和顺序动画的区别

---

## 🗒️ 学习笔记

### Scene 的基本结构

```python
class MyScene(Scene):
    def construct(self):
        # 所有动画在这里编写
        pass
```

- `Scene` 是所有 2D 动画场景的基类
- `construct()` 是场景的入口方法，类似 `main()` 函数
- 使用 `self.play()` 播放动画，`self.wait()` 暂停

### 创建图形

```python
circle   = Circle(radius=1, color=BLUE)
square   = Square(side_length=2, color=RED)
triangle = Triangle(color=GREEN)
```

### 位置控制

```python
obj.move_to(LEFT * 3)   # 移到原点左边3个单位
obj.move_to(ORIGIN)     # 移到屏幕中心
obj.shift(UP)           # 在当前位置向上移动
```

### 播放动画

```python
# 顺序播放
self.play(Create(circle))
self.play(Create(square))

# 并行播放（同时进行）
self.play(Create(circle), Create(square))
```

---

## 🔑 今日 Key Points

| 知识点 | 代码 |
|--------|------|
| 创建圆 | `Circle(radius=1, color=BLUE)` |
| 创建正方形 | `Square(side_length=2)` |
| 绘制动画 | `self.play(Create(mob))` |
| 淡出 | `self.play(FadeOut(mob))` |
| 填充颜色 | `mob.animate.set_fill(BLUE, opacity=0.5)` |
| 等待 | `self.wait(1)` |

---

## 🚀 渲染命令

```bash
# 开发预览
conda activate manim-study
manim -pql main.py ShapesDemo

# 高质量导出
manim -pqh main.py ShapesDemo
```

---

## 📝 完成情况

- [ ] 成功渲染示例代码
- [ ] 理解每行代码的含义
- [ ] 独立修改代码（改颜色、改大小）

---

*学习时间：2026-03-24*
