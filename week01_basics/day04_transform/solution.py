from manim import *

# Day 04 参考答案：变换与过渡 (Transformations & Transitions)
# 每个场景均提供了上述练习的标准实现方案和详细中文注释。

class Day03Solution1(Scene):
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

class Day03Solution2(Scene):
    """
    练习 2：淡入淡出过渡 (FadeTransform)
    不同异形物体的平滑过渡：Star -> Annulus
    """
    def construct(self):
        # 创建星形
        star = Star(color=YELLOW, inner_radius=0.5, outer_radius=1)
        self.play(Create(star))
        self.wait(0.5)
        
        # 创建圆环
        # FadeTransform 对此类外向差异巨大的物体表现更稳
        annulus = Annulus(inner_radius=0.8, outer_radius=1.2, color=PURPLE)
        self.play(FadeTransform(star, annulus))
        self.wait(1)
        
        self.play(FadeOut(annulus))

class Day03Solution3(Scene):
    """
    练习 3：分配律公式推导 (TransformMatchingTex)
    a(b+c) = ab + ac 的智能位移演示
    """
    def construct(self):
        # 首先定义公式片段。通过精细化拆分，Manim 就会知道哪些项是“同一个”，并自动让它们飞向新位置。
        
        # 公式 A: a 和 ( b + c )
        expr1 = MathTex("a", "(", "b", "+", "c", ")", font_size=72)
        
        # 公式 B: a b + a c
        # 重点：此处出现了两个 "a"，Manim 会尝试从 A 中的 a 去匹配位置
        expr2 = MathTex("a", "b", "+", "a", "c", font_size=72)
        
        self.play(Write(expr1))
        self.wait(1)
        
        # 这种动画效果非常适合解释数学推导过程
        self.play(
            TransformMatchingTex(expr1, expr2),
            run_time=2
        )
        self.wait(1)
        
        self.play(FadeOut(expr2))

if __name__ == "__main__":
    # 使用低质量预览模式渲染所有解决方案
    with tempconfig({"quality": "low_quality", "preview": True}):
        # 顺序执行 3 个场景展示答案
        Day03Solution1().render()
        Day03Solution2().render()
        Day03Solution3().render()
