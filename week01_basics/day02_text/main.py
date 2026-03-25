"""
Day 02: 文字与 LaTeX
学习目标：掌握 Manim 中的文字渲染，包括普通文字（Text）和
         数学公式（MathTex / Tex），并学会控制字体、大小、颜色、位置。
运行方式：python main.py
"""

import sys
import os

# 将项目根目录添加到 python 搜索路径（针对直接运行脚本的情况）
# week01_basics / day02_text / main.py -> 所以要向上退两级到根目录
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from manim import *
from utils.templates import StudyScene


class Day02TextDemo(StudyScene):
    """展示 Text、Tex、MathTex 三种文字类的用法和差异"""

    # 继承自 StudyScene，可以通过以下参数控制模板显示
    # show_header = True  # 设置为 False 可关闭欢迎语
    # show_footer = True  # 设置为 False 可关闭结尾动画

    def construct(self):
        # ==========================================
        # 0. 欢迎语与通用标识（由模板 StudyScene 提供）
        # ==========================================
        self.play_welcome()


        # ==========================================
        # 1. Text：普通文字（不依赖 LaTeX，支持中文）
        # ==========================================

        # 创建标题（加粗、黄色）
        title = Text("Day 02: 文字与公式", font_size=42, color=YELLOW, weight=BOLD)
        self.play(Write(title))
        self.wait(0.8)

        # 标题移到顶部
        self.play(title.animate.to_edge(UP))
        self.wait(0.3)

        # ==========================================
        # 2. Text 的颜色分段（t2c 参数）
        # ==========================================

        # t2c：对指定文字片段单独上色
        colored_text = Text(
            "Manim = Math + Animation",
            font_size=36,
            t2c={
                "Math": BLUE,        # "Math" 部分用蓝色
                "Animation": GREEN,  # "Animation" 部分用绿色
            }
        )
        self.play(FadeIn(colored_text))
        self.wait(1)
        self.play(FadeOut(colored_text))

        # ==========================================
        # 3. MathTex：LaTeX 数学公式渲染
        # ==========================================

        # 欧拉公式：e^{i\pi} + 1 = 0
        euler = MathTex(
            r"e^{i\pi} + 1 = 0", 
            font_size=60, 
            color=GOLD,
            substrings_to_isolate=["e"]  # 告诉 Manim：把 "e" 单独拎出来
        )
        self.play(Write(euler), run_time=2)
        self.wait(0.5)


        # 为公式的各个部分单独上色
        # MathTex 可以通过索引访问各部分
        self.play(euler.animate.set_color_by_tex("e", WHITE))
        self.wait(0.5)

        self.play(FadeOut(euler))

        # ==========================================
        # 4. MathTex 分段着色：对齐公式推导
        # ==========================================

        # 分步展示二次公式
        formula_title = Text("二次方程求根公式", font_size=32, color=WHITE)
        formula_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(formula_title))

        # 公式本体
        quadratic = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=52,
            color=BLUE_B
        )
        self.play(Write(quadratic), run_time=2)
        self.wait(1.5)

        # ==========================================
        # 5. 多行公式（使用 aligned 环境）
        # ==========================================
        self.play(FadeOut(formula_title), FadeOut(quadratic))

        multiline = MathTex(
            r"(a+b)^2 &= a^2 + 2ab + b^2 \\",
            r"(a-b)^2 &= a^2 - 2ab + b^2",
            font_size=40
        )
        multiline.move_to(ORIGIN)
        self.play(Write(multiline), run_time=2)
        self.wait(1.5)

        # ==========================================
        # 6. 公式变换动画（TransformMatchingTex）
        # ==========================================
        self.play(FadeOut(multiline))

        # 从左边的表达式变换到右边的
        # 通过将公式拆分为多个字符串，TransformMatchingTex 能更精准地匹配组件
        expr1 = MathTex("x", "^2", "+", "2", "x", "+", "1", font_size=64)
        expr2 = MathTex("(", "x", "+", "1", ")", "^2", font_size=64)

        label = Text("因式分解", font_size=28, color=GRAY).next_to(expr1, UP)
        self.play(Write(expr1), FadeIn(label))
        self.wait(0.8)

        # 现在你会看到：x、+、1、^2 这些字符会平滑地“飞向”新位置！
        self.play(
            TransformMatchingTex(expr1, expr2),
            label.animate.set_opacity(0)
        )
        self.wait(1.5)

        # ==========================================
        # 7. 结尾（使用模板方法）
        # ==========================================
        self.play_finish("Day 02")


# ==================================================
# 渲染说明：
#   直接运行 python main.py 即可实现与 
#   manim -pql main.py TextDemo 一致的效果
# ==================================================

if __name__ == "__main__":
    # 使用低质量预览模式 (等同于命令行 -pql)
    # 增加 input_file=__file__ 确保输出路径带上脚本名目录
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day02TextDemo()
        scene.render()