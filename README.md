# 🎬 Manim 系统学习计划

> **目标**：系统性掌握 Manim Community Edition，从基础动画到复杂数学可视化，每天学习一个核心技巧。

---

## 📋 项目概述

本项目记录使用 **Manim Community Edition (v0.18+)** 制作数学动画的完整学习路径。  
每天聚焦一个技巧，产出可运行的示例代码 + 渲染结果。

## 🗂️ 目录结构

```
manim-study/
├── README.md               # 本文件
├── AGENTS.md               # AI 助理协作规范
├── .env                    # 环境变量（可选）
├── requirements.txt        # Python 依赖
│
├── week01_basics/          # 第1周：基础图形与动画
│   ├── day01_shapes/       # 基本几何图形
│   ├── day02_text/         # 文字与 LaTeX
│   ├── day03_color/        # 颜色与渐变
│   ├── day04_transform/    # 变换与过渡
│   ├── day05_camera/       # 摄像机与场景
│   ├── day06_group/        # 对象分组
│   └── day07_review/       # 第1周综合练习
│
├── week02_animation/       # 第2周：动画技巧进阶
│   ├── day08_timing/       # 动画时序与速率
│   ├── day09_updater/      # Updater 实时更新
│   ├── day10_3d/           # 3D 场景基础
│   ├── day11_graph/        # 函数图像绘制
│   ├── day12_vector/       # 向量场
│   ├── day13_matrix/       # 矩阵变换可视化
│   └── day14_review/       # 第2周综合练习
│
├── week03_math/            # 第3周：数学概念可视化
│   ├── day15_calculus/     # 微积分动画
│   ├── day16_fourier/      # 傅里叶变换
│   ├── day17_geometry/     # 几何证明
│   ├── day18_number_theory/# 数论可视化
│   ├── day19_complex/      # 复数与欧拉公式
│   ├── day20_physics/      # 物理模拟
│   └── day21_review/       # 第3周综合练习
│
├── week04_advanced/        # 第4周：高级技巧与项目
│   ├── day22_custom_anim/  # 自定义动画类
│   ├── day23_svg/          # SVG 导入与处理
│   ├── day24_audio/        # 音频同步
│   ├── day25_section/      # 分段与剪辑
│   ├── day26_plugin/       # 插件扩展
│   ├── day27_optimization/ # 渲染优化技巧
│   └── day28_project/      # 综合实战项目
│
├── assets/                 # 静态资源
│   ├── images/             # 图片素材
│   ├── svg/                # SVG 文件
│   └── audio/              # 音频文件
│
├── output/                 # 渲染输出（已 gitignore）
│   ├── videos/
│   └── images/
│
└── notes/                  # 学习笔记
    ├── cheatsheet.md       # 快速参考手册
    ├── troubleshooting.md  # 常见问题排查
    └── resources.md        # 参考资源汇总
```

---

## 🚀 快速开始

### 1. 激活 conda 环境

```bash
conda activate manim-study
```

### 2. 渲染单个文件（低质量预览）

```bash
manim -pql week01_basics/day01_shapes/main.py ShapesDemo
```

### 3. 渲染高质量输出

```bash
manim -pqh week01_basics/day01_shapes/main.py ShapesDemo
```

### 4. 渲染成 GIF

```bash
manim -i week01_basics/day01_shapes/main.py ShapesDemo
```

---

## 📅 学习进度

| 天次 | 主题 | 状态 | 笔记 |
|------|------|------|------|
| Day 01 | 基本几何图形 | ✅ 已完成 | [笔记](week01_basics/day01_shapes/README.md) |
| Day 02 | 文字与 LaTeX | ✅ 已完成 | [笔记](week01_basics/day02_text/README.md) |
| Day 03 | 颜色与渐变 | 🔄 进行中 | [笔记](week01_basics/day03_color/README.md) |
| Day 04 | 变换与过渡 | ⬜ 待开始 | - |
| Day 05 | 摄像机与场景 | ⬜ 待开始 | - |
| Day 06 | 对象分组 | ⬜ 待开始 | - |
| Day 07 | 第1周综合 | ⬜ 待开始 | - |
| Day 08 | 动画时序 | ⬜ 待开始 | - |
| Day 09 | Updater | ⬜ 待开始 | - |
| Day 10 | 3D 场景 | ⬜ 待开始 | - |
| Day 11 | 函数图像 | ⬜ 待开始 | - |
| Day 12 | 向量场 | ⬜ 待开始 | - |
| Day 13 | 矩阵变换 | ⬜ 待开始 | - |
| Day 14 | 第2周综合 | ⬜ 待开始 | - |
| Day 15 | 微积分动画 | ⬜ 待开始 | - |
| Day 16 | 傅里叶变换 | ⬜ 待开始 | - |
| Day 17 | 几何证明 | ⬜ 待开始 | - |
| Day 18 | 数论可视化 | ⬜ 待开始 | - |
| Day 19 | 复数欧拉 | ⬜ 待开始 | - |
| Day 20 | 物理模拟 | ⬜ 待开始 | - |
| Day 21 | 第3周综合 | ⬜ 待开始 | - |
| Day 22 | 自定义动画 | ⬜ 待开始 | - |
| Day 23 | SVG 处理 | ⬜ 待开始 | - |
| Day 24 | 音频同步 | ⬜ 待开始 | - |
| Day 25 | 分段剪辑 | ⬜ 待开始 | - |
| Day 26 | 插件扩展 | ⬜ 待开始 | - |
| Day 27 | 渲染优化 | ⬜ 待开始 | - |
| Day 28 | 综合项目 | ⬜ 待开始 | - |

---

## 🔧 常用命令参考

```bash
# 低质量预览（开发用，速度快）
manim -pql <文件> <场景名>

# 中质量
manim -pqm <文件> <场景名>

# 高质量（1080p）
manim -pqh <文件> <场景名>

# 4K 输出
manim -pqk <文件> <场景名>

# 导出 GIF
manim -i <文件> <场景名>

# 从特定帧开始预览
manim -pql -n 5 <文件> <场景名>

# 列出文件中所有场景
manim --list <文件>
```

---

## 📚 参考资源

- [Manim Community 官方文档](https://docs.manim.community/)
- [Manim GitHub 仓库](https://github.com/ManimCommunity/manim)
- [3Blue1Brown 原版 manim](https://github.com/3b1b/manim)
- [Manim 示例库](https://docs.manim.community/en/stable/examples.html)

---

## 📝 环境信息

- **Python**: 3.11+
- **Manim**: Community Edition v0.18+
- **Conda 环境名**: `manim-study`
- **系统**: macOS

---

*开始时间：2026-03-24 | 目标完成：2026-04-21*
