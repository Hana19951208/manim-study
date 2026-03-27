import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import StudyScene

class Day06Exercise1(StudyScene):
    """
    任务 1 解答：渐变网格
    """
    def construct(self):
        self.play_welcome()
        
        # 1. 创建并排版
        dots = VGroup(*[Dot(radius=0.1) for _ in range(25)])
        dots.arrange_in_grid(rows=5, cols=5, buff=0.5)
        
        # 2. 应用渐变
        dots.set_color_by_gradient(BLUE, PINK)
        
        # 3. 动画演示
        self.play(DrawBorderThenFill(dots))
        self.play(dots.animate.rotate(TAU/4).scale(1.5), run_time=2)
        self.wait(1)
        
        self.play_finish("Ex 1")

class Day06Exercise2(StudyScene):
    """
    任务 2 解答：嵌套星系模型
    """
    def construct(self):
        # 1. 创建星系结构
        sun = Dot(color=YELLOW, radius=0.4)
        
        # 轨道组
        orbit1 = Circle(radius=2, color=WHITE).set_stroke(opacity=0.2)
        planet1 = Dot(color=BLUE, radius=0.15).move_to(orbit1.point_from_proportion(0))
        
        orbit2 = Circle(radius=3, color=WHITE).set_stroke(opacity=0.2)
        planet2 = Dot(color=MAROON, radius=0.2).move_to(orbit2.point_from_proportion(0))
        
        system = VGroup(sun, orbit1, planet1, orbit2, planet2)
        self.add(system)

        # 2. 增加动态逻辑 (Updater)
        # 让行星绕轨道旋转
        planet1.add_updater(lambda m, dt: m.rotate(dt * 1.5, about_point=ORIGIN))
        planet2.add_updater(lambda m, dt: m.rotate(dt * 0.8, about_point=ORIGIN))
        
        # 3. 演示整体缩放
        self.play(system.animate.scale(0.6).shift(UP * 0.5), run_time=3)
        self.wait(2)
        
        # 4. 回复
        self.play(system.animate.scale(1.5).shift(DOWN * 0.5), run_time=2)
        
        # 清理
        planet1.clear_updaters()
        planet2.clear_updaters()
        self.play_finish("Ex 2")

if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day06Exercise2()
        scene.render()
