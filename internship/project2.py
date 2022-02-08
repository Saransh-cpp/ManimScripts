from manimlib.imports import *
class ad(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        
        building = ImageMobject("./build.png")
        building.scale(6)
        building.move_to(0.7*DOWN)

        man1 = ImageMobject("./man1.png")
        man2 = ImageMobject("./man2.png")
        man1.move_to(1.4*RIGHT+3.1*DOWN)
        man2.move_to(1*LEFT+3.1*DOWN)
        man1s = ImageMobject("./man1.png")
        man1s.move_to(10*RIGHT+3.1*DOWN)
        man2s = ImageMobject("./man2.png")
        man2s.move_to(10**LEFT+3.1*DOWN)
        man1e = ImageMobject("./man1.png")
        man1e.move_to(10*LEFT+3.1*DOWN)
        man2e = ImageMobject("./man2.png")
        man2e.move_to(10*RIGHT+3.1*DOWN)



        man1cloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        man2cloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        man2cloud1.flip(UP)
        man1cloud1.move_to(1.5*RIGHT+1*DOWN)
        man2cloud1.next_to(man2, UP, buff=0.1)
        man1cloud1text1 = TextMobject("Oh hi Raj!\\\\",
        "Remember\\\\"
        , "me?").set_color(BLACK)
        man2cloud1text1 = TextMobject("Wait,\\\\",
        "Rohan?").set_color(BLACK)
        man1cloud1text1.move_to(1.5*RIGHT+0.7*DOWN)
        man2cloud1text1.move_to(1*LEFT+0.7*DOWN)
        man1cloud1text1.scale(0.7)
        man1cloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        man1cloud.move_to(1.5*RIGHT+1*DOWN)

        man1cloud2 =  SVGMobject("./cloud1.svg").set_stroke(BLACK)
        man1cloud1text2 = TextMobject("Yes!\\\\", "me").set_color(BLACK)
        man1cloud1text3 = TextMobject("So, what\\\\"
        ,"you up to\\\\",
        "nowadays").set_color(BLACK)
        man2cloud1text3 = TextMobject("Just trying\\\\",
        "to earn\\\\",
        "some money").set_color(BLACK)
        man2cloud1text4 = TextMobject("Quite tough\\\\",
        "nowadays").set_color(BLACK)
        man1cloud1text4 = TextMobject("What? That's\\\\",
        "so easy").set_color(BLACK)
        man1cloud1text5 = TextMobject("Even generating\\\\",
        "additional revenue\\\\"
        "is so easy").set_color(BLACK)
        man1cloud1text6 = TextMobject("Haven't you\\\\",
        "heard about\\\\",
        "MONEYSEEDS?").set_color(BLACK)
        man2cloud1text5 = TextMobject("No? What\\\\",
        "is that?").set_color(BLACK)
        man1cloud2text1 = TextMobject("Professionals at\\\\",
        "moneyseeds work hard\\\\",
        "to provide us crucial\\\\",
        "information about\\\\",
        "everything related to\\\\",
        "personal finance!").set_color(BLACK)
        man1cloud2text2 = TextMobject("In the past few\\\\",
        "days, I have learnt\\\\",
        "so much about personal\\\\",
        "finance. All thanks\\\\",
        "to moneyseeds").set_color(BLACK)
        man1cloud2text3 = TextMobject("Their program is\\\\",
        "open with a limited\\\\",
        "number of seats\\\\",
        "Enrol Today!").set_color(BLACK)
        man1cloud1text3.scale(0.7)
        man1cloud1text4.scale(0.7)
        man1cloud1text5.scale(0.5)
        man1cloud1text6.scale(0.5)
        man1cloud2text1.scale(0.7)
        man1cloud2text2.scale(0.7)
        man1cloud2text3.scale(0.7)
        man2cloud1text3.scale(0.7)
        man2cloud1text4.scale(0.7)
        man2cloud1text5.scale(0.7)
        man1cloud1text3.move_to(1.5*RIGHT+0.7*DOWN)
        man2cloud1text3.move_to(1*LEFT+0.7*DOWN)
        man1cloud1text2.move_to(1.5*RIGHT+0.7*DOWN)
        man1cloud1text4.move_to(1.5*RIGHT+0.7*DOWN)
        man2cloud1text4.move_to(1*LEFT+0.7*DOWN)
        man1cloud1text4.move_to(1.5*RIGHT+0.7*DOWN)
        man1cloud1text5.move_to(1.5*RIGHT+0.7*DOWN)
        man1cloud1text6.move_to(1.5*RIGHT+0.7*DOWN)
        man2cloud1text5.move_to(1*LEFT+0.7*DOWN)
        man1cloud2text1.move_to(1.5*RIGHT+0.6*UP)
        man1cloud2text2.move_to(1.5*RIGHT+0.6*UP)
        man1cloud2text3.move_to(1.5*RIGHT+0.6*UP)
        man1cloud2.scale(2)
        man1cloud2.next_to(man1, UP, buff=0.1)

        man2cloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        man2cloud2.flip(UP)
        man2cloud2.scale(2)
        man2cloud2.next_to(man2, UP, buff=0.1)
        
        man2cloud2text1 = TextMobject("Oh, that actually\\\\",
        "sounds interesting\\\\",
        "and helpful. I'll \\\\",
        "enrol today!").set_color(BLACK)
        man2cloud2text1.scale(0.9)

        man1cloud1text = TextMobject("Oh, I gotta\\\\",
        "go, let's meet\\\\",
        "tomorrow again?").set_color(BLACK)
        man1cloud1text.scale(0.5)
        man2cloud1text = TextMobject("Yeah!, Bye\\\\",
        "Nice to meet\\\\",
        "you again").set_color(BLACK)
        man2cloud1text.scale(0.5)
        man2cloud2text1.move_to(1*LEFT+0.5*UP)
        man1cloud1text.move_to(1.5*RIGHT+0.7*DOWN)
        man2cloud1text.move_to(1*LEFT+0.7*DOWN)

        nday = TextMobject("Next Day").set_color(BLACK)
        nday.scale(2)
        nday.move_to(3*UP)
        m1 = ImageMobject("./man1.png")
        m2 = ImageMobject("./man2.png")
        m1.move_to(1.4*RIGHT+3.1*DOWN)
        m2.move_to(1*LEFT+3.1*DOWN)

        m2c1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        m2c1.next_to(m2, UP, buff=0.1)
        m1c1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        m1c1.move_to(1.5*RIGHT+1*DOWN)
        m2c1t1 = TextMobject("Oh hi").set_color(BLACK)
        m2c1t2 = TextMobject("Dude that\\\\",
        "course was\\\\",
        "so amazing!").set_color(BLACK)
        m1c1t1 = TextMobject("Told you!\\\\",
        "All doubts\\\\",
        "cleared?").set_color(BLACK)
        m2c1t3 =TextMobject("Yeah, I even\\\\",
        "started\\\\",
        "investing").set_color(BLACK)
        m2c1t4 = TextMobject("Never thought\\\\",
        "this all was\\\\",
        "so easy!").set_color(BLACK)
        m1c1t2 = TextMobject("Yeah! Now you\\\\",
        "are even set\\\\",
        "for retirement").set_color(BLACK)
        m1f = TextMobject("What are ",
        "you guys ",
        "waiting for?").set_color(BLACK)
        m1f.move_to(3*UP)
        m1f1 = TextMobject("ENROL NOW!").set_color(RED)
        m1f1.scale(2)
        m1f1.move_to(3*UP)
        m2c1t1.move_to(1*LEFT+0.7*DOWN)
        m2c1t2.scale(0.7)
        m2c1t2.move_to(1*LEFT+0.7*DOWN)
        m1c1t1.scale(0.7)
        m1c1t1.move_to(1.5*RIGHT+0.7*DOWN)
        m2c1t3.scale(0.7)
        m2c1t3.move_to(1*LEFT+0.7*DOWN)
        m2c1t4.scale(0.5)
        m2c1t4.move_to(1*LEFT+0.7*DOWN)
        m1c1t2.scale(0.5)
        m1c1t2.move_to(1.5*RIGHT+0.7*DOWN)

        


        



        
        self.play(FadeInFromDown(building))
        self.play(FadeInFromDown(man1), FadeInFromDown(man2))
        self.play(Write(man1cloud1))
        self.play(Write(man1cloud1text1))
        self.wait()
        self.play(Write(man2cloud1))
        self.play(Write(man2cloud1text1))
        self.wait()
        self.play(FadeOut(man1cloud1text1))
        self.play(Write(man1cloud1text2))
        self.play(FadeOut(man1cloud1text2))
        self.play(Write(man1cloud1text3))
        self.play(FadeOut(man2cloud1text1))
        self.play(Write(man2cloud1text3))
        self.play(FadeOut(man2cloud1text3))
        self.play(Write(man2cloud1text4))
        self.play(FadeOut(man1cloud1text3))
        self.play(Write(man1cloud1text4))
        self.play(FadeOut(man1cloud1text4))
        self.play(Write(man1cloud1text5))
        self.play(FadeOut(man1cloud1text5))
        self.play(Write(man1cloud1text6))
        self.play(FadeOut(man2cloud1text4))
        self.play(Write(man2cloud1text5))
        self.play(FadeOut(man2cloud1), FadeOut(man2cloud1text5), FadeOut(man1cloud1text6))
        self.play(ReplacementTransform(man1cloud1, man1cloud2))
        self.play(Write(man1cloud2text1, run_time=3))
        self.wait()
        self.play(FadeOut(man1cloud2text1))
        self.play(Write(man1cloud2text2, run_time=3))
        self.wait()
        self.play(FadeOut(man1cloud2text2))
        self.play(Write(man1cloud2text3, run_time=3))
        self.wait()
        self.play(FadeOut(man1cloud2text3), FadeOut(man1cloud2))
        self.play(Write(man2cloud2))
        self.play(Write(man2cloud2text1, run_time=2))
        self.wait()
        self.play(FadeOut(man2cloud2text1))
        self.play(ReplacementTransform(man2cloud2, man2cloud1))
        self.play(Write(man1cloud))
        self.play(Write(man1cloud1text))
        self.play(FadeOut(man1cloud1text))
        self.play(Write(man2cloud1text))
        self.play(FadeOut(man2cloud1text))
        self.play(FadeOut(man1cloud), FadeOut(man2cloud1))
        self.play(ReplacementTransform(man1, man1e), ReplacementTransform(man2, man2e))
        self.play(Write(nday))
        self.play(FadeOut(nday))
        self.play(GrowFromEdge(m1, RIGHT), GrowFromEdge(m2,LEFT))
        self.play(Write(m2c1))
        self.play(Write(m2c1t1))
        self.play(FadeOut(m2c1t1))
        self.play(Write(m2c1t2))
        self.play(Write(m1c1))
        self.play(Write(m1c1t1))
        self.play(FadeOut(m1c1t1))
        self.play(FadeOut(m2c1t2))
        self.play(Write(m2c1t3))
        self.play(FadeOut(m2c1t3))
        self.play(Write(m2c1t4))
        self.play(Write(m1c1t2))
        self.play(FadeOut(m1c1), FadeOut(m2c1), FadeOut(m2c1t4), FadeOut(m1c1t2) )
        self.play(Write(m1f))
        self.play(FadeOut(m1f))
        self.play(Write(m1f1))
        

        











        self.wait()
        