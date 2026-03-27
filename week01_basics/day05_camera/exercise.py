import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import MovingCameraStudyScene

"""
Day 05 练习题：由浅入深掌握摄像机控制

任务 1 (基础): 
    创建三个 Text 对象，分别在坐标 (-3, 2), (0, 0), (3, -2)。
    要求摄像机按顺序依次平滑切换到这三个物体，并在每个物体处停留 1 秒，
    最后回到全局视角。

任务 2 (进阶挑战):
    模拟一个“星系”的一部分。在屏幕中心创建一个大的黄色圆形（太阳），
    创建一个小的蓝色圆形（地球）绕其公转。
    要求摄像机实时追踪蓝色圆形（地球），即地球始终在镜头中心，
    而太阳看起来在背景中移动。

提示:
    1. 使用 self.camera.frame.animate.move_to() 来切换焦距。
    2. 使用 add_updater() 来动态捕捉位置。
"""

class Day05Exercise1(MovingCameraStudyScene):
    def construct(self):
        self.play_welcome()
        # 你的任务 1 代码写在这里
        # 创建三个 Text 对象，分别在坐标 (-3, 2), (0, 0), (3, -2)。
        # 要求摄像机按顺序依次平滑切换到这三个物体，并在每个物体处停留 1 秒，
        # 最后回到全局视角。
        text1 = Text("Step 1").shift(UP*2 + LEFT*3)
        text2 = Text("Step 2").shift(ORIGIN)
        text3 = Text("Step 3").shift(DOWN*2 + RIGHT*3)
        self.add(text1, text2, text3)
        self.play(self.camera.frame.animate.move_to(text1).set_width(text1.width * 3), run_time=2)
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(text2).set_width(text2.width * 3), run_time=2)
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(text3).set_width(text3.width * 3), run_time=2)
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set_width(14), run_time=2)
        self.wait(1)
        

class Day05Exercise2(MovingCameraScene):
    def construct(self):
        # 你的任务 2 代码写在这里
        # 模拟一个“星系”的一部分。在屏幕中心创建一个大的黄色圆形（太阳），
        # 创建一个小的蓝色圆形（地球）绕其公转。
        # 要求摄像机实时追踪蓝色圆形（地球），即地球始终在镜头中心，
        # 而太阳看起来在背景中移动。
        plane = NumberPlane()
        sun = Circle(radius=1, color=YELLOW).shift(ORIGIN)
        earth = Circle(radius=0.2, color=BLUE).shift(RIGHT * 3)
        self.add(plane, sun, earth)
        
        earth.add_updater(lambda m, dt: m.rotate(dt * (TAU / 5), about_point=sun.get_center()))
        
        def update_camera(m):
            earth_pos = earth.get_center()
            m.move_to(earth_pos)
            angle = angle_of_vector(earth_pos)
            m.set(angle=angle - PI / 2)
            
        self.camera.frame.add_updater(update_camera)
        self.add(self.camera.frame)
        self.wait(5)
    


if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day05Exercise2() # 切换类名进行预览
        scene.render()
