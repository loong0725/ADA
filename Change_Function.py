from manim import *

class ChangeFunction(Scene):
    def construct(self):
        # 创建数字文本对象  
        number1 = Text('3', font="Times New Roman").scale(1)
        number2 = Text('9', font="Times New Roman").scale(1)
        number3 = Text('7', font="Times New Roman").scale(1)
        number4 = Text('5', font="Times New Roman").scale(1)
  
        # 设置文本位置  
        number1.move_to(RIGHT * 2)  
        number2.move_to(RIGHT * 3)  
        number3.move_to(RIGHT * 4)  
        number4.move_to(RIGHT * 5)
        
        number_group1 = VGroup(number1, number2, number3, number4)
        number_group1.shift(UP * 1)
        self.add(number_group1)
        
        sign = MathTex(r"\times").scale(2)
        sign.shift(UP * 1.8)
        sign.shift(LEFT * 2.5)
        self.add(sign)
        
        number5 = Text('1', font="Times New Roman").scale(1)
        number6 = Text('3', font="Times New Roman").scale(1)
        number7 = Text('4', font="Times New Roman").scale(1)
        number8 = Text('8', font="Times New Roman").scale(1)
        number9 = Text('2', font="Times New Roman").scale(1)

        # 设置每个正方形的位置
        number5.shift(RIGHT * 1)
        number6.shift(RIGHT * 2)
        number7.shift(RIGHT * 3)
        number8.shift(RIGHT * 4)
        number9.shift(RIGHT * 5)

        number_group2 = VGroup(number5, number6, number7, number8, number9)
        number_group2.shift(UP * 2.5)
        self.add(number_group2)
        
        answer1 = Text('5', font="Times New Roman").scale(1)
        answer2 = Text('3', font="Times New Roman").scale(1)
        answer3 = Text('5', font="Times New Roman").scale(1)
        answer4 = Text('9', font="Times New Roman").scale(1)
        answer5 = Text('0', font="Times New Roman").scale(1)
        answer6 = Text('9', font="Times New Roman").scale(1)
        answer7 = Text('5', font="Times New Roman").scale(1)
        answer8 = Text('0', font="Times New Roman").scale(1)
        
        line = Line(LEFT*5, RIGHT*5.2, stroke_width=3)
        line.shift(DOWN * 0.4)
        self.add(line)
        
        answer1.shift(LEFT * 2)
        answer2.shift(LEFT * 1)
        # answer3.shift(LEFT * 0)
        answer4.shift(RIGHT * 1)
        answer5.shift(RIGHT * 2)
        answer6.shift(RIGHT * 3)
        answer7.shift(RIGHT * 4)
        answer8.shift(RIGHT * 5)
        
        answer_group = VGroup(answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8)
        answer_group.shift(DOWN * 1.5)
        self.add(answer_group) 
        
        self.wait(1)
        
        fx_number = MathTex(r"1x^4+3x^3+4x^2+8x^1+2").scale(1) 
        fx_number.shift(RIGHT * (5 - fx_number.get_right())) 
        fx_number.shift(UP * 2.5) 
        self.play(Transform(number_group2, fx_number))
        
        gx_number = MathTex(r"3x^3+9x^2+7x^1+5").scale(1) 
        gx_number.shift(RIGHT * (5 - gx_number.get_right()))
        gx_number.shift(UP * 1)
        self.play(Transform(number_group1, gx_number)) 
        
        self.wait(2) 
        
        hx_number = MathTex(r"3x^7+18x^6+46x^5+86x^4+121x^3+94x^2+54x^1+10").scale(1)
        hx_number.shift(RIGHT * (5 - gx_number.get_right()))
        hx_number.shift(DOWN * 1.5) 
        self.play(Transform(answer_group, hx_number))
        
        self.wait(5)
        
        self.play(FadeOut(VGroup(sign, line)))
        
        fx_parameter = MathTex(r"f(x)= \sum\limits_{i=0}^{n-1}a_i x^i=a_0+a_1x+ \cdots+a_{n-1}x^{n-1}").scale(0.8)
        fx_parameter.shift(LEFT * (6 + fx_parameter.get_left()))
        fx_parameter.shift(UP * 2.5)
        self.play(Transform(number_group2, fx_parameter))
        
        gx_parameter = MathTex(r"g(x)= \sum\limits_{i=0}^{m-1}b_i x^i=b_0+b_1x+ \cdots+b_{m-1}x^{m-1}").scale(0.8)
        gx_parameter.shift(LEFT * (6 + gx_parameter.get_left()))
        gx_parameter.shift(UP * 0.5)
        self.play(Transform(number_group1, gx_parameter)) 
        
        hx_fxg = MathTex(r"h(x)=f(x)g(x)").scale(0.8) 
        hx_fxg.shift(LEFT * (6 + hx_fxg.get_left())) 
        hx_fxg.shift(DOWN * 2)
        self.play(Transform(answer_group, hx_fxg))
        
        self.wait(3)
        
        hx_parameter = MathTex(r"h(x)=\sum\limits_{i=0}^{(n-1)+(m-1)}c_i x^i=c_0+c_1x+\cdots+c_{(n-1)+(m-1)}x^{(n-1)+(m-1)}").scale(0.8) 
        hx_parameter.shift(LEFT * (6 + hx_parameter.get_left())) 
        hx_parameter.shift(DOWN * 2) 
        self.play(Transform(answer_group, hx_parameter))
        
        self.wait(5)
