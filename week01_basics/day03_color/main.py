"""
Day 03: 颜色与渐变
学习目标：学习颜色系统，掌握 set_color_gradient() 和颜色深浅分级。
运行方式：python main.py
"""

import sys
import os

# 将项目根目录添加到 python 搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from manim import *
from utils.templates import StudyScene


class Day03ColorDemo(StudyScene):
    def construct(self):
        # 0. 欢迎语与通用标识
        self.play_welcome()

        # 1. 标题（使用带有渐变的文字）
        title = Text("Day 03: 颜色与渐变", font_size=42, weight=BOLD)
        title.set_color_by_gradient(BLUE, GREEN) # 文字渐变
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

        # 3. 形状渐变 (Sheen 方案)
        # set_sheen 可以在单一物体上产生类似金属光泽的线性渐变感
        ring = Annulus(inner_radius=1.0, outer_radius=1.5, fill_opacity=1)
        # 设置底色并添加“极化光泽”方能看到明显的色彩跨度
        ring.set_color(PURPLE)
        ring.set_sheen(1.0, direction=UR) # 设置 1.0 的光泽强度，方向朝向右上角
        
        ring_label = Text("线性光泽渐变", font_size=24).next_to(ring, DOWN)
        self.play(Create(ring), Write(ring_label))
        # 旋转时，你会发现光泽会随着旋转产生动态变化
        self.play(Rotate(ring, angle=TAU, run_time=3)) 
        self.wait(1)
        self.play(FadeOut(ring), FadeOut(ring_label))

        # 4. 多色径向渐变 (VGroup 细分方案)
        # 要想让一个圆形内部充满彩虹，最好的办法是把它画成“一圈一圈”的
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        rainbow_circle = VGroup(*[
            Annulus(inner_radius=i/10, outer_radius=(i+1)/10, fill_opacity=0.8)
            .set_color(colors[i % len(colors)])
            for i in range(20) # 创建 20 层极细的圆环
        ])
        
        finish_text = Text("多层径向彩虹", font_size=32).move_to(rainbow_circle.get_center())
        
        # 这种写法不仅效果完美，文字在上面也会非常清晰
        self.play(Create(rainbow_circle, lag_ratio=0.1), run_time=2)
        self.play(Write(finish_text))
        self.wait(1)
        self.play(FadeOut(rainbow_circle), FadeOut(finish_text))

        finish_text = Text("自定义色彩系统", font_size=32).move_to(rainbow_circle.get_center())
        
        self.play(DrawBorderThenFill(rainbow_circle))
        self.play(Write(finish_text))
        self.wait(2)

        # 5. 结尾（使用模板方法）
        self.play_finish("Day 03")

if __name__ == "__main__":
    # 使用中等质量预览模式 (等同于命令行 -pqm)
    with tempconfig({"quality": "medium_quality", "preview": True, "input_file": __file__}):
        scene = Day03ColorDemo()
        scene.render()
