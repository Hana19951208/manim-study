import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import StudyScene

"""
Day 06 练习题：精通对象分组与排版

任务 1 (基础): 
    创建 25 个小圆点 (5x5 网格)。
    1. 使用 arrange_in_grid 自动排版。
    2. 使用 set_color_by_gradient 使圆点呈现从左上角到右下角的颜色过渡 (BLUE -> PINK)。
    3. 给整个网格添加一个平滑的旋转动画。

任务 2 (进阶挑战):
    模拟一个“星系模型”。
    1. 创建一个中心大圆（太阳）。
    2. 创建一个 VGroup（轨道组），包含两个圆环轨道。
    3. 在每个轨道上放置一个不同颜色的小圆点（行星）。
    4. 将轨道和行星再次组合成一个 VGroup。
    5. 同时演示行星绕太阳转、行星自转以及整个星系缓缓缩小的效果。

提示:
    1. group[i] 可以精确控制组内特定物体。
    2. VGroup 的嵌套是管理复杂层级的关键。
"""

class Day06Exercise1(StudyScene):
    def construct(self):
        self.play_welcome()
        # 你的任务 1 代码写在这里
        pass

class Day06Exercise2(StudyScene):
    def construct(self):
        # 你的任务 2 代码写在这里
        pass

if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day06Exercise1()
        scene.render()
