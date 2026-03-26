from manim import *

# Day 04 练习：变换与过渡 (Transformations & Transitions)
# 任务目标：
# 1. 实现一个三级跳变换：圆形 -> 正方形 -> 三角形，要求使用 ReplacementTransform 且颜色随之改变。
# 2. 使用 FadeTransform 实现两个完全不同类型物体（如 Star 和 Ring）之间的平滑过渡。
# 3. 制作一个分配律公式推导：a(b+c) = ab + ac，要求使用 TransformMatchingTex 实现字母的平滑位移。

class Day04Exercise1(Scene):
    """
    练习 1：多级替换变换
    任务：
    - 在中心创建一个蓝色 Circle。
    - 将其变换为红色的 Square。
    - 再将其变换为绿色的 Triangle。
    - 每次变换后等待 0.5 秒。
    """
    def construct(self):
        # 在此处编写你的代码
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)

        self.play(Create(circle))
        self.wait(0.5)
        self.play(Transform(circle,square))
        self.wait(0.5)
        self.play(Transform(circle,triangle))
        self.wait(0.5)

class Day04Exercise2(Scene):
    """
    练习 2：淡入淡出过渡 (FadeTransform)
    任务：
    - 创建一个黄色的 Star。
    - 使用 FadeTransform 将其变换为一个紫色的 Annulus (圆环)。
    - 体会 FadeTransform 与普通 Transform 在处理异形物体时的视觉差异。
    """
    def construct(self):
        # 在此处编写你的代码
        star = Star(color=YELLOW).set_fill(YELLOW)
        annulus = Annulus(color=PURPLE).set_fill(PURPLE)
        self.play(Create(star))
        self.wait(0.5)
        self.play(FadeTransform(star,annulus))
        self.play(FadeOut(annulus))

class Day04Exercise3(Scene):
    """
    练习 3：智能公式位移 (TransformMatchingTex)
    任务：
    - 创建公式 A：a(b+c)
    - 创建公式 B：ab + ac
    - 使用 TransformMatchingTex 将 A 变为 B。
    - 提示：定义 MathTex 时，需要巧妙地拆分字符串片段以帮助 Manim 识别匹配项。
    """
    def construct(self):
        # 在此处编写你的代码
        eqa = MathTex("a", "(" ,"b","+","c",")")
        eqb = MathTex("a" ,"b","+","a","c")
        self.play(Write(eqa))
        self.wait(0.5)
        self.play(TransformMatchingTex(eqa,eqb))
        self.play(FadeOut(eqb))

class Day04Exercise4(Scene):
    """
    练习 4（进阶）：几何图形 -> 文字的丝滑变换
    任务：
    - 创建一个由 4 个彩色 Dot 组成的正方形阵列。
    - 使用变换动画将这 4 个点“平滑”地变成四个字母 "CODE"。
    - 难点：处理 VGroup 内部组件的一一对应关系，建议使用 ReplacementTransform 或直接对 Group 进行变换。
    """
    def construct(self):
        # 在此处编写你的代码
        dots = VGroup(*[
            Dot(color=c, radius=0.2) 
            for c in [BLUE, GREEN, RED, YELLOW]
        ]).arrange(RIGHT, buff=1)
        self.play(Create(dots))
        self.wait(0.5)
        letters = VGroup(*[
            Text(l, font_size=80, color=dots[i].get_color()) 
            for i, l in enumerate(["C", "O", "D", "E"])
        ]).arrange(RIGHT, buff=1)
        self.play(ReplacementTransform(dots, letters), run_time=2)
        self.wait(2)
        self.play(FadeOut(letters))
        

class Day04Exercise5(Scene):
    """
    练习 5（思考）：路径与属性的联动变换
    任务：
    - 创建一个粗边框的红色圆。
    - 在 2 秒内将其变换为一个细边框的黄色三角形。
    - 同时让它在变换过程中绕轴旋转 360 度 (TAU)。
    - 难点：将 Transform 与其它动画（如 Rotate）组合在同一个 self.play() 中执行。
    """
    def construct(self):
        # 1. 创建物体
        circle = Circle(color=RED, stroke_width=10)
        dot = Dot(circle.point_at_angle(0), color=WHITE)
        shape = VGroup(circle, dot)  # 父级容器
        
        triangle = Triangle(color=YELLOW, stroke_width=2)
        
        self.play(Create(shape))
        self.wait(0.5)

        # 2. 【核心技巧】
        # 让 shape (父级) 负责旋转 360 度
        # 让 circle 和 dot (子级) 分别执行变形和淡出
        # 它们在不同的层级操作，坐标不会冲突！
        self.play(
            Rotate(shape, angle=TAU),          # 整体旋转
            Transform(circle, triangle),       # 圆形变三角形
            FadeOut(dot),                      # 点淡出（或变成三角形的一部分）
            run_time=2,
            rate_func=linear                   # 匀速旋转配合变形效果更佳
        )
        self.wait(0.5)



if __name__ == "__main__":
    # 使用低质量预览模式渲染
    # 强制规范：必须包含 "input_file": __file__
    with tempconfig({"quality": "low_quality","flush_cache": True, "preview": True, "input_file": __file__}):
        # 你可以在这里切换想要预览的场景类名
        scene = Day04Exercise5() 
        scene.render()
