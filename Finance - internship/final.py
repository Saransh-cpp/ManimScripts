from manimlib.imports import *
class Final(GraphScene):
    CONFIG = {
        "x_min":-5,
        "x_max": 5,
        "x_axis_width": 10,
        "y_axis_width": 11,
        "x_tick_frequency": 0.5,
        "x_labeled_nums": range(-5, 6),
        "x_axis_label": None,
        "y_min": -3,
        "y_max": 3,
        "y_axis_height": 6,
        "x_axis_height": 6,
        "y_tick_frequency": 0.5,
        "y_labeled_nums": range(-3, 4),
        "y_axis_label": None,
        "axes_color": RED,
        "graph_origin": ORIGIN,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": GOLD,
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "function_color": WHITE,
        "area_opacity": 0.8,
        "num_rects": 50,
        "light_source": 15 * DOWN + 7 * LEFT + 10 * OUT,
        "number_line_config": {
            "include_tip": True,
            },
        }  
    def construct(self):
        im = SVGMobject("./311831.svg")
        im.flip(RIGHT)
        self.add_sound("./YT3.mp3")
        
        text1 = TextMobject(" PHY ")
        text1.scale(2)
        self.add(text1)
        text1.move_to(55*UP+1.7*LEFT)
        text2 = TextMobject(" PHY ")
        text2.scale(2)
        text2.move_to(1.36*UP+1.7*LEFT)
        text = TextMobject(" PHY ")
        text.scale(2)
        text.move_to(3*UP+1.7*LEFT)
        text3 = TextMobject(" PHY ")
        text3.scale(2)
        text3.move_to(1.36*UP+1.7*LEFT)
        text4 = TextMobject(" PHY ")
        text4.scale(2)
        text4.move_to(1.5*UP+1.7*LEFT)

        text12 = TextMobject(" SUCKS ")
        text12.scale(2)
        text12.move_to(1.1*RIGHT+55*UP)
        self.add(text12)
        text22 = TextMobject(" SUCKS ")
        text22.scale(2)
        text22.move_to(1.36*UP+1.1*RIGHT)
        text21 = TextMobject(" SUCKS ")
        text21.scale(2)
        text21.move_to(3*UP+1.1*RIGHT)
        text32 = TextMobject(" SUCKS ")
        text32.scale(2)
        text32.move_to(1.36*UP+1.1*RIGHT)
        text42 = TextMobject(" SUCKS ")
        text42.scale(2)
        text42.move_to(1.5*UP+1.1*RIGHT)



        texta = TextMobject("ME")
        texta.move_to(55*UP)
        text1a = TextMobject("ME")
        text1a.scale(2)
        text1a.move_to(1.5*LEFT)
        
        textb = TextMobject("TH")
        textb.move_to(55*UP)
        text1b = TextMobject("TH")
        text1b.scale(2)
        text1b.move_to(1.5*RIGHT)

        newt = TexMobject("AND")
        newt.set_color(YELLOW)
        newt.scale(5)
        
        self.add(texta)
        self.add(textb)
        self.play(Write(im))
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(text2, text))
        self.play(ReplacementTransform(text, text3))
        self.play(ReplacementTransform(text3, text4))
        self.play(ReplacementTransform(text12, text22))
        self.play(ReplacementTransform(text22, text21))
        self.play(ReplacementTransform(text21, text32))
        self.play(ReplacementTransform(text32, text42))
        self.play(GrowFromCenter(newt))
        self.play(FadeOut(newt))
        self.play(Write(text1a, run_time=0.5))
        self.play(Write(text1b, run_time=0.5))
        self.wait()

        self.play(FadeOut(text4), FadeOut(text42), FadeOut(text1a), FadeOut(text1b), FadeOut(im))



        g = NumberPlane()   
        self.play(Write(g)) 
        self.wait(2)
        text1 = TextMobject(" Finding Area between\\\\ ",
                            " X axis and Log(x) in range [0,1]") 
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        self.wait()               
        self.setup_axes(animate=True)
        self.wait(2)
        text = TextMobject("Graphing Log(x)")
        text.move_to(3*RIGHT+3*UP)
        self.play(Write(text))
        self.wait()
        f = self.get_graph(self.func, x_min=0.01, x_max=5, color=YELLOW)
        self.play(Write(f, run_time=2))
        dot=Dot()
        dot.move_to(1*RIGHT)
        self.play(Write(dot))
        text4 = TextMobject("(1,0)")
        text4.next_to(dot, UP, buff= 0.1)
        self.play(Write(text4))
        self.play(FadeOut(text))
        text2 = TextMobject(" The Graph approaches \\\\",
        "negative infinity at\\\\",
        "x=0")
        text3 = TextMobject(" But the area of graph\\\\",
        "in the range [0,1]\\\\",
        " is still finite! ")
        text2.move_to(3*LEFT+2*UP)
        text3.move_to(3*RIGHT+2*DOWN)
        self.play(Write(text2, run_time=2))
        self.wait()
        self.play(Write(text3))
        self.wait(2)
        area = self.get_area(f,0.0001,1)
        self.play(FadeOut(text2),FadeOut(text3))
        self.wait()
        text5 = TextMobject(" The required area can be\\\\",
        " deduced using integration")
        text5.move_to(3.5*LEFT+2*UP)
        self.play(Write(area), Write(text5))
        self.wait()
        self.play(FadeOut(area), FadeOut(dot), FadeOut(text4), FadeOut(f), FadeOut(self.axes), FadeOut(text5))
        self.wait()
        text6 = TextMobject(" Integrating Log(x)")
        text6.scale(1.5)
        text6.move_to(3.2*UP)
        self.play(Write(text6))
        self.wait()
        t1 = TexMobject(r"\int \ln (x)dx")
        t1.move_to(5.5*LEFT+2*UP)
        self.play(Write(t1))
        self.wait()
        t2 = TexMobject(r"\int \ln (x).1dx")
        t2.move_to(5.5*LEFT+2*UP)
        self.play(Transform(t1, t2))
        self.wait()
        text7 = TextMobject("Using By Parts")
        text7.scale(1.5)
        text7.move_to(3.2*UP)
        self.play(ReplacementTransform(text6,text7))
        self.wait()
        t3 = TexMobject(r" = \ln(x).\int1dx", " -",r" \int (\frac{d}{dx}(\ln(x))\int1dx)dx" )
        t3.next_to(t2,RIGHT,buff=0.5)
        self.play(Write(t3))
        self.wait()
        brace1 = Brace(t3[0], DOWN)
        brace2 = Brace(t3[2], DOWN)
        b1 = brace1.get_text("$u(x)\int v(x)dx$")
        b2 = brace2.get_text(r"$\int(\frac{d}{dx}u(x)\int v(x)dx)dx $")
        self.play(GrowFromCenter(brace1), FadeIn(b1))
        self.wait()
        self.play(ReplacementTransform(brace1.copy(), brace2),
        ReplacementTransform(b1.copy(), b2))
        self.wait()
        tmid = TexMobject(r"\int \ln (x).1dx")
        tmid.move_to(3*LEFT+1*UP)
        t4 = TexMobject(r"=  x\ln(x)", "-", r"\int\frac{1}{x}.(x)dx")
        t4.next_to(tmid,RIGHT,buff=0.5)
        self.play(ReplacementTransform(t1,tmid), ReplacementTransform(t3, t4), FadeOut(brace1), FadeOut(brace2), FadeOut(b1), FadeOut(b2))
        self.wait()
        t5 = TexMobject(r"\int \ln (x)dx")
        t5.move_to(2.5*LEFT+1*UP)
        self.play(ReplacementTransform(tmid,t5))
        self.wait()
        t6 = TexMobject(r"=  x\ln(x)", "-","x","+ C")
        t6.next_to(tmid,RIGHT,buff=0.5)
        self.play(ReplacementTransform(t4,t6))
        self.wait()
        text8 = TextMobject("Putting up the limits")
        text8.scale(1.5)
        text8.move_to(3.2*UP)
        self.play(ReplacementTransform(text7,text8))
        self.wait()
        t7 = TexMobject(r"\int_0^1\ln (x)dx")
        t7.move_to(2.5*LEFT+1*UP)
        self.play(ReplacementTransform(t5,t7))
        self.wait()
        t8 = TexMobject(r"=  (x\ln(x)-x+ C)|_{0}^{1}")
        t8.next_to(tmid,RIGHT,buff=0.5)
        self.play(ReplacementTransform(t6,t8))
        self.wait()
        tmid1 = TexMobject(r"\int_0^1\ln (x)dx")
        tmid1.move_to(3.5*LEFT+1*UP)
        t9 = TexMobject(r"=    (1\ln(1)-1)"," -", "(",r"0\ln(0)","-0)")
        t9.next_to(tmid1,RIGHT,buff=0.5)
        self.play(ReplacementTransform(t8, t9), ReplacementTransform(t7, tmid1))
        self.wait()
        frame1 = SurroundingRectangle(t9[3], buff=0.1)
        frametext = TextMobject(" This expression here\\\\"," is not defined as ln(0)\\\\"," approaches negative infinity")
        frametext.next_to(frame1, DOWN, buff=0.3)
        self.play(ShowCreation(frame1), Write(frametext))
        self.wait()
        text9 = TextMobject(" We'll need to use limits to deduce\\\\",
        "the value of xln(x) at x=0")
        self.wait()
        text9.move_to(1.5*DOWN)
        self.play(ReplacementTransform(frametext, text9))
        self.wait(2)
        text10 = TextMobject("Deducing xln(x) at x=0")
        text10.scale(1.5)
        text10.move_to(3*UP)
        self.play(ReplacementTransform(text8, text10), FadeOut(frame1), FadeOut(text9), FadeOut(t9), FadeOut(tmid1))
        self.wait()
        lim1 = TexMobject(r"\lim_{x\rightarrow 0}","x",r"\ln(x)")
        lim1.move_to(3*LEFT+1*UP)
        self.play(Write(lim1))
        self.wait()
        frame2 = SurroundingRectangle(lim1[1],buff=0.1)
        lim2 = TexMobject(r"=  \lim_{x\rightarrow 0}\frac{\ln(x)}{\frac{1}{x}}")
        lim2.next_to(lim1, RIGHT, buff=0.5)
        self.play(Write(lim2))
        self.play(ShowCreation(frame2))
        self.wait()
        arr =Arrow(RIGHT,LEFT)
        arr.move_to(1.7*RIGHT+0.5*UP)
        self.play(ReplacementTransform(frame2, arr))
        self.wait()
        self.play(FadeOut(arr))
        lim3 = TexMobject(r"= -\lim_{x\rightarrow 0}\frac{\frac{1}{x}}{\frac{1}{x^{2}}}")
        lim3.next_to(lim2, RIGHT, buff=0.5)
        text11 = TextMobject("Using L'Hôpital's rule")
        text11.scale(1.5)
        text11.move_to(3*UP)
        self.play(ReplacementTransform(text10, text11))
        self.wait()
        self.play(Write(lim3))
        self.wait()
        lim4 =TexMobject(r"= -\lim_{x\rightarrow 0}x")
        lim4.next_to(lim2, RIGHT, buff=0.5) 
        self.play(ReplacementTransform(lim3, lim4))
        self.wait()
        zerotext = TexMobject("=  0")
        zerotext.next_to(lim2, RIGHT, buff=0.5) 
        self.play(ReplacementTransform(lim4, zerotext))
        self.wait()
        self.play(FadeOut(lim4), FadeOut(lim2), FadeOut(zerotext), FadeOut(text11), FadeOut(lim1))
        self.play(Write(g))
        self.setup_axes(animate=True)
        self.wait()
        newtext = TextMobject("Coming back to\\\\", 
        "our graph and\\\\", 
        "the integral")
        newtext.move_to(3*LEFT+2*UP)
        self.play(Write(newtext))
        self.wait()
        self.play(Write(f))
        self.play(Write(area))
        self.wait()
        newtex = TexMobject(r"\int_0^1 \ln(x)")
        newtex1 = TexMobject(r"=  (1\ln(1)-1)")
        newtex.move_to(2*RIGHT+2.5*UP)
        newtex1.next_to(newtex,RIGHT,buff=0.5)
        self.play(Write(newtex))
        self.wait()
        self.play(Write(newtex1))
        self.wait()
        newtex2 = TexMobject("=","-","1")
        newtex2.next_to(newtex,RIGHT,buff=0.5)
        self.play(ReplacementTransform(newtex1,newtex2))
        newframe = SurroundingRectangle(newtex2[1], buff=0.5)
        newframetext = TextMobject("'-' indicating area\\\\", "under the x axis")
        newframetext.next_to(newframe,UP,buff=0.1)
        self.play(ShowCreation(newframe))
        self.play(Write(newframetext))
        self.wait()
        self.play(FadeOut(newframe), FadeOut(newtex), FadeOut(newtex2), FadeOut(newframetext), FadeOut(newframetext))
        newtext1 = TextMobject("This area that looks\\\\",
        "infinite")
        newtext1.move_to(3*LEFT+2*UP)
        newtext2 = TextMobject("is actually equal\\\\"
        "to 1 sq unit!")
        newtext2.move_to(3*RIGHT+2*DOWN)
        newarr = Arrow(UP,DOWN)
        newarr.move_to(0.5*RIGHT+1*UP)
        self.play(ReplacementTransform(newtext, newtext1), GrowArrow(newarr))
        self.wait()
        self.play(Write(newtext2))
        self.wait()
        finaltext = TextMobject(" Thanks for waching :D")
        finaltext.move_to(3*LEFT+2*DOWN)
        self.play(Write(finaltext))
        self.wait(2)
        self.play(FadeOut(area), FadeOut(finaltext), FadeOut(g), FadeOut(self.axes), FadeOut(f), FadeOut(newarr), FadeOut(newtext1), FadeOut(newtext2))
        self.wait()
        
        










    def func(self, x):
        return math.log(x)
        
