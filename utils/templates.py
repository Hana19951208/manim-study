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

        # 1. 统一创建所有元素（语义化命名，避免重名）
        logo = SVGMobject("assets/svg/github.svg", height=1, width=1) \
            .set_fill(color=GRAY_B) \
            .scale(1.5)
        
        main_text = Text("创意无限，代码即艺术!!", font_size=40, color=GRAY_B)
        github_text = Text(f"{self.github_url}", font_size=24, color=GRAY)

        # 2. 精准排版（指定对齐方向，杜绝位置偏移）
        main_text.next_to(logo, RIGHT, buff=0.3)  # 文字在logo右侧
        main_text.align_to(logo, VCenter)         # 与logo垂直居中对齐

        github_text.next_to(logo, DOWN, buff=0.3) # 链接在logo正下方
        github_text.align_to(logo, CENTER)        # 与整体水平居中对齐

        # 3. 一次性组合所有元素 + 整体居中（仅居中1次，无冗余）
        self.github_mobject = VGroup(logo, main_text, github_text)
        self.github_mobject.center()  # 最终整体居中，一步到位

        # 4. 同步播放所有入场动画
        self.play(
            DrawBorderThenFill(logo),
            Write(main_text),
            Write(github_text),
            run_time=1.2
        )
        self.wait(1)

        # 5. 整体移动缩放（保持组合完整性）
        self.play(
            self.github_mobject.animate
                .scale(0.3)
                .to_corner(UL, buff=0.1),
            run_time=1
        )
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
