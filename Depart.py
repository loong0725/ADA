from manim import *

class Depart(Scene):
    def construct(self):
        fx_number = MathTex(r"f(x)=5x^0+7x^1+9x^2+3x^3+0x^4+0x^5+0x^6+0x^7").scale(0.8)
        fx_number.move_to(UP * 3)
        self.add(fx_number)
        
        x_in = MathTex(r"x\in(\omega^0,\omega^1,\omega^2,\omega^3,\omega^4,\omega^5,\omega^6,\omega^7)").scale(0.8)
        x_in.move_to(UP * 2.3)
        self.add(x_in) 
        
        fx_get = MathTex(r"GET?\ f(\omega^0),f(\omega^1),f(\omega^2),f(\omega^3),f(\omega^4),f(\omega^5),f(\omega^6),f(\omega^7)").scale(0.8)
        fx_get.move_to(UP * 1.5)
        self.play(Write(fx_get))
        
        self.wait(0.5)
        
        fx_oe = MathTex(r"f(x)=(5x^0+9x^2+0x^4+0x^6)+(7x^1+3x^3+0x^5+0x^7)").scale(0.8)
        fx_oe.move_to(UP * 3)
        self.play(Transform(fx_number, fx_oe))
        
        self.wait(0.5)
        
        fx_xoe = MathTex(r"f(x)=(5x^0+9x^2+0x^4+0x^6)+x(7x^0+3x^2+0x^4+0x^6)").scale(0.8)
        fx_xoe.move_to(UP * 3)
        self.play(Transform(fx_number, fx_xoe))
        
        self.wait(0.5)
        
        px_1 = MathTex(r"p_1(x)=5x^0+9x^1+0x^2+0x^3").scale(0.8)
        px_1.shift(LEFT * 3)
        
        px_2 = MathTex(r"p_2(x)=7x^0+3x^1+0x^2+0x^3").scale(0.8)
        px_2.shift(RIGHT * 3)
        
        px = VGroup(px_1, px_2)
        px.shift(UP * 0.5)
        self.play(FadeIn(px))
        
        self.wait(0.5)
        
        fx_p = MathTex(r"f(x)=p_1(x^2)+xp_2(x^2)", color=YELLOW).scale(1)
        fx_p.shift(DOWN * 0.5)
        self.play(TransformFromCopy(fx_number, fx_p))
         
        self.wait(0.5)
        
        fx_q = MathTex(r"f(x)=(q_{11}(x^4)+x^2q_{12}(x^4))+x(q_{21}(x^4)+x^2q_{22}(x^4))").scale(0.8)
        fx_q.shift(DOWN * 1.3)
        self.play(TransformFromCopy(fx_p, fx_q))
        
        dot = MathTex(r"\vdots").scale(0.8)
        dot.shift(DOWN * 2)
        self.play(Create(dot))
        
        self.wait(0.5)
