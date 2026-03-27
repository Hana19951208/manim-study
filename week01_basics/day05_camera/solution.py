import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import MovingCameraStudyScene

class Day05Exercise1(MovingCameraStudyScene):
    """
    任务 1 解答：多目标平滑切换
    """
    def construct(self):
        self.play_welcome()
        
        # 1. 创建目标
        t1 = Text("目标 1").shift(LEFT * 3 + UP * 2)
        t2 = Text("目标 2").shift(ORIGIN)
        t3 = Text("目标 3").shift(RIGHT * 3 + DOWN * 2)
        self.add(t1, t2, t3)
        self.wait(1)

        # 2. 依次平滑切换相镜
        targets = [t1, t2, t3]
        for target in targets:
            self.play(
                self.camera.frame.animate.move_to(target).set_width(target.width * 2.5),
                run_time=2
            )
            self.wait(1)

        # 3. 回到原始视角
        self.play(self.camera.frame.animate.move_to(ORIGIN).set_width(14), run_time=2)
        self.wait(1)
        self.play_finish("Ex 1")

class Day05Exercise2(MovingCameraStudyScene):
    """
    任务 2 解答：实时追踪动画
    """
    def construct(self):
        # 1. 场景设置
        sun = Dot(color=YELLOW, radius=0.5).move_to(ORIGIN)
        earth = Dot(color=BLUE, radius=0.2).shift(RIGHT * 3)
        self.add(sun, earth)
        
        # 装饰性背景网格（为了看出相对运动）
        grid = NumberPlane(background_line_style={"stroke_opacity": 0.2})
        self.add(grid)

        # 2. 地球公转更新逻辑
        def rotate_earth(mob, dt):
            mob.rotate(dt * 1, about_point=ORIGIN)
        earth.add_updater(rotate_earth)

        # 3. 相机追踪地球更新逻辑
        self.camera.frame.add_updater(lambda f: f.move_to(earth.get_center()))
        
        # 播放 5 秒
        self.wait(5)
        
        # 停止追踪和旋转
        earth.remove_updater(rotate_earth)
        self.camera.frame.clear_updaters()
        
        # 完成
        self.play(FadeOut(earth), FadeOut(sun), FadeOut(grid))
        self.play_finish("Ex 2")

if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day05Exercise2()
        scene.render()
