# Day 04：变换与过渡 (Transformations & Transitions)

## 📚 今日学习目标

- [ ] 理解 `Transform` 与 `ReplacementTransform` 的底层差异（对象持有权）
- [ ] 掌握 `FadeTransform` 在不同形状物体间的自然过渡效果
- [ ] 学习使用 `TransformMatchingTex` 制作动态公式推导动画
- [ ] 掌握 `TransformMatchingShapes` 在普通物体间的智能变换
- [ ] 实际产出一个几何图形与公式协同变换的演示页面

---

## 🗒️ 学习笔记

### 核心变换 API 对比

| 方法 | 核心逻辑 | 适用场景 |
|------|---------|---------|
| `Transform(A, B)` | 修改 A 的点位置以匹配 B，A 依然留在场景中 | 变换后仍需引用 A |
| `ReplacementTransform(A, B)` | 修改 A 到 B 后，将 A 在场景中销毁并替换为 B | 变换后只需引用 B (推荐写法) |
| `FadeTransform(A, B)` | 淡出 A 的同时淡入 B，并带有轻微缩放变换 | 形状差异过大，传统 Transform 效果差的情况 |
| `TransformMatchingTex(A, B)` | 根据 LaTeX 字符串匹配自动调整各子图层位置 | 复杂的公式推导、方程变换 |

### 💡 技巧提示

1.  **分段公式**：在使用 `TransformMatchingTex` 时，务必将公式拆分为多个字符串片段，以便 Manim 自动寻找相同的子串。
2.  **路径平整化**：变换动画若出现“交叉重叠”或“形状诡异”，可以尝试加上 `path_arc` 参数以增加旋转过渡感。
3.  **lag_ratio**：在对 VGroup 使用变换时，设置 `lag_ratio=0.1` 可以产生依次变换的层次美感。

---

## 🚀 渲染命令

```bash
conda activate manim-study
# 预览 Day04TransformDemo
python week01_basics/day04_transform/main.py
```

---

## 📝 完成情况

- [x] 成功运行 Day04TransformDemo
- [x] 学会了如何拆分公式片段以支持智能匹配
- [x] 完成一个从正方形平滑变换为数学公式的小实验
- [x] 了解了 ReplacementTransform 的对象销毁机制
- [x] 生成并预览了课后练习 ([查看题目](exercise.py) | [参考答案](solution.py))

---

## 🛠️ 预览练习
```bash
conda activate manim-study
# 预览练习模板
manim -pql week01_basics/day04_transform/exercise.py Day04Exercise1

# 预览参考答案
manim -pql week01_basics/day04_transform/solution.py Day03Solution1
manim -pql week01_basics/day04_transform/solution.py Day03Solution2
manim -pql week01_basics/day04_transform/solution.py Day03Solution3
```
