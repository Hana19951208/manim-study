from manim import *

# Day 03 参考答案：颜色与渐变
# 每个场景均提供了上述任务的标准实现方式。

class Day03Solution1(Scene):
    """
    练习 1：基础颜色设置与透明度
    任务：
    - 在左侧创建一个 Square，颜色设置为 "#00FF00" (Hex)，填充透明度为 0.8。
    - 在右侧创建一个 Circle，颜色使用 RGB [1, 0, 0.5]，填充透明度为 0.3。
    """
    def construct(self):
        # 创建一个 Hex 颜色的 Square
        square = Square(color="#00FF00")
        square.set_fill("#00FF00", opacity=0.8) # 设置填充透明度
        square.shift(LEFT * 2)

        # 使用 RGB 创建颜色，Manim 的颜色列表本质上是字符串，
        # RGB 可以通过 rgb_to_color 将一个 [0-1] 的列表转换为颜色字符串
        rgb_color = rgb_to_color([1, 0, 0.5])
        circle = Circle(color=rgb_color)
        circle.set_fill(rgb_color, opacity=0.3)
        circle.shift(RIGHT * 2)

        # 添加到场景中
        self.play(Create(square), Create(circle))
        self.wait(2)

class Day03Solution2(Scene):
    """
    练习 2：深浅色系的应用
    任务：
    - 使用 VGroup 创建 5 个 Circle。
    - 分别设置它们的颜色为 RED_A, RED_B, RED_C, RED_D, RED_E (浅 -> 深)。
    - 将它们水平排列 (arrange)。
    """
    def construct(self):
        # 使用不同的 RED 系列颜色创建圆圈
        # RED_A (最浅), RED_B, RED_C (标准 RED), RED_D, RED_E (最深)
        colors = [RED_A, RED_B, RED_C, RED_D, RED_E]
        
        # 批量创建
        circles = VGroup(*[
            Circle(radius=0.5, color=c).set_fill(c, opacity=1) 
            for c in colors
        ])
        
        # 水平排列
        circles.arrange(RIGHT, buff=0.5)
        
        # 演示显示
        self.play(FadeIn(circles, shift=UP))
        self.wait(2)

class Day03Solution3(Scene):
    """
    练习 3：多色渐变效果
    任务：
    - 创建一个大的 "Manim Color" 文字，使用从蓝色到绿色再到黄色的多重渐变效果。
    """
    def construct(self):
        # 创建文字
        text = Text("Manim Color Gradient", font_size=72)
        
        # 使用 set_color_by_gradient() 给文字设置多重渐变
        # 提示：VMobject 类型通用的方法是 set_color_by_gradient() 或 set_color_gradient()
        # 这里使用了 Blue -> Green -> Yellow 三重渐变
        text.set_color_by_gradient(BLUE, GREEN, YELLOW)
        
        # 背景装饰：一个带渐变的圆圈
        bg_circle = Circle(radius=3, stroke_width=8)
        bg_circle.set_color_by_gradient(YELLOW, GREEN, BLUE) # 与文字相反的渐变
        
        # 动画展示
        self.play(Write(text), Create(bg_circle), run_time=3)
        self.wait(2)

if __name__ == "__main__":
    # 使用低质量预览模式渲染所有解决方案
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scenes = [Day03Solution1(), Day03Solution2(), Day03Solution3()]
        for scene in scenes:
            scene.render()
