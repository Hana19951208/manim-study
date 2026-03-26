from manim import *

class StudyScene(Scene):
    """
    项目专用的基础场景类，集成了欢迎语、Github 链接和结尾动画模板。
    
    属性:
        show_header (bool): 是否显示开头的欢迎语和 Github 链接
        show_footer (bool): 是否显示结束后的完成提示
        welcome_text (str): 欢迎语内容
        github_url (str): Github 仓库地址
    """
    
    show_header = True
    show_footer = True
    welcome_text = "欢迎来到Manim学习之旅"
    github_url = "https://github.com/Hana19951208/manim-study"

    def play_welcome(self):
        """播放欢迎语和 Github 链接动画"""
        if not self.show_header:
            return
            
        # 0. 欢迎标题
        welcome = Text(self.welcome_text, font_size=42, color=YELLOW, weight=BOLD)
        self.play(Write(welcome))
        self.wait(0.8)
        self.play(FadeOut(welcome))

        # 1. 统一创建所有元素
        logo = SVGMobject("assets/svg/github.svg", height=1.2).set_fill(color=GRAY_B)
        text = Text("创意无限，代码即艺术!!", font_size=40, color=GRAY_B)
        github = Text(self.github_url, font_size=24, color=GRAY)

        # 2. 语义化排版：使用 arrange 自动对齐
        # 先将 logo 和主文字水平排列，buff 指定间距
        header = VGroup(logo, text).arrange(RIGHT, buff=0.4)
        # 将头部与 github 链接垂直排列（arrange 会自动处理水平居中）
        self.github_mobject = VGroup(header, github).arrange(DOWN, buff=0.3)
        # 整体居中显示
        self.github_mobject.center()

        # 3. 同步绘制动画
        self.play(
            DrawBorderThenFill(logo),
            Write(text),
            Write(github),
            run_time=1.2
        )
        self.wait(1)

        # 4. 整体缩放平移至左上角
        self.play(
            self.github_mobject.animate.scale(0.3).to_corner(UL, buff=0.1),
            run_time=1
        )
        self.add(self.github_mobject) # 确保作为常驻标识
        self.wait(1)

    def play_finish(self, day_label="Day XX"):
        """
        播放结束动画
        
        参数:
            day_label (str): 当前学习的天数标识，如 "Day 01"
        """
        if not self.show_footer:
            return
            
        # 清理屏幕
        self.play(*[FadeOut(m) for m in self.mobjects])
        
        # 显示完成文字
        end_text = Text(f"✓ {day_label} 完成！", font_size=44, color=GREEN)
        self.play(Write(end_text))
        self.wait(0.8)
        self.play(FadeOut(end_text))
