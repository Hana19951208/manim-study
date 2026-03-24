# Day 02：文字与 LaTeX

## 📚 今日学习目标

- [ ] 掌握 `Text` 类——渲染普通文字（支持中文，不依赖 LaTeX）
- [ ] 掌握 `MathTex` 类——渲染 LaTeX 数学公式
- [ ] 了解 `Tex` 和 `MathTex` 的区别
- [ ] 学会文字颜色分段（`t2c` 参数）
- [ ] 使用 `TransformMatchingTex` 制作公式推导动画

---

## 🗒️ 学习笔记

### Text / MathTex / Tex 的区别

| 类名 | 底层 | 适用场景 | 支持中文 |
|------|------|----------|---------|
| `Text` | Pango | 普通文字、标题、中文 | ✅ |
| `MathTex` | LaTeX `$...$` | 数学公式（推荐） | ❌ |
| `Tex` | LaTeX | 混合文字+公式 | ❌（需配置） |

### 创建文字

```python
# 普通文字
t = Text("你好，Manim！", font_size=48, color=WHITE)

# 分段上色
t = Text("Math + Code", t2c={"Math": BLUE, "Code": GREEN})

# 数学公式
eq = MathTex(r"e^{i\pi} + 1 = 0", font_size=60)
```

### 公式变换动画

```python
expr1 = MathTex(r"x^2 + 2x + 1")
expr2 = MathTex(r"(x + 1)^2")
self.play(TransformMatchingTex(expr1, expr2))
```

---

## 🔑 今日 Key Points

| 知识点 | 代码 |
|--------|------|
| 普通文字 | `Text("内容", font_size=48)` |
| 颜色分段 | `Text("AB", t2c={"A": RED, "B": BLUE})` |
| 加粗 | `Text("内容", weight=BOLD)` |
| 数学公式 | `MathTex(r"公式", font_size=52)` |
| 公式书写 | `self.play(Write(eq))` |
| 公式变换 | `TransformMatchingTex(expr1, expr2)` |

---

## 🚀 渲染命令

```bash
conda activate manim-study
manim -pql main.py TextDemo
```

---

## 📝 完成情况

- [ ] 成功渲染 TextDemo 场景
- [ ] 理解 Text 与 MathTex 的使用场景
- [ ] 独立编写一个数学公式动画

---

*学习时间：待补充*
