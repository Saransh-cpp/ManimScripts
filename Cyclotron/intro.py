from manimlib.imports import *

class Simulate(Scene):
    def construct(self):

        g = NumberPlane()

        rec = Rectangle(width = 6, height = 1).move_to(4*RIGHT + 2*UP)

        sq1 = Square()
        sq1.move_to(RIGHT)

        d1 = Dot()
        d1.move_to(4*LEFT)

        l1 = Line()
        l1.rotate(PI/2)
        l1.move_to(2.05*RIGHT+UP)

        d2 = Dot()
        # d2.move_to(3*RIGHT)

        d3 = Dot()
        d3.move_to(3*RIGHT)

        sq2 = Square()
        sq2.move_to(4*RIGHT)

        l2 = Line()
        l2.rotate(PI/2)
        l2.move_to(5.05*RIGHT+UP)

        sq3 = Square()
        sq3.move_to(RIGHT)

        d4 = Dot()
        # d2.move_to(3*RIGHT)

        l4 = Line().scale(2)
        l4.move_to(3*UP + 3*RIGHT)

        x = TextMobject('x').scale(1.3)

        x.next_to(l4, UP, buff = 0.3)

        lf = Line().scale(10)
        lf.move_to(DOWN)

        

        # self.add(g)
        self.play(Write(lf))
        self.play(Write(sq1), Write(d1))
        self.play(Write(rec), Write(l1))
        # self.play(AnimationGroup(ReplacementTransform(d1,d2), AnimationGroup(ReplacementTransform(sq1, sq2), ReplacementTransform(l1, l2)), lag_ratio = 0.35))
        self.play(ReplacementTransform(d1, d2))
        self.play(ReplacementTransform(d2,d3), ReplacementTransform(sq1, sq2), ReplacementTransform(l1, l2))
        self.play(ReplacementTransform(d3, d4), ReplacementTransform(sq2, sq3))
        self.play(Write(l4), Write(x))