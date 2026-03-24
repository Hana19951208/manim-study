"""
Day 01: 基本几何图形
学习目标：掌握 Manim 最基础的图形对象（Circle、Square、Triangle），
         学会将它们添加到场景中并制作简单的动画效果。
运行方式：python main.py
"""

from manim import *


class Day01ShapesDemo(Scene):
    """展示基本几何图形：圆形、正方形、三角形的创建与动画"""

    def construct(self):
        # ==========================================
        # 1. 创建基本图形对象
        # ==========================================

        # 创建一个蓝色圆形（半径默认为 1）
        circle = Circle(radius=1, color=BLUE)

        # 创建一个红色正方形（边长为 2）
        square = Square(side_length=2, color=RED)

        # 创建一个绿色三角形
        triangle = Triangle(color=GREEN)

        # ==========================================
        # 2. 设置位置（让三个图形并排显示）
        # ==========================================
        # 圆形放左边，正方形放中间，三角形放右边
        circle.move_to(LEFT * 3)
        square.move_to(ORIGIN)          # ORIGIN = [0, 0, 0]，即屏幕中心
        triangle.move_to(RIGHT * 3)

        # ==========================================
        # 3. 播放动画：用 Create 动画依次"画出"各图形
        # ==========================================
        # run_time 控制动画持续时间（秒）
        self.play(Create(circle), run_time=1)
        self.play(Create(square), run_time=1)
        self.play(Create(triangle), run_time=1)

        # 等待 1 秒，让观众看清楚
        self.wait(1)

        # ==========================================
        # 4. 同时播放多个动画（并行）
        # ==========================================
        # 让所有图形同时旋转 + 改变颜色
        self.play(
            circle.animate.set_fill(BLUE, opacity=0.5),   # 圆形填充颜色
            square.animate.set_fill(RED, opacity=0.5),    # 正方形填充颜色
            triangle.animate.set_fill(GREEN, opacity=0.5),  # 三角形填充颜色
            run_time=1.5
        )

        self.wait(0.5)

        # ==========================================
        # 5. 让图形移出屏幕（FadeOut）
        # ==========================================
        self.play(
            FadeOut(circle),
            FadeOut(square),
            FadeOut(triangle),
            run_time=1
        )

        # ==========================================
        # 6. 显示标题文字
        # ==========================================
        title = Text("Day 01: 基本图形", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(2)


# ==================================================
# 渲染说明：
#   直接运行 python main.py 即可实现与 
#   manim -pql main.py ShapesDemo 一致的效果
# ==================================================

if __name__ == "__main__":
    # 使用低质量预览模式 (等同于命令行 -pql)
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day01ShapesDemo()
        scene.render()
