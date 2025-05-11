from manim import *

class Normalization(Scene):
    def construct(self):
        fx_origin = MathTex(r"f(x)= \sum\limits_{i=0}^{n-1}a_i x^i=a_0+a_1x+ \cdots+a_{n-1}x^{n-1}").scale(0.8)
        fx_origin.move_to(UP * 3)
        self.add(fx_origin)
        
        gx_origin = MathTex(r"g(x)= \sum\limits_{i=0}^{m-1}b_i x^i=b_0+b_1x+ \cdots+b_{m-1}x^{m-1}").scale(0.8)
        gx_origin.move_to(UP * 1.5)
        self.add(gx_origin)
        
        hx_origin = MathTex(r"h(x)= \sum\limits_{i=0}^{(n-1)+(m-1)}c_i x^i=c_0+c_1x+ \cdots+c_{(n-1)+(m-1)}x^{(n-1)+(m-1)}").scale(0.8)
        hx_origin.move_to(UP * 0)
        self.add(hx_origin)
        
        N = MathTex(r"N=2^{\lfloor\log_{2}{(n-1)+(m-1)\rfloor+1}}").scale(1)
        N.move_to(DOWN * 2)
        self.play(Write(N))
        
        fx_new = MathTex(r"f(x)= \sum\limits_{i=0}^{N-1}a_i x^i=a_0+a_1x+ \cdots+a_{N-1}x^{N-1}").scale(0.8)
        fx_new.move_to(UP * 3)
        self.play(Transform(fx_origin, fx_new))
        
        gx_new = MathTex(r"g(x)= \sum\limits_{i=0}^{N-1}b_i x^i=b_0+b_1x+ \cdots+b_{N-1}x^{N-1}").scale(0.8)
        gx_new.move_to(UP * 1.5)
        self.play(Transform(gx_origin, gx_new))
        
        hx_new = MathTex(r"h(x)= \sum\limits_{i=0}^{N-1}c_i x^i=c_0+c_1x+ \cdots+c_{N-1}x^{N-1}").scale(0.8)
        hx_new.move_to(UP * 0)
        self.play(Transform(hx_origin, hx_new))
        
        self.play(FadeOut(N, run_time=0.5))
        
        # 3975*13482=53590950
        fx_number = MathTex(r"f(x)=5+7x+9x^2+3x^3+0x^4+0x^5+0x^6+0x^7").scale(0.8)
        fx_number.move_to(UP * 3)
        self.play(Transform(fx_origin, fx_number))
        
        gx_number = MathTex(r"g(x)=2+8x+4x^2+3x^3+1x^4+0x^5+0x^6+0x^7").scale(0.8)
        gx_number.move_to(UP * 1.5)
        self.play(Transform(gx_origin, gx_number))
        
        # 10+54x+94x^2+121x^3+86x^4+46x^5+18x^6+3x^7
        hx_number = MathTex(r"h(x)=10+54x+94x^2+121x^3+86x^4+46x^5+18x^6+3x^7").scale(0.8)
        hx_number.move_to(UP * 0)
        self.play(Transform(hx_origin, hx_number))
        
        self.wait(1)  
