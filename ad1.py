from manimlib.imports import *
class final(Scene):
    CONFIG={
        "camera_config": {"background_color":YELLOW_C},
    }
    def construct(self):
        g = NumberPlane()
        t1 = TextMobject("Priced at").set_color(BLACK)
        t1.scale(3)
        t1.move_to(2.5*UP)

        t2 = TextMobject("Rs 799").set_color(BLACK)
        t2.scale(1.5)
        t2.move_to(0.25*UP+2*LEFT)
        line1 = Line(t2.get_right(), t2.get_left(), buff=0.1).set_color(BLACK)
        arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        arr1.next_to(t2, RIGHT, buff=0.1)
        t3 = TextMobject("Rs 299").set_color(BLACK)
        t3.scale(1.5)
        t3.next_to(arr1, RIGHT, buff=0.1)
        f1 = SurroundingRectangle(t3, buff=0.1).set_color(BLACK)
        ftext = TextMobject("With ", "a ", "Certificate\\\\",
        "of ","Completion","!").set_color(BLACK)
        ftext.scale(2)
        ftext.move_to(2*DOWN)






        self.play(GrowFromCenter(t1))
        self.play(GrowFromCenter(t2))
        self.play(ShowCreation(line1))
        self.play(GrowArrow(arr1))
        self.play(GrowFromCenter(t3))
        self.play(ShowCreation(f1))
        self.play(AnimationGroup(GrowFromCenter(ftext[0]),GrowFromCenter(ftext[1]), GrowFromCenter(ftext[2]), GrowFromCenter(ftext[3]), GrowFromCenter(ftext[4]), GrowFromCenter(ftext[5]), lag_ratio=0.3))
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(line1), FadeOut(arr1),
        FadeOut(t3), FadeOut(f1), FadeOut(ftext))



        self.wait()
        self.add(g)