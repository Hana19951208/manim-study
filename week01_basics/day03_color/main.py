"""
Day 03: 颜色与渐变
学习目标：学习颜色系统，掌握 set_color_gradient() 和颜色深浅分级。
运行方式：python main.py
"""

from manim import *

class Day03ColorDemo(Scene):
    def construct(self):
        # 1. 标题（使用带有渐变的文字）
        title = Text("Day 03: 颜色与渐变", font_size=42, weight=BOLD)
        title.set_color_gradient(BLUE, GREEN) # 文字渐变
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 2. 颜色深浅展示 (Color Gradients)
        # 展示 BLUE 从 A (浅) 到 E (深) 的五个级别
        blue_blocks = VGroup(*[
            Rectangle(width=1, height=1, fill_opacity=1, color=c)
            for c in [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        ])
        blue_blocks.arrange(RIGHT, buff=0.2)
        blue_label = Text("蓝色分级 (BLUE_A → BLUE_E)", font_size=20).next_to(blue_blocks, UP)
        
        self.play(FadeIn(blue_label), Create(blue_blocks))
        self.wait(1.5)
        self.play(FadeOut(blue_blocks), FadeOut(blue_label))

        # 3. 形状渐变 (set_color_gradient)
        # 一个从紫色渐变到红色的圆环
        ring = Annulus(inner_radius=1.0, outer_radius=1.5)
        ring.set_color_gradient(PURPLE, RED) # 整体渐变
        
        ring_label = Text("线性渐变效果", font_size=24).next_to(ring, DOWN)
        self.play(Create(ring), Write(ring_label))
        self.play(ring.animate.rotate(PI)) # 旋转渐变物体
        self.wait(1)
        self.play(FadeOut(ring), FadeOut(ring_label))

        # 4. 多色径向渐变 (结合坐标系)
        # 创建一个受多色填充的大圆
        rainbow_circle = Circle(radius=2, fill_opacity=0.8)
        # 除了两个色，还可以传一整组颜色列表实现“彩虹”效果
        rainbow_circle.set_color_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        
        finish_text = Text("自定义色彩系统", font_size=32).move_to(rainbow_circle.get_center())
        
        self.play(DrawBorderThenFill(rainbow_circle))
        self.play(Write(finish_text))
        self.wait(2)

        # 5. 结尾
        self.play(*[FadeOut(m) for m in self.mobjects])
        
        end_msg = Text("✓ Day 03 预览准备就绪！", color=GREEN)
        self.play(FadeIn(end_msg))
        self.wait(1.5)

if __name__ == "__main__":
    # 使用中等质量预览模式 (等同于命令行 -pqm)
    with tempconfig({"quality": "medium_quality", "preview": True, "input_file": __file__}):
        scene = Day03ColorDemo()
        scene.render()
