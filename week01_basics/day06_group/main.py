import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import StudyScene

class Day06GroupBasicDemo(StudyScene):
    """
    入门级：基础 VGroup 与 arrange 排版
    """
    def construct(self):
        self.play_welcome()

        # 1. 创建多个形状
        shapes = [Circle(), Square(), Triangle(), Star()]
        # 赋予不同颜色
        for shape, color in zip(shapes, [RED, GREEN, BLUE, GOLD]):
            shape.set_fill(color, opacity=0.5)

        # 2. 将它们组合成 VGroup
        # VGroup 是 Vectorized Group 的缩写，专门处理 VMobject
        group = VGroup(*shapes)

        # 3. 使用 arrange 进行对齐
        # buff 参数控制间距
        group.arrange(RIGHT, buff=0.5)
        self.play(Create(group))
        self.wait(1)

        # 4. 演示整体缩放和旋转
        # 你可以像操作单个物体一样操作 VGroup
        self.play(group.animate.scale(0.5).rotate(PI/4))
        self.wait(1)
        
        self.play_finish("Day 06 Basic")

class Day06GroupAdvancedDemo(StudyScene):
    """
    进阶级：网格布局 (arrange_in_grid) 与嵌套分组
    """
    def construct(self):
        # 1. 使用列表推导式批量创建 12 个正方形
        squares = VGroup(*[Square(side_length=1) for _ in range(12)])
        
        # 2. 排列为 3 行 4 列的网格
        squares.arrange_in_grid(rows=3, cols=4, buff=0.2)
        self.play(DrawBorderThenFill(squares))
        self.wait(1)

        # 3. 嵌套分组：选择其中一行
        row1 = squares[0:4] # 第 0 到 3 个正方形
        self.play(row1.animate.set_color(YELLOW).scale(1.2))
        self.wait(1)

        # 4. 针对整个网格应用动画，同时保持子分组的相对关系
        self.play(squares.animate.shift(UP * 1).rotate(PI/8))
        self.wait(1)

class Day06GroupDeepDemo(StudyScene):
    """
    深度解析：批量动画 (LaggedStart) 与 Group vs VGroup
    """
    def construct(self):
        # 1. 创建大量的点阵 (30x30 = 900个点)
        # 注意：处理大量点时，VGroup 的性能非常重要
        dots = VGroup(*[
            Dot(radius=0.05, color=interpolate_color(BLUE, PINK, np.random.random()))
            for _ in range(200)
        ])
        dots.arrange_in_grid(rows=10, cols=20, buff=0.1)
        self.add(dots)
        self.wait(1)

        # 2. 批量动画技巧：LaggedStart
        # 让所有点按顺序依次放大
        self.play(
            LaggedStart(
                *[d.animate.scale(2) for d in dots],
                lag_ratio=0.01, # 控制每个动画开始的延迟
                run_time=3
            )
        )
        self.wait(1)

        # 3. 颜色梯度批量设置 (set_color_by_gradient)
        # 这是 VGroup 的专属魔法，普通 Group 不支持
        self.play(dots.animate.set_color_by_gradient(RED, YELLOW, GREEN))
        self.wait(2)

if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day06GroupAdvancedDemo()
        scene.render()
