"""
Day 04: 变换与过渡
学习目标：掌握 Manim 中最核心的变换动画（Transform 系列），
         学习如何让一个物体平滑地“变成”另一个物体，并处理文字变换。
运行方式：python main.py
"""

import sys
import os

# 将项目根目录添加到 python 搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from manim import *
from utils.templates import StudyScene

class Day04TransformDemo(StudyScene):
    """展示 Transform, ReplacementTransform 以及公式变换的典型用法"""

    def construct(self):
        # 0. 欢迎语与项目标识
        self.play_welcome()

        # ==========================================
        # 1. 基础变换：Transform (保留原对象引用)
        # ==========================================
        title_1 = Text("1. 基础变换：Transform", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(title_1))
        
        # 创建一个圆和正方
        circle = Circle(color=WHITE)
        square = Square(color=BLUE)
        
        self.play(Create(circle))
        self.wait(0.5)
        
        # Transform 会让 circle 的外观变成 square 的外观，但 circle 的内部引用依然是 circle
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(FadeOut(circle), FadeOut(title_1))

        # ==========================================
        # 2. 替换变换：ReplacementTransform (销毁原对象)
        # ==========================================
        title_2 = Text("2. 替换变换：ReplacementTransform", font_size=32, color=GREEN).to_edge(UP)
        self.play(Write(title_2))
        
        tri = Triangle(color=YELLOW)
        star = Star(color=RED)
        
        self.play(Create(tri))
        self.wait(0.5)
        
        # 此后 tri 对象的引用会被 star 替换并从场景中移除
        self.play(ReplacementTransform(tri, star))
        self.wait(1)
        self.play(FadeOut(star), FadeOut(title_2))
        
        # ==========================================
        # 3. 混合过渡：FadeTransform
        # ==========================================
        title_3 = Text("3. 混合过渡：FadeTransform", font_size=32, color=GOLD).to_edge(UP)
        self.play(Write(title_3))
        
        rect = Rectangle(width=4, height=2, color=PURPLE)
        circ_red = Circle(radius=1.5, color=RED, fill_opacity=0.5)
        
        self.play(Create(rect))
        self.wait(0.5)
        
        # FadeTransform 是一种淡入淡出结合的变换，适用于形状差异巨大的对象
        self.play(FadeTransform(rect, circ_red))
        self.wait(1)
        self.play(FadeOut(circ_red), FadeOut(title_3))

        # ==========================================
        # 4. 高级：公式文字的“智能”变换
        # ==========================================
        title_4 = Text("4. 逻辑变换：TransformMatchingTex", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(title_4))
        
        # 准备两个分段的公式
        eq1 = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=72)
        eq2 = MathTex("c^2", "=", "a^2", "+", "b^2", font_size=72)
        
        self.play(Write(eq1))
        self.wait(1)
        
        # TransformMatchingTex 会自动寻找相同的子串并互换位置，而不是暴力变形
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1.5)

        # ==========================================
        # 5. 结尾
        # ==========================================
        self.play_finish("Day 04")

if __name__ == "__main__":
    # 使用中等质量预览模式
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day04TransformDemo()
        scene.render()
