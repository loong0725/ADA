from manim import *

class Summarize(Scene):
    def construct(self):
        fx_parameter = MathTex(r"f(x)=a_0+a_1x+ \cdots+a_{n-1}x^{n-1}").scale(0.6)
        fx_parameter.shift(LEFT * 4.2 + UP * 3.2)
        self.play(Write(fx_parameter))
        
        gx_parameter = MathTex(r"g(x)=b_0+b_1x+ \cdots+b_{m-1}x^{m-1}").scale(0.6)
        gx_parameter.shift(LEFT * 4.2 + UP * 2.7)
        self.play(Write(gx_parameter)) 
        
        arrow1 = Arrow(start=UP * 2.3 + LEFT * 4.2, end=UP * 1.8 + LEFT * 4.2)
        self.play(Create(arrow1))
        
        rect_fft = Rectangle(width=3, height=1.5, color=RED)
        rect_fft.shift(LEFT * 4.2 + UP * 1)
        self.play(Create(rect_fft))
        
        fft_text = MathTex(r"Coeff\Rightarrow Value").scale(0.7)
        fft_text.shift(LEFT * 4.2 + UP * 1.4)
        self.play(FadeIn(fft_text))
        
        fft = Text("F F T", color=RED_A)
        fft.shift(LEFT * 4.2 + UP * 0.7)
        self.play(FadeIn(fft))
        
        arrow2 = Arrow(start=UP * 0.5 + LEFT * 4.2, end=DOWN * 0.5 + LEFT * 4.2)
        self.play(Create(arrow2))
        
        axes_f = Axes(
                    x_range=[-2, 2, 1],
                    y_range=[0, 9, 1],
                    x_length=1.5,
                    y_length=2.5,
                    tips=False,
                    color=GRAY
                )
        axes_f.shift(LEFT * 5.3 + DOWN * 1.7)
        
        label_fx = Text("x").scale(0.6)
        label_fx.shift(LEFT * 4.3 + DOWN * 3)
        label_fy = Text("f(x)").scale(0.6)
        label_fy.shift(LEFT * 5.3 + DOWN * 0.2)
        label_f = VGroup(label_fx, label_fy)
        
        line_f = axes_f.plot(lambda x: (x-1)**2, x_range=[-2, 2], color = BLUE)
        
        dot_f1 = Dot(axes_f.coords_to_point(-2,9), color=BLUE)
        dot_f2 = Dot(axes_f.coords_to_point(-1,4), color=BLUE)
        dot_f3 = Dot(axes_f.coords_to_point(0,1), color=BLUE)
        dot_f4 = Dot(axes_f.coords_to_point(1,0), color=BLUE)
        dot_f5 = Dot(axes_f.coords_to_point(2,1), color=BLUE)
        dot_f = VGroup(dot_f1, dot_f2, dot_f3, dot_f4, dot_f5)
        
        self.play(Create(VGroup(axes_f, label_f, line_f, dot_f)))
        
        axes_g = Axes(
                    x_range=[-2, 2, 1],
                    y_range=[0, 9, 1],
                    x_length=1.5,
                    y_length=2.5,
                    tips=False,
                    color=GRAY
                )
        axes_g.shift(LEFT * 3.1 + DOWN * 1.7)
        
        label_gx = Text("x").scale(0.6)
        label_gx.shift(LEFT * 2.1 + DOWN * 3)
        label_gy = Text("g(x)").scale(0.6)
        label_gy.shift(LEFT * 3.1 + DOWN * 0.2)
        label_g = VGroup(label_gx, label_gy)
        
        line_g = axes_g.plot(lambda x: (x+1)**2, x_range=[-2, 2], color = YELLOW)
        
        dot_g1 = Dot(axes_g.coords_to_point(-2,1), color=YELLOW)
        dot_g2 = Dot(axes_g.coords_to_point(-1,0), color=YELLOW)
        dot_g3 = Dot(axes_g.coords_to_point(0,1), color=YELLOW)
        dot_g4 = Dot(axes_g.coords_to_point(1,4), color=YELLOW)
        dot_g5 = Dot(axes_g.coords_to_point(2,9), color=YELLOW)
        dot_g = VGroup(dot_g1, dot_g2, dot_g3, dot_g4, dot_g5)
        
        self.play(Create(VGroup(axes_g, label_g, line_g, dot_g)))
        
        self.wait(0.5)
        
        arrow3 = Arrow(start=DOWN * 1.7 + LEFT * 2.1, end=DOWN * 1.7 + LEFT * 1.1)
        self.play(Create(arrow3))
        
        h_fg = MathTex(r"h(x)=f(x)\times g(x)").scale(0.6)
        h_fg.shift(DOWN * 0.7)
        self.play(FadeIn(h_fg))
        
        rect_multiply = Rectangle(width=2.5, height=1.5, color=TEAL)
        rect_multiply.shift(DOWN * 1.7)
        self.play(Create(rect_multiply))
        
        multiply = Text("Multiply").scale(0.7)
        multiply.shift(DOWN * 1.7)
        self.play(FadeIn(multiply))
        
        arrow4 = Arrow(start=DOWN * 1.7 + RIGHT * 1.1, end=DOWN * 1.7 + RIGHT * 2.1)
        self.play(Create(arrow4))
        
        axes_h = Axes(
                    x_range=[-2, 2, 1],
                    y_range=[0, 9, 1],
                    x_length=2,
                    y_length=2.5,
                    tips=False,
                    color=GRAY
                )
        axes_h.shift(RIGHT * 4.2 + DOWN * 1.7)
        
        label_hx = Text("x").scale(0.6)
        label_hx.shift(RIGHT * 5.5 + DOWN * 3)
        label_hy = Text("h(x)").scale(0.6)
        label_hy.shift(RIGHT * 4.7 + DOWN * 0.4)
        label_h = VGroup(label_hx, label_hy)
        
        line_h = axes_h.plot(lambda x: ((x+1)**2)*((x-1)**2), x_range=[-2, 2], color = GREEN)
        
        dot_h1 = Dot(axes_h.coords_to_point(-2,9), color=GREEN)
        dot_h2 = Dot(axes_h.coords_to_point(-1,0), color=GREEN)
        dot_h3 = Dot(axes_h.coords_to_point(0,1), color=GREEN)
        dot_h4 = Dot(axes_h.coords_to_point(1,0), color=GREEN)
        dot_h5 = Dot(axes_h.coords_to_point(2,9), color=GREEN)
        dot_h = VGroup(dot_h1, dot_h2, dot_h3, dot_h4, dot_h5)
        
        self.play(Create(VGroup(axes_h, label_h, line_h, dot_h)))
        
        arrow5 = Arrow(start=DOWN * 0.5 + RIGHT * 4.2, end=UP * 0.5 + RIGHT * 4.2)
        self.play(Create(arrow5))
        
        rect_ifft = Rectangle(width=3, height=1.5, color=GREEN)
        rect_ifft.shift(RIGHT * 4.2 + UP * 1)
        self.play(Create(rect_ifft))
        
        ifft_text = MathTex(r"Value\Rightarrow Coeff").scale(0.7)
        ifft_text.shift(RIGHT * 4.2 + UP * 1.4)
        self.play(FadeIn(ifft_text))
        
        ifft = Text("I F F T", color=GREEN_A)
        ifft.shift(RIGHT * 4.2 + UP * 0.7)
        self.play(FadeIn(ifft))
        
        arrow6 = Arrow(start=UP * 1.8 + RIGHT * 4.2, end=UP * 2.3 + RIGHT * 4.2)
        self.play(Create(arrow6))
        
        hx_parameter = MathTex(r"h(x)=c_0+c_1x+\cdots+c_{N-1}x^{N-1}").scale(0.6)
        hx_parameter.shift(RIGHT * 4.2 + UP * 3.2)
        self.play(Write(hx_parameter))
        
        N = MathTex(r"(N=2^{\lfloor\log_{2}{(n-1)+(m-1)\rfloor+1}})").scale(0.6)
        N.shift(RIGHT * 4.2 + UP * 2.7)
        self.play(Write(N))
        
        self.wait(1)
