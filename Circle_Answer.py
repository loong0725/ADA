import math
from manim import *

class Circle_Answer(Scene):
    def construct(self):
        axes = Axes(
                    x_range=[-2.5, 2.5], # 效果与(-3, 3, 1)完全相同
                    y_range=[-2.5, 2.5],  # 效果与(-3, 3, 1)完全相同
                    x_length=5,
                    y_length=5,
                    axis_config={"include_numbers": True}
                )
        circle = Circle(radius=1, color=WHITE)
        self.add(circle)

        dot_axes1 = Dot(axes.coords_to_point(1,0), color=BLUE)
        t0 = MathTex(r'\omega^0',color = 'YELLOW').scale(0.7).next_to(dot_axes1,RIGHT,UP)
        self.add(axes,dot_axes1)

        dot_axes2 = Dot(axes.coords_to_point(math.sqrt(2)/2, math.sqrt(2)/2), color=BLUE)
        self.add(axes,dot_axes2)
        t1 = MathTex(r'\omega^{1}',color = 'YELLOW').scale(0.7).next_to(dot_axes2,RIGHT,UP)

        dot_axes3 = Dot(axes.coords_to_point(0,1), color=BLUE)
        self.add(axes,dot_axes3)
        t2 = MathTex(r'\omega^{2}',color = 'YELLOW').scale(0.7).next_to(dot_axes3,UP*0.4)

        dot_axes4 = Dot(axes.coords_to_point(-math.sqrt(2)/2, math.sqrt(2)/2), color=BLUE)
        self.add(axes,dot_axes4)
        t3 = MathTex(r'\omega^{3}',color = 'YELLOW').scale(0.7).next_to(dot_axes4,LEFT,UP)

        dot_axes5 = Dot(axes.coords_to_point(-1,0), color=BLUE)
        self.add(axes,dot_axes5)
        t4 = MathTex(r'\omega^{4}',color = 'YELLOW').scale(0.7).next_to(dot_axes5,LEFT,UP)

        dot_axes6 = Dot(axes.coords_to_point(-math.sqrt(2)/2, -math.sqrt(2)/2), color=BLUE)
        self.add(axes,dot_axes6)
        t5 = MathTex(r'\omega^{5}',color = 'YELLOW').scale(0.7).next_to(dot_axes6,LEFT,UP)

        dot_axes7 = Dot(axes.coords_to_point(0, -1), color=BLUE)
        self.add(axes,dot_axes7)
        t6 = MathTex(r'\omega^{6}',color = 'YELLOW').scale(0.7).next_to(dot_axes7,DOWN*0.4)

        dot_axes8 = Dot(axes.coords_to_point(math.sqrt(2)/2, -math.sqrt(2)/2), color=BLUE)
        self.add(axes,dot_axes8)
        t7 = MathTex(r'\omega^{7}',color = 'YELLOW').scale(0.7).next_to(dot_axes8,RIGHT,UP)

        allt = VGroup(t0,t1,t2,t3,t4,t5,t6,t7)
        all_dot = VGroup(dot_axes1,dot_axes2,dot_axes3,dot_axes4,dot_axes5,dot_axes6,dot_axes7,dot_axes8)
        all_elements = VGroup(allt, axes, circle, all_dot)
        all_elements.to_edge(RIGHT)
        self.add(all_elements)
        
        self.wait(0.5)
        
        fx_get = MathTex(r"GET?\ f(\omega^0),f(\omega^1),f(\omega^2),f(\omega^3),f(\omega^4),f(\omega^5),f(\omega^6),f(\omega^7)").scale(0.8)
        fx_get.shift(UP * 3.5)
        self.play(FadeIn(fx_get))
        
        fw0 = MathTex(r"f(\omega^0)=p_1(\omega^{0\times 2})+\omega^0 p_2(\omega^{0\times 2})").scale(0.6)
        fw0.shift(UP * 2.1)
        
        fw1 = MathTex(r"f(\omega^1)=p_1(\omega^{1\times 2})+\omega^1 p_2(\omega^{1\times 2})").scale(0.6)
        fw1.shift(UP * 1.5)
        
        fw2 = MathTex(r"f(\omega^2)=p_1(\omega^{2\times 2})+\omega^2 p_2(\omega^{2\times 2})").scale(0.6)
        fw2.shift(UP * 0.9)
        
        fw3 = MathTex(r"f(\omega^3)=p_1(\omega^{3\times 2})+\omega^3 p_2(\omega^{3\times 2})").scale(0.6)
        fw3.shift(UP * 0.3)
        
        fw0123 = VGroup(fw0, fw1, fw2, fw3)
        fw0123.shift(LEFT * 4.5)
        self.play(Write(fw0123))
        
        fw4 = MathTex(r"f(\omega^4)=p_1(\omega^{4\times 2})+\omega^4 p_2(\omega^{4\times 2})").scale(0.6)
        fw4.shift(DOWN * 0.3)
        
        fw5 = MathTex(r"f(\omega^5)=p_1(\omega^{5\times 2})+\omega^5 p_2(\omega^{5\times 2})").scale(0.6)
        fw5.shift(DOWN * 0.9)
        
        fw6 = MathTex(r"f(\omega^6)=p_1(\omega^{6\times 2})+\omega^6 p_2(\omega^{6\times 2})").scale(0.6)
        fw6.shift(DOWN * 1.5)
        
        fw7 = MathTex(r"f(\omega^7)=p_1(\omega^{7\times 2})+\omega^7 p_2(\omega^{7\times 2})").scale(0.6)
        fw7.shift(DOWN * 2.1)
        
        fw4567 = VGroup(fw4, fw5, fw6, fw7)
        fw4567.shift(LEFT * 4.5)
        self.play(Write(fw4567))
        
        Rect1_origin = Rectangle(width=1.3, height=4.8, color=RED)
        Rect1_origin.shift(LEFT * 4.8)
        self.play(Create(Rect1_origin))
        
        Rect2_origin = Rectangle(width=1.3, height=4.8, color=RED)
        Rect2_origin.shift(LEFT * 3)
        self.play(Create(Rect2_origin))
        
        ww0 = MathTex(r"\omega^4=-\omega^0").scale(0.8)
        ww0.shift(UP * 0.9)
        
        ww1 = MathTex(r"\omega^5=-\omega^1").scale(0.8)
        ww1.shift(UP * 0.3)
        
        ww2 = MathTex(r"\omega^6=-\omega^2").scale(0.8)
        ww2.shift(DOWN * 0.3)
        
        ww3 = MathTex(r"\omega^7=-\omega^3").scale(0.8)
        ww3.shift(DOWN * 0.9)
        
        ww = VGroup(ww0, ww1, ww2, ww3)
        ww.shift(LEFT * 0.5)
        self.play(TransformFromCopy(allt, ww))
        
        self.wait(1)
        
        ww0_trans = MathTex(r"f(\omega^4)=f(-\omega^0)").scale(0.8)
        ww0_trans.shift(UP * 0.9)
        
        ww1_trans = MathTex(r"f(\omega^5)=f(-\omega^1)").scale(0.8)
        ww1_trans.shift(UP * 0.3)
        
        ww2_trans = MathTex(r"f(\omega^6)=f(-\omega^2)").scale(0.8)
        ww2_trans.shift(DOWN * 0.3)
        
        ww3_trans = MathTex(r"f(\omega^7)=f(-\omega^3)").scale(0.8)
        ww3_trans.shift(DOWN * 0.9)
        
        ww_trans = VGroup(ww0_trans, ww1_trans, ww2_trans, ww3_trans)
        ww_trans.shift(LEFT * 0.5)
        self.play(Transform(ww, ww_trans))
       
        self.wait(1)
        
        fw4_easy = MathTex(r"f(\omega^4)=p_1(\omega^{0\times 2})-\omega^0 p_2(\omega^{0\times 2})").scale(0.6)
        fw4_easy.shift(DOWN * 0.3)
        
        fw5_easy = MathTex(r"f(\omega^5)=p_1(\omega^{1\times 2})-\omega^1 p_2(\omega^{1\times 2})").scale(0.6)
        fw5_easy.shift(DOWN * 0.9)
        
        fw6_easy = MathTex(r"f(\omega^6)=p_1(\omega^{2\times 2})-\omega^2 p_2(\omega^{2\times 2})").scale(0.6)
        fw6_easy.shift(DOWN * 1.5)
        
        fw7_easy = MathTex(r"f(\omega^7)=p_1(\omega^{3\times 2})-\omega^3 p_2(\omega^{3\times 2})").scale(0.6)
        fw7_easy.shift(DOWN * 2.1)
        
        fw_easy = VGroup(fw4_easy, fw5_easy, fw6_easy, fw7_easy)
        fw_easy.shift(LEFT * 4.5)
        self.play(Transform(fw4567, fw_easy))
        
        Rect1_new = Rectangle(width=1.3, height=2.4, color=RED)
        Rect1_new.shift(LEFT * 4.8)
        Rect1_new.shift(UP * 1.1)
        self.play(ReplacementTransform(Rect1_origin, Rect1_new))
        
        Rect2_new = Rectangle(width=1.3, height=2.4, color=RED)
        Rect2_new.shift(LEFT * 3)
        Rect2_new.shift(UP * 1.1)
        self.play(ReplacementTransform(Rect2_origin, Rect2_new))
        
        self.wait(1)
