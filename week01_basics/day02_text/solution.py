"""
Day 02 练习题参考答案
运行方式：python solution.py
"""

from manim import *

class Exercise1Solution(Scene):
    def construct(self):
        # 创建三行文本
        red_text = Text("Red", color=RED)
        green_text = Text("Green", color=GREEN)
        blue_text = Text("Blue", color=BLUE)
        
        # 垂直排列
        group = VGroup(red_text, green_text, blue_text).arrange(DOWN, buff=0.5)
        
        # 播放动画
        self.play(Write(group), run_time=3)
        self.wait(1)

class Exercise2Solution(Scene):
    def construct(self):
        # 创建求根公式
        # 注意：Raw string (r"") 是处理 LaTeX 转义字符的推荐做法
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=72
        )
        
        # 设置部分着色：x 对应第 0 个字符（或使用 set_color_by_tex）
        formula.set_color_by_tex("x", GOLD)
        
        self.play(Write(formula))
        self.wait(2)

class Exercise3Solution(Scene):
    def construct(self):
        # 1. 初始文本
        intro = Text("Let's solve for x:", font_size=40)
        
        # 2. 目标公式
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=60
        )
        formula.set_color_by_tex("x", GOLD)
        
        # 动画流程
        self.play(Write(intro))
        self.wait(1)
        self.play(Transform(intro, formula)) # 将 intro 变换为 formula 的形状
        self.wait(2)

if __name__ == "__main__":
    # 使用低质量预览模式 (等同于命令行 -pql)
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        # 同时渲染所有练习答案
        for SceneClass in [Exercise1Solution, Exercise2Solution, Exercise3Solution]:
            scene = SceneClass()
            scene.render()
