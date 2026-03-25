from manim import *

# Day 03 练习：颜色与渐变
# 任务目标：
# 1. 创建两个几何图形，一个使用 Hex 颜色，一个使用 RGB 颜色，并设置不同的透明度 (Opacity)。
# 2. 创建一个由 5 个圆圈组成的水平行，它们的颜色从 RED_A 渐变到 RED_E。
# 3. 创建一个大的 "Manim Color" 文字，使用从蓝色到绿色再到黄色的多重渐变效果。

class Day03Exercise1(Scene):
    """
    练习 1：基础颜色设置与透明度
    任务：
    - 在左侧创建一个 Square，颜色设置为 "#00FF00" (Hex)，填充透明度为 0.8。
    - 在右侧创建一个 Circle，颜色使用 RGB [1, 0, 0.5]，填充透明度为 0.3。
    """
    def construct(self):
        # 在此处编写你的代码
        title = Text("1：基础颜色设置与透明度", font_size=42, weight=BOLD).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        square = Square(
            stroke_color="#00FF00",
            fill_color="#00FF00",
            fill_opacity=0.8
        ).move_to(LEFT * 2)

        self.play(Create(square))
        self.play(FadeOut(square))
        self.wait(1)
        
        circle = Circle(
            stroke_color=BLUE_B,
            fill_color=BLUE_B,
            fill_opacity=0.3
        ).move_to(RIGHT * 2)

        self.play(Create(circle))
        self.wait(1)


class Day03Exercise2(Scene):
    """
    练习 2：深浅色系的应用
    任务：
    - 使用 VGroup 创建 5 个 Circle。
    - 分别设置它们的颜色为 RED_A, RED_B, RED_C, RED_D, RED_E。
    - 将它们水平排列 (arrange)。
    """
    def construct(self):
        colors = [RED_A, RED_B, RED_C, RED_D, RED_E]
        five_circle = VGroup(*[
            Circle(fill_color=colors[0], fill_opacity=1, stroke_width=0) 
            for _ in colors
        ])
        five_circle.arrange(RIGHT, buff=0.2)
        
        self.play(FadeIn(five_circle, shift=UP))
        self.wait(0.5)

        # 依次把每个圆变成对应颜色，形成渐变流动
        for i, c in enumerate(colors):
            self.play(
                five_circle[i].animate.set_color(c),
                run_time=0.6
            )
        
        self.wait(2)
        self.play(FadeOut(five_circle))

class Day03Exercise3(Scene):
    """
    练习 3：多色渐变动画
    任务：
    - 创建一个 MathTex("f(x) = \\int y dx") 或普通 Text("Gradient")。
    - 使用 set_color_gradient() 设置从 Blue 到 Green 再到 Yellow 的渐变。
    - 使用 Write 动画显示。
    """
    def construct(self):
        # 在此处编写你的代码
        text = MathTex(r"f(x) = \int y dx",font_size=72)
        text.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
        self.play(Write(text),run_time=2)
        self.wait(0.5)
        self.play(FadeOut(text))

if __name__ == "__main__":
    # 使用低质量预览模式渲染 Exercise 1
    with tempconfig({"quality": "low_quality", "preview": True,"flush_cache": True, "input_file": __file__}):
        scene = Day03Exercise3()
        scene.render()
