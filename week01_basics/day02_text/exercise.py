"""
Day 02 练习题：文本与数学公式巩固
学习目标：掌握 Text, MathTex 的基本用法及简单变换
运行方式：python exercise.py
"""

from manim import *

class Day02Exercise1(Scene):
    """
    练习 1：多行彩色文本
    任务：创建三行文本，内容分别为 "Red", "Green", "Blue"
    要求：每行文本的颜色需与其内容对应，三行垂直排列，并带有逐字书写动画。
    """
    def construct(self):
        # 请在此处编写你的代码
        redText = Text("Red",font_size=42).set_color(RED);
        greenText = Text("Green",font_size=42).set_color(GREEN);
        blueText = Text("Blue",font_size=42).set_color(BLUE);
        
        text_group = VGroup(redText, greenText, blueText);

        text_group.arrange(DOWN,buff=0.5);

        self.play(Write(redText));
        self.wait(0.1);
        self.play(Write(greenText));
        self.wait(0.1);
        self.play(Write(blueText));
        
        self.wait(1);

        self.play(text_group.animate.scale(0.5).to_corner(UL),run_time=1.5);
        
        self.wait(0.5);
        self.play(FadeOut(redText));
        self.wait(0.1);
        self.play(FadeOut(greenText));
        self.wait(0.1);
        self.play(FadeOut(blueText));

class Day02Exercise2(Scene):
    """
    练习 2：经典的求根公式
    任务：使用 MathTex 渲染公式：x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    要求：将变量 x 设为金色 (GOLD)，公式居中显示，使用 Write 动画展现。
    """
    def construct(self):
        # 请在此处编写你的代码
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",font_size=42,color=GOLD);
        self.play(Write(formula));
        self.wait(1);
        self.play(FadeOut(formula));

class Day02Exercise3(Scene):
    """
    练习 3：从文字到公式的变换
    任务：
    1. 先在屏幕中心显示 Text "Let's solve for x:"
    2. 等待 1 秒后，将其变换 (Transform) 为练习 2 中的求根公式。
    """
    def construct(self):
        # 请在此处编写你的代码
        text = Text("Let's solve for x:",font_size=42);
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",font_size=42,color=GOLD);
        self.play(Write(text));
        self.wait(1);
        self.play(Transform(text,formula,run_time=0.5));
        self.wait(1);
        text2 = Text("Let's Transform !!!",font_size=42);
        self.play(Transform(text,text2,run_time=0.5));
        self.wait(1);
        self.play(FadeOut(text));


if __name__ == "__main__":
    # 使用低质量预览模式 (等同于命令行 -pql)
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        # 默认运行第 1 个练习，你可以手动修改此处来运行不同的场景
        scene = Day02Exercise3() 
        scene.render()
