from manimlib.imports import *
class fund(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        bank = ImageMobject("./bank.png")
        bank.scale(2)
        g= NumberPlane()
        city= ImageMobject("./city.png")
        city.scale(10)
        city.move_to(2.3*DOWN+1*LEFT)
        bank.move_to(4*RIGHT+2.4*DOWN)
        corp = ImageMobject("./corp.png")
        corp.move_to(3*DOWN+1.5*RIGHT)
        bucks = ImageMobject("./bucks.png")

        n1t1 = TextMobject("The first domain that we are talking about\\\\",
        "gives fixed returns over your investment").set_color(BLACK)
        n1t1.move_to(2*LEFT+3*UP)
        buck = ImageMobject("./bucks.png")
        buck.move_to(5*LEFT+1*UP)
        arr = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr.scale(0.5)
        arr.next_to(buck, RIGHT, buff=0.1)
        invest = TextMobject("Invest").set_color(RED)
        invest.scale(2)
        invest.next_to(arr, RIGHT, buff=0.1)
        t1 = ImageMobject("./return.png")
        t1.move_to(5*RIGHT+3*UP)
        t1.scale(0.5)
        t2 = TextMobject("Same every year").set_color(BLACK)
        arr1 = Arrow(UP,DOWN).set_color(BLACK)
        arr1.scale(0.5)
        arr1.next_to(t1, DOWN, buff=0.1)
        t2.next_to(arr1, DOWN, buff=0.1)
        t3 = TextMobject("For example - Fixed deposit and bonds").set_color(BLACK)
        t3.move_to(2*LEFT+3*UP)
        t4= TextMobject("The return is\\\\"
        "fixed in this\\\\"
        "domain").set_color(BLACK)
        t4.scale(0.7)
        t4.move_to(1.5*RIGHT+0.7*DOWN)
        at1 = TextMobject("Average return").set_color(BLACK)
        at2 = TextMobject("is 6-8 percent "
        "p.a.").set_color(BLACK)
        a = Arrow(LEFT,RIGHT).set_color(BLACK)
        a.scale(0.5)
        at1.move_to(4*LEFT+2.25*UP)
        a.next_to(at1, RIGHT, buff=0.1)
        at2.next_to(a, RIGHT, buff=0.1)

        bcloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        bcloud.next_to(corp, UP, buff=0.1)

        d = TextMobject("Depends upon").set_color(BLACK)
        bank2 = ImageMobject("./bank.png")
        time = ImageMobject("./time.png")
        a1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        a1.scale(0.5)
        a2 = Arrow(UP,DOWN).set_color(BLACK)
        a2.scale(0.5)
        d.move_to(5*LEFT+DOWN)
        a1.next_to(d, RIGHT, buff=0.1)
        a2.next_to(d, DOWN, buff=0.1)
        bank2.next_to(a1, RIGHT, buff=0.1)
        time.next_to(a2, DOWN, buff=0.1)

        f1 = TextMobject("It is the\\\\"
        "safest option\\\\" 
        "among all\\\\", "of them").set_color(BLACK)
        f2 = TextMobject("The", " low risk\\\\","-"," low return\\\\","option!")
        f2[0].set_color(BLACK)
        f2[1].set_color(RED)
        f2[2].set_color(BLACK)
        f2[3].set_color(RED)
        f2[4].set_color(BLACK)
        f1.move_to(2*LEFT+2*UP)
        f2.move_to(2*LEFT+UP)
        f1.scale(0.5)
        f1.move_to(1.5*RIGHT+0.7*DOWN)
        f2.scale(0.7)
        f2.move_to(1.5*RIGHT+0.7*DOWN)
    







        self.play(FadeIn(city))
        self.play(FadeInFromDown(bank))
        self.play(Write(n1t1))
        self.play(FadeInFromDown(buck))
        self.play(GrowArrow(arr))
        self.play(Write(invest))
        self.play(FadeIn(t1))
        self.play(GrowArrow(arr1))
        self.play(Write(t2))
        self.play(ReplacementTransform(n1t1, t3))
        self.play(GrowFromEdge(corp,LEFT,run_time=0.5))
        self.play(Write(bcloud))
        self.play(Write(t4))
        self.play(Write(at1))
        self.play(GrowArrow(a))
        self.play(Write(at2))
        self.play(Write(d))
        self.play(GrowArrow(a1), GrowArrow(a2))
        self.play(GrowFromCenter(bank2), GrowFromCenter(time))
        self.play(FadeOut(t4))
        self.play(Write(f1))
        self.play(FadeOut(f1))
        self.play(Write(f2))
        self.play(FadeOut(corp), FadeOut(at1), FadeOut(a), FadeOut(at2),
        FadeOut(bcloud), FadeOut(f2), FadeOut(t1), FadeOut(t2), FadeOut(t3),
        FadeOut(arr1), FadeOut(buck), FadeOut(invest), FadeOut(arr),
        FadeOut(bank), FadeOut(city))


        










        self.add(g)

