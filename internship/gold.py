from manimlib.imports import *
class gold(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        j = ImageMobject("./jewel.png")
        j.scale(4)

        s4t1 = TextMobject("The 4th and the last\\\\",
        "domain is metal investment").set_color(BLACK)
        s4t1.move_to(4*LEFT+3*UP)
        s4t2 = TextMobject("What is\\\\",
        "metal\\\\", "investment?").set_color(BLACK)
        s4t2.move_to(4*RIGHT+0.4*UP)
        s4t3 = TextMobject("It means, you\\\\"
        "invest in some\\\\"
        "kind of metal.\\\\"
        "Like-").set_color(BLACK)
        avg = TextMobject("Average return").set_color(BLACK)
        avg.move_to(2*LEFT+3.5*DOWN)
        avga = Arrow(LEFT,RIGHT).set_color(BLACK)
        avg1 = TextMobject("8 percent p.a.").set_color(BLACK)
        avga.next_to(avg, RIGHT, buff=0.1)
        avg1.next_to(avga, RIGHT, buff=0.1)
        s4t4 = TextMobject("Similar as fixed deposit returns").set_color(BLACK)
        s4t3.scale(0.75)
        s4t3.move_to(4*RIGHT+0.4*UP)
        s4t4.move_to(3.5*DOWN)

        gold = ImageMobject("./gold.png")
        silver = ImageMobject("./silver.png")
        platinum = ImageMobject("./platinum.png")
        gold.move_to(5*LEFT+UP)
        platinum.move_to(3*RIGHT+3*UP)
        silver.move_to(6*RIGHT+2.5*UP)

        c4 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        c4.scale(1.5)
        c4.move_to(4*RIGHT)
        




        self.play(FadeInFromDown(j))
        self.play(Write(s4t1))
        self.play(Write(c4))
        self.play(Write(s4t2))
        self.play(FadeOut(s4t2))
        self.play(Write(s4t3))
        self.play(GrowFromCenter(gold))
        self.play(GrowFromCenter(silver))
        self.play(GrowFromCenter(platinum))
        self.play(Write(avg))
        self.play(GrowArrow(avga))
        self.play(Write(avg1))
        self.play(FadeOut(avg), FadeOut(avga), FadeOut(avg1))
        self.play(Write(s4t4))





        self.wait()
        self.add(g)