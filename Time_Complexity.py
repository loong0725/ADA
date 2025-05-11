import math
from manim import *

class Time_Complexity(Scene):
    def construct(self):  
        axes = Axes(
                    x_range=[0, 32, 32],
                    y_range=[0, 500, 500]
                )
        axes.shift(UP * 0.5)
        self.play(Create(axes))  
        
        x_label = Text("Number of samples(N)").scale(0.5)
        x_label.shift(DOWN * 2.8)
        self.play(FadeIn(x_label))
        
        y_label = Text("Number of calculations").scale(0.5)
        y_label.rotate(PI * 0.5)
        y_label.to_edge(LEFT)
        y_label.shift(UP * 0.5 + RIGHT * 0.2)
        self.play(FadeIn(y_label))
        
        fx_origin = MathTex(r"f(\omega^k)=p_1(\omega^{2k})+\omega^k p_2(\omega^{2k}),\ k\in[0, N-1]").scale(0.7)
        fx_origin.shift(LEFT * (5.5 + fx_origin.get_left()))
        fx_origin.shift(UP * 3)
        self.play(Write(fx_origin))
        
        graph_origin = axes.plot(lambda x: x**2, x_range=[0.001, 28], color = RED)
        self.play(Create(graph_origin))
        
        O_n2 = MathTex(r"O(N^2)")
        O_n2.shift(UP * 3)
        O_n2.shift(RIGHT * 3)
        self.play(FadeIn(O_n2))
        
        arrow = Arrow(start=UP * 3 + LEFT * 5, end=UP * 2 + LEFT * 5)
        self.play(Create(arrow))
        
        fx_new1 = MathTex(r"f(\omega^k)=p_1(\omega^{2k})+\omega^k p_2(\omega^{2k})").scale(0.7)
        fx_new1.shift(LEFT * (5.5 + fx_new1.get_left()))
        fx_new1.shift(UP * 2)
        self.play(Write(fx_new1))
        
        fx_new2 = MathTex(r"f(\omega^{k+\frac{N}{2}})=p_1(\omega^{2k})-\omega^k p_2(\omega^{2k})").scale(0.7)
        fx_new2.shift(LEFT * (5.5 + fx_new2.get_left()))
        fx_new2.shift(UP * 1.4)
        self.play(Write(fx_new2))
        
        fx_k = MathTex(r"k\in[0, \frac{N}{2}-1]").scale(0.7)
        fx_k.shift(RIGHT * 0.5)
        fx_k.shift(UP * 1.8)
        self.play(Write(fx_k))
        
        graph_new = axes.plot(lambda x: x*math.log(x), x_range=[0.001, 32], color = YELLOW)
        self.play(Create(graph_new))
        
        O_nlogn = MathTex(r"O(N\log(N))")
        O_nlogn.shift(RIGHT * 4)
        O_nlogn.shift(DOWN * 2)
        self.play(FadeIn(O_nlogn))
        
        self.wait(1)
