"""
Day 02: 字体风格展示
学习目标：预览适合数学动画的高级感字体组合，并观察中英混排与技术标签效果。
运行方式：python font_showcase.py
"""

import os
import sys

# 将项目根目录添加到 python 搜索路径（针对直接运行脚本的情况）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from manim import *
import manimpango

from utils.templates import StudyScene


FONT_PRESETS = {
    "hero": {
        "title": ["Avenir Next", "Avenir", "Helvetica Neue", "Futura"],
        "body": [
            "Source Han Sans VF",
            "Source Han Sans SC VF",
            "Source Han Sans CN",
            "PingFang SC",
            "Hiragino Sans GB",
        ],
        "mono": ["JetBrains Mono", "IBM Plex Mono", "Menlo"],
    },
    "clean": {
        "title": ["Helvetica Neue", "Avenir Next", "Avenir"],
        "body": ["PingFang SC", "Hiragino Sans GB", "Source Han Sans VF"],
        "mono": ["JetBrains Mono", "Menlo"],
    },
    "poster": {
        "title": ["Futura", "Avenir Next", "Helvetica Neue"],
        "body": ["Source Han Sans SC VF", "PingFang SC", "Hiragino Sans GB"],
        "mono": ["JetBrains Mono", "Menlo"],
    },
}


def pick_available_font(candidates: list[str]) -> str:
    """从候选字体中挑选当前系统可用的第一项。"""

    installed_fonts = set(manimpango.list_fonts())
    for font_name in candidates:
        if font_name in installed_fonts:
            return font_name
    return candidates[0]


def resolve_font_triplet(preset_name: str) -> tuple[str, str, str]:
    """解析标题、正文、等宽字体。"""

    preset = FONT_PRESETS[preset_name]
    title_font = pick_available_font(preset["title"])
    body_font = pick_available_font(preset["body"])
    mono_font = pick_available_font(preset["mono"])
    return title_font, body_font, mono_font


class Day02FontShowcase(StudyScene):
    """展示适合 Manim 的理性科技感字体组合。"""

    show_header = False
    show_footer = False

    def construct(self):
        self.camera.background_color = "#0F1115"

        title_font, body_font, mono_font = resolve_font_triplet("hero")

        title = Text(
            "LINEAR ALGEBRA",
            font=title_font,
            font_size=50,
            weight=BOLD,
            color="#F3F5F7",
        )

        subtitle = Text(
            "向量空间与线性变换",
            font=body_font,
            font_size=28,
            weight=MEDIUM,
            color="#D8E1EA",
        )

        caption = Text(
            "现代、克制、适合数学动画的标题组合",
            font=body_font,
            font_size=20,
            color="#92A0AF",
        )

        accent_line = Line(LEFT * 2.8, RIGHT * 2.8, stroke_width=2.5, color="#5B8DEF")

        formula = MathTex(
            r"T(\mathbf{v}) = A\mathbf{v}",
            font_size=60,
            color="#7CC6FE",
        )

        code_label = Text(
            "eigenvalue = 3.14",
            font=mono_font,
            font_size=24,
            color="#91F2D0",
        )

        font_meta = Text(
            f"Title: {title_font}   Body: {body_font}   Mono: {mono_font}",
            font=mono_font,
            font_size=16,
            color="#6B7785",
        )

        top_group = VGroup(title, subtitle, caption).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT
        )

        bottom_group = VGroup(formula, code_label, font_meta).arrange(
            DOWN, buff=0.38, aligned_edge=LEFT
        )

        layout = VGroup(top_group, accent_line, bottom_group).arrange(
            DOWN, buff=0.55, aligned_edge=LEFT
        )
        layout.move_to(ORIGIN)
        layout.shift(UP * 0.15)

        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.15), FadeIn(caption), run_time=0.8)
        self.play(Create(accent_line), run_time=0.6)
        self.play(Write(formula), run_time=1.4)
        self.play(FadeIn(code_label, shift=UP * 0.1), FadeIn(font_meta), run_time=0.8)
        self.wait(2)


class Day02PosterFontShowcase(StudyScene):
    """展示更强视觉张力的封面海报风字体布局。"""

    show_header = False
    show_footer = False

    def construct(self):
        self.camera.background_color = "#090B10"

        title_font, body_font, mono_font = resolve_font_triplet("poster")

        glow = Circle(radius=2.6, stroke_opacity=0, fill_color="#113355", fill_opacity=0.24)
        glow.shift(RIGHT * 3.2 + UP * 1.6)

        red_panel = Rectangle(
            width=3.8,
            height=8.5,
            stroke_opacity=0,
            fill_color="#F25F5C",
            fill_opacity=0.92,
        )
        red_panel.rotate(-0.22)
        red_panel.to_edge(LEFT, buff=-1.2)
        red_panel.shift(UP * 0.2)

        blue_panel = Rectangle(
            width=4.6,
            height=2.1,
            stroke_opacity=0,
            fill_color="#1F6FEB",
            fill_opacity=0.88,
        )
        blue_panel.rotate(0.18)
        blue_panel.to_corner(DR, buff=-0.8)

        ghost = Text(
            "VECTOR",
            font=title_font,
            font_size=108,
            weight=BOLD,
            color="#171B22",
        )
        ghost.set_opacity(0.78)
        ghost.rotate(-0.12)
        ghost.shift(UP * 2.15 + RIGHT * 1.2)

        tag = Text(
            "DAY 02  TYPOGRAPHY STUDY",
            font=mono_font,
            font_size=18,
            color="#B7C2D0",
        )

        headline_a = Text(
            "VISUAL",
            font=title_font,
            font_size=72,
            weight=BOLD,
            color="#F4F7FB",
        )
        headline_b = Text(
            "TENSION",
            font=title_font,
            font_size=72,
            weight=BOLD,
            color="#F25F5C",
        )
        headline = VGroup(headline_a, headline_b).arrange(
            DOWN, buff=0.08, aligned_edge=LEFT
        )

        subtitle = Text(
            "更强对比、更大留白、更像封面而不是讲义",
            font=body_font,
            font_size=24,
            weight=MEDIUM,
            color="#D9E2EC",
        )

        equation = MathTex(
            r"\lambda_{\max} \cdot \mathbf{v}",
            font_size=54,
            color="#7CC6FE",
        )

        descriptor = Text(
            "Futura / Source Han Sans SC VF / JetBrains Mono",
            font=mono_font,
            font_size=17,
            color="#8A97A6",
        )

        content = VGroup(tag, headline, subtitle, equation, descriptor).arrange(
            DOWN, buff=0.26, aligned_edge=LEFT
        )
        content.to_edge(LEFT, buff=0.9)
        content.shift(DOWN * 0.15)

        self.add(glow)
        self.play(FadeIn(red_panel, shift=LEFT * 0.35), FadeIn(blue_panel, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(ghost, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(tag, shift=UP * 0.15), run_time=0.4)
        self.play(FadeIn(headline_a, shift=RIGHT * 0.18), run_time=0.5)
        self.play(FadeIn(headline_b, shift=RIGHT * 0.18), run_time=0.5)
        self.play(FadeIn(subtitle), run_time=0.45)
        self.play(Write(equation), run_time=1.1)
        self.play(FadeIn(descriptor), run_time=0.35)
        self.wait(2)


if __name__ == "__main__":
    # 使用低质量预览模式 (等同于命令行 -pql)
    with tempconfig({"quality": "low_quality", "preview": True, "input_file": __file__}):
        scene = Day02PosterFontShowcase()
        scene.render()
