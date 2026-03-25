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
            
        # 1. 欢迎标题
        welcome = Text(self.welcome_text, font_size=42, color=YELLOW, weight=BOLD)
        self.play(Write(welcome))
        self.wait(0.8)
        self.play(FadeOut(welcome))

        # 2. Github 地址
        github = Text(f"github学习地址: {self.github_url}", font_size=24, color=GRAY)
        self.play(Write(github))
        self.wait(0.8)
        
        # 将 Github 地址缩小并移动到左上角，作为常驻标识（可选）
        self.play(github.animate.scale(0.5).to_corner(UL, buff=0.1), run_time=1)
        self.github_mobject = github
        self.add(self.github_mobject) # 确保它留在场景中

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
        self.wait(2)
        self.play(FadeOut(end_text))
