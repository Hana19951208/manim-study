# Manim API 快速手册 (Cheatsheet)

> 💡 本手册定位为 **API 速查索引**。深度学习笔记与避坑经验请点击对应章节的“路由链接”。

---

## 🏗️ 基础与几何 (Mobjects)
| 类型 | 常用类名 | 学习笔记路由 |
|------|---------|------------|
| 基础形状 | `Circle`, `Square`, `Triangle`, `Rectangle` | [Day 01: 基础形状](../week01_basics/day01_shapes/README.md) |
| 文本处理 | `Text`, `MathTex`, `Tex` | [Day 02: 文字与公式](../week01_basics/day02_text/README.md) |
| 颜色/样式 | `set_color`, `set_fill`, `set_stroke` | [Day 03: 颜色与样式](../week01_basics/day03_color/README.md) |

---

## 🎬 核心动画 (Animations)
| 类别 | 常用方法 | 核心技巧 |
|------|---------|---------|
| 创建/移除 | `Create`, `Write`, `FadeIn`, `FadeOut` | - |
| 基础变换 | `Transform`, `ReplacementTransform` | [Day 04: 变换与过渡](../week01_basics/day04_transform/README.md) |
| 智能变换 | `TransformMatchingTex`, `TransformMatchingShapes` | [详见 Day 04 避坑指南](../week01_basics/day04_transform/README.md#🐞-避坑指南-troubleshooting) |

---

## 🎯 排版与对齐 (Layout)
| 功能 | 方法 | 说明 |
|------|---------|---------|
| 线性排版 | `group.arrange(RIGHT, buff=0.5)` | 自动沿方向排列 [详见 Day 02](../week01_basics/day02_text/README.md) |
| 网格排版 | `group.arrange_in_grid(rows=2, buff=1)` | 快速生成阵列 [详见 Day 04](../week01_basics/day04_transform/README.md) |
| 相对对齐 | `obj.next_to(other, DOWN)` | 处理物体间间距 |

---

## 🛠️ 项目模板 (Templates)
| 模板类 | 主要功能 | 使用参考 |
|------|---------|---------|
| `StudyScene` | 自动开场/结尾动画, GitHub 标识 | [查看模板源码](../utils/templates.py) |

---

## 🧭 进阶路由：避坑指南 (Troubleshooting)
> 记录学习过程中遇到的疑难杂症与解决方案。

- [**动画冲突**：同时执行 Transform 与 Rotate 的解法](../week01_basics/day04_transform/README.md#1-transform-与-rotate-的抢地盘冲突)
- [**参数匹配**：UpdateFromAlphaFunc 的 TypeError 处理](../week01_basics/day04_transform/README.md#2-updatefromalphafunc-报错)

---
*持续更新中... 最后更新日期: 2026-03-26*
