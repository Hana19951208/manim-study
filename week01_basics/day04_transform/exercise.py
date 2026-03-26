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
        pass

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
        pass

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
        pass

if __name__ == "__main__":
    # 使用低质量预览模式渲染
    with tempconfig({"quality": "low_quality", "preview": True}):
        scene = Day04Exercise1()
        scene.render()
