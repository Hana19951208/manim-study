import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.templates import MovingCameraStudyScene

class Day05CameraBasicDemo(MovingCameraStudyScene):
    """
    入门级：演示摄像机帧 (camera.frame) 的基本平移与缩放
    """
    show_header = False
    show_footer = False
    def construct(self):
        # 0. 欢迎语
        self.play_welcome()

        # 1. 创建背景网格和一些物体
        grid = NumberPlane()
        dot = Dot(color=RED).scale(2)
        circle = Circle(radius=1, color=BLUE).shift(RIGHT * 3)
        square = Square(side_length=1, color=GREEN).shift(LEFT * 3 + UP * 2)
        
        self.add(grid, dot, circle, square)
        self.wait(1)

        # 2. 演示摄像机平移 (Shift)
        # 镜头向右移动，效果效果等同于所有物体向左移动
        self.play(self.camera.frame.animate.shift(RIGHT * 3), run_time=2)
        self.wait(1)

        # 3. 演示摄像机缩放 (Scale/Zoom)
        # set_width(n) 会调整相机视野宽度。值越小，镜头越聚焦（放大）
        self.play(self.camera.frame.animate.set_width(5), run_time=2)
        self.wait(1)

        # 4. 回到初始视角
        self.play(self.camera.frame.animate.set_width(14).move_to(ORIGIN), run_time=2)
        self.wait(1)
        
        self.play_finish("Day 05 Basic")

class Day05CameraAdvancedDemo(MovingCameraStudyScene):
    """
    进阶级：演示 save_state, restore 和多目标平滑切换
    """
    def construct(self):
        grid = NumberPlane()
        self.add(grid) 
        # 准备物体
        objs = VGroup(
            Tex("Step 1").shift(UP*2 + LEFT*3),
            Tex("Step 2").shift(ORIGIN),
            Tex("Step 3").shift(DOWN*2 + RIGHT*3)
        )
        self.add(objs)

        # 保存初始相机状态
        self.camera.frame.save_state()

        # 依次聚焦到各个物体
        for obj in objs:
            self.play(
                self.camera.frame.animate.move_to(obj).set_width(obj.width * 3),
                run_time=1.5
            )
            self.wait(1)

        # 恢复初始状态
        self.play(Restore(self.camera.frame), run_time=2)
        self.wait(1)

class Day05CameraDeepDemo(MovingCameraStudyScene):
    """
    深度解析：动态追踪与视角旋转 (Rotate)
    """
    def construct(self):
        grid = NumberPlane()
        # 创建一个不动的参考点
        ref_dot = Dot(color=RED).shift(UP * 2) 
        
        path = Circle(radius=3, color=WHITE).set_stroke(opacity=0.3)
        dot = Dot(color=YELLOW).scale(2).move_to(path.point_from_proportion(0))
        
        self.add(grid, ref_dot, path, dot)

        # 1. 点绕圆心转，4秒一圈
        dot.add_updater(lambda m, dt: m.rotate(dt * (TAU / 4), about_point=ORIGIN))
        
        # 2. 相机追踪（实现：黄色点静止在中心，红色点和网格旋转）
        def update_camera(frame):
            pos = dot.get_center()
            frame.move_to(pos)

            # 黄点相对圆心的位置角度
            theta = angle_of_vector(pos)

            # 圆周运动的切线方向 = 半径方向 + PI/2
            # 为了让画面看起来像“朝前走”，通常要再根据你的视觉习惯微调
            frame.set_angle(theta - PI / 2)

        self.camera.frame.add_updater(update_camera, call_updater=True)

        # 关键：把 camera.frame 加入 scene，
        # 这样 wait(4) 时它的 updater 才会真的每帧执行
        self.add(self.camera.frame)

        self.wait(4)


if __name__ == "__main__":
    # 使用低质量预览模式
    from manim import tempconfig
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        # 渲染其中一个场景
        scene = Day05CameraDeepDemo()
        scene.render()
    # import manimpango
    # fonts = manimpango.list_fonts()
    # print([f for f in fonts if "PT Serif" in f])