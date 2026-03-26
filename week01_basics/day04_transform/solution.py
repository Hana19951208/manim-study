from manim import *

# Day 04 参考答案：变换与过渡 (Transformations & Transitions)
# 每个场景均提供了上述练习的标准实现方案和详细中文注释。

class Day04Solution1(Scene):
    """
    练习 1：多级替换变换
    从白色 Circle 变换为红色 Square，再到绿色 Triangle。
    """
    def construct(self):
        # 1. 创建圆形
        circle = Circle(color=WHITE)
        self.play(Create(circle))
        self.wait(0.5)
        
        # 2. 变换为红色正方形 (ReplacementTransform 推荐写法)
        square = Square(color=RED)
        self.play(ReplacementTransform(circle, square))
        self.wait(0.5)
        
        # 3. 变换为绿色三角形
        triangle = Triangle(color=GREEN)
        self.play(ReplacementTransform(square, triangle))
        self.wait(0.5)
        
        self.play(FadeOut(triangle))

class Day04Solution2(Scene):
    """
    练习 2：淡入淡出过渡 (FadeTransform)
    不同异形物体的平滑过渡：Star -> Annulus
    """
    def construct(self):
        # 创建星形
        star = Star(color=YELLOW, inner_radius=0.5, outer_radius=1).set_fill(YELLOW, opacity=0.8)
        self.play(Create(star))
        self.wait(0.5)
        
        # 创建圆环
        # FadeTransform 对此类外向差异巨大的物体表现更稳
        annulus = Annulus(inner_radius=0.8, outer_radius=1.2, color=PURPLE).set_fill(PURPLE, opacity=0.8)
        self.play(FadeTransform(star, annulus))
        self.wait(1)
        
        self.play(FadeOut(annulus))

class Day04Solution3(Scene):
    """
    练习 3：分配律公式推导 (TransformMatchingTex)
    a(b+c) = ab + ac 的智能位移演示
    """
    def construct(self):
        # 公式 A: a 和 ( b + c )
        expr1 = MathTex("a", "(", "b", "+", "c", ")", font_size=72)
        # 公式 B: a b + a c
        expr2 = MathTex("a", "b", "+", "a", "c", font_size=72)
        
        self.play(Write(expr1))
        self.wait(1)
        
        self.play(TransformMatchingTex(expr1, expr2), run_time=2)
        self.wait(1)
        self.play(FadeOut(expr2))

class Day04Solution4(Scene):
    """
    练习 4（进阶）：几何图形 -> 文字的丝滑变换
    将 4 个点变换为单词 "CODE"
    """
    def construct(self):
        # 1. 创建四个不同颜色的点
        dots = VGroup(*[
            Dot(color=c, radius=0.2) 
            for c in [BLUE, GREEN, RED, YELLOW]
        ])
        
        # 使用 arrange_in_grid 实现 2x2 正方形阵列
        dots.arrange_in_grid(rows=2, buff=1)
        
        # 2. 创建文字，并将其排列成同样的 2x2 阵列
        letters = VGroup(*[
            Text(l, font_size=80, color=dots[i].get_color()) 
            for i, l in enumerate(["C", "O", "D", "E"])
        ])
        letters.arrange_in_grid(rows=2, buff=1)

        self.play(Create(dots))
        self.wait(1)
        
        # 3. 对 Group 进行 ReplacementTransform
        self.play(ReplacementTransform(dots, letters), run_time=2)
        self.wait(2)
        self.play(FadeOut(letters))

class Day04Solution5(Scene):
    """
    练习 5（思考）：路径与属性的联动变换
    圆到三角形的旋转变换
    """
    def construct(self):
        # 1. 创建红色圆，加粗边框
        circle = Circle(stroke_width=12, color=RED)
        
        # 2. 创建黄色三角形，细边框
        triangle = Triangle(stroke_width=2, color=YELLOW)
        
        self.play(Create(circle))
        self.wait(1)
        
        # 3. 在 play 中合并动画
        self.play(
            Transform(circle, triangle),   # 形状变换
            Rotate(circle, angle=TAU),     # 绕轴旋转 360 度
            run_time=2,
            rate_func=smooth               # 平滑速率
        )
        self.wait(2)
        self.play(FadeOut(circle))

if __name__ == "__main__":
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        # 渲染两个高难度思考题的答案
        Day04Solution4().render()
        # Day04Solution5().render()
