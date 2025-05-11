from manim import *

class Points_Line(Scene):
    def construct(self):
        fx_1 = MathTex(r"f(x)=a_0+a_1x").scale(0.8)
        fx_1.shift(UP * 1.5 + LEFT * 2.5)
        self.add(fx_1)
        
        px_1 = MathTex(r"\{(x_0,f(x_0),(x_1,f(x_1)\}").scale(0.8)
        px_1.shift(UP * 0.5 + LEFT * 2.5)
        self.add(px_1)
        
        axes = Axes(
                    x_range=[-5, 5, 1],
                    y_range=[-5, 5, 1],
                    x_length=5,
                    y_length=5,
                    tips=False,
                    color=GRAY
                )
        axes.to_edge(RIGHT)
        label = axes.get_axis_labels(x_label='x',y_label='f(x)').scale(0.8)
        self.play(Create(VGroup(axes,label)))
        
        
        dot_x0 = Dot(axes.coords_to_point(-1,-1))
        dot_x1 = Dot(axes.coords_to_point(1,3))
        self.play(FadeIn(VGroup(dot_x0, dot_x1)))
        
        line_1 = axes.plot(lambda x: 2*x+1, x_range=[-3, 2], color = BLUE) 
        self.play(Create(line_1,run_time=0.5))
        
        fx_2 = MathTex(r"f(x)=a_0+a_1x+a_2x^2").scale(0.8)
        fx_2.shift(UP * 1.5 + LEFT * 2.5)
        self.play(Transform(fx_1, fx_2))
        
        px_2 = MathTex(r"\{(x_0,f(x_0),(x_1,f(x_1),(x_2,f(x_2)\}").scale(0.8)
        px_2.shift(UP * 0.5 + LEFT * 2.5)
        self.play(Transform(px_1, px_2))
        
        dot_x2 = Dot(axes.coords_to_point(-3,1))
        self.play(FadeIn(dot_x2))
        
        line_2 = axes.plot(lambda x: 0.75*x*x+2*x+0.25, x_range=[-4.18, 1.51], color = GREEN)
        self.play(FadeOut(line_1))
        self.play(Create(line_2,run_time=0.5))
        
        Vandermonde = Text("Vandermonde determinant").scale(0.8)
        Vandermonde.shift(DOWN * 1 + LEFT *2.5)
        self.play(Create(Vandermonde))
        
        self.wait(1)
        
        fx_n = MathTex(r"f(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n").scale(0.8)
        fx_n.shift(UP * 1.5 + LEFT * 2.5)
        self.play(Transform(fx_1, fx_n))
        
        px_n = MathTex(r"\{(x_0,f(x_0),(x_1,f(x_1),(x_2,f(x_2),\cdots,(x_n,f(x_n)\}").scale(0.8)
        px_n.shift(UP * 0.5 + LEFT * 2.5)
        self.play(Transform(px_1, px_n))
        
        self.wait(1)
