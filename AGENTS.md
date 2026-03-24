# AGENTS.md — AI 助理协作规范

## 项目上下文

本项目是一个 **Manim 系统学习计划**，使用 Manim Community Edition 制作数学动画。
- 学习周期：28 天，每天一个技巧
- 语言：Python 3.11+
- conda 环境名：`manim-study`

---

## 🤖 AI 助理工作规则

### 1. 代码规范

- **所有注释使用中文**，确保详细、通俗易懂
- 每个示例文件必须包含 `if __name__ == "__main__"` 的渲染提示注释
- 场景类名使用英文 PascalCase，文件名使用小写下划线
- 每个 `day{{N}}` 文件夹内固定结构：

```
day01_shapes/
├── main.py          # 主要示例代码
├── README.md        # 当日学习笔记和说明
└── output/          # 渲染输出（gitignore）
```

### 2. 渲染命令规范

```bash
# 开发预览（优先使用，速度快）
conda activate manim-study && manim -pql <文件> <场景名>

# 最终输出
manim -pqh <文件> <场景名>
```

### 3. 文件模板

每个 `main.py` 都应遵循以下模板：

```python
"""
Day XX: <主题名称>
学习目标：<具体目标描述>
运行方式：manim -pql main.py <场景类名>
"""

from manim import *


class <场景类名>(Scene):
    """<场景说明>"""
    
    def construct(self):
        # 构建动画逻辑
        pass
```

### 4. 进度更新规则

每完成一天的学习，必须同步更新：
1. `README.md` 中的进度表（⬜ → ✅）
2. 当日目录的 `README.md` 学习笔记
3. `notes/cheatsheet.md` 中新学到的 API

### 5. 目录命名规则

```
week{NN}_{主题}/day{NN}_{英文主题}/
```
例：`week01_basics/day01_shapes/`

---

## 📁 关键文件说明

| 文件 | 用途 |
|------|------|
| `README.md` | 项目总览与进度跟踪 |
| `AGENTS.md` | 本文件，AI 协作规范 |
| `requirements.txt` | Python 依赖声明 |
| `notes/cheatsheet.md` | Manim API 快速手册 |
| `notes/troubleshooting.md` | 常见错误与解决方案 |
| `notes/resources.md` | 学习资源汇总 |

---

## ⚙️ 环境规范

```bash
# 激活环境
conda activate manim-study

# 验证安装
python -c "import manim; print(manim.__version__)"

# 渲染测试
manim -pql week01_basics/day01_shapes/main.py ShapesDemo
```

---

## 🚫 禁止事项

1. **不要**将 `output/` 目录提交到 git
2. **不要**修改 `.gitignore` 中的排除规则
3. **不要**在 `assets/` 之外存储大型媒体文件
4. **不要**跳过当天的 `README.md` 笔记更新

---

## 💡 当有新需求时

如果需要添加新的每日主题，请：
1. 在对应 `week{{N}}_*` 目录下创建文件夹
2. 按模板初始化 `main.py` 和 `README.md`  
3. 同步更新 `README.md` 进度表
4. 在 `notes/resources.md` 中记录参考链接
