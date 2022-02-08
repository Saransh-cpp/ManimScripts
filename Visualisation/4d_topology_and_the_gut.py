from manim import *


class Intro(Scene):
    config.background_color = YELLOW_C

    def construct(self):

        g = NumberPlane()
        self.add_sound(
            "Soft Inspirational Background Music for Videos & Presentation.mp3"
        )
        # self.add(g)

        title1 = Tex("Mathematical Visualisation Project").set_color(BLACK)
        title2 = Tex("4th Dimension, Topology and").set_color(BLACK)
        title3 = Tex("The Grand Unified Theory").set_color(BLACK)
        credit = Tex("Saransh Chopra, Parth Tripathi and Naman Priyadarshi").set_color(
            BLACK
        )

        title1.scale(0.9)
        title2.scale(1.5)
        title3.scale(1.5)
        credit.scale(0.75)
        title1.move_to(2 * UP)
        title2.next_to(title1, DOWN, buff=1)
        title3.next_to(title2, DOWN, buff=0.25)
        credit.next_to(title3, DOWN, buff=1.25)

        self.play(Write(title1))
        self.play(Write(title2))
        self.play(Write(title3))
        self.play(Write(credit))

        self.play(FadeOut(title1), FadeOut(title2), FadeOut(title3), FadeOut(credit))

        intro_text1 = Tex("Through this project we will try to help").set_color(BLACK)
        intro_text2 = Tex(
            "you visualise some stuff that can not be visualised,"
        ).set_color(BLACK)
        intro_text3 = Tex("and obviously, we will fail.").set_color(BLACK)
        intro_text4 = Tex("But you will learn a lot through this journey!").set_color(
            BLACK
        )
        intro_text5 = Tex("SO").set_color(RED)
        intro_text6 = Tex("BUCKLE").set_color(RED)
        intro_text7 = Tex("UP!").set_color(RED)

        intro_text1.move_to(1.75 * UP)
        intro_text5.scale(2)
        intro_text6.scale(2)
        intro_text7.rotate(PI / 2)

        intro_text2.next_to(intro_text1, DOWN, buff=0.25)
        intro_text3.next_to(intro_text2, DOWN, buff=0.25)
        intro_text4.next_to(intro_text3, DOWN, buff=0.25)
        intro_text5.move_to(2 * DOWN + 2.5 * LEFT)
        intro_text6.next_to(intro_text5, RIGHT, buff=0.5)
        intro_text7.next_to(intro_text6, RIGHT, buff=0.1)

        self.play(Write(intro_text1))
        self.play(Write(intro_text2))
        self.play(Write(intro_text3))
        self.play(Write(intro_text4))
        self.play(GrowFromCenter(intro_text5, run_time=0.5))
        self.play(GrowFromCenter(intro_text6, run_time=0.5))
        self.play(GrowFromCenter(intro_text7, run_time=0.5))
        self.wait()
        self.play(
            FadeOut(intro_text1),
            FadeOut(intro_text2),
            FadeOut(intro_text3),
            FadeOut(intro_text4),
            FadeOut(intro_text5),
            FadeOut(intro_text6),
            FadeOut(intro_text7),
        )

        tech_text1 = Tex("Let us first have a quick look at the").set_color(BLACK)
        tech_text2 = Tex("Tech Stack that we are using.").set_color(BLACK)
        tech_text3 = Tex("All the animations that you have seen").set_color(BLACK)
        tech_text4 = Tex("till now and most of the ones which").set_color(BLACK)
        tech_text5 = Tex("you will be seeing, are made by us.").set_color(BLACK)

        tech_text1.move_to(1.75 * UP)
        tech_text2.next_to(tech_text1, DOWN, buff=0.25)
        tech_text3.next_to(tech_text2, DOWN, buff=0.25)
        tech_text4.next_to(tech_text3, DOWN, buff=0.25)
        tech_text5.next_to(tech_text4, DOWN, buff=0.25)

        self.play(Write(tech_text1))
        self.play(Write(tech_text2))
        self.play(Write(tech_text3))
        self.play(Write(tech_text4))
        self.play(Write(tech_text5))
        self.play(
            FadeOut(tech_text1),
            FadeOut(tech_text2),
            FadeOut(tech_text3),
            FadeOut(tech_text4),
            FadeOut(tech_text5),
        )

        stack1a = Tex("The TECH STACK").set_color(RED).scale(3)
        stack1b = Tex("The TECH STACK").set_color(BLACK).scale(1.5).move_to(3 * UP)

        stack_c1 = Circle(radius=2)
        stack2a = Tex("Manim").set_color(RED)
        stack2b = Tex("A Mathematical").set_color(RED)
        stack2c = Tex("Animation").set_color(RED)
        stack2d = Tex("Engine").set_color(RED)
        stack2e = Tex("Manim").set_color(BLACK)

        stack2a.move_to(UP)
        stack2b.next_to(stack2a, DOWN, buff=0.5)
        stack2c.next_to(stack2b, DOWN, buff=0.25)
        stack2d.next_to(stack2c, DOWN, buff=0.25)
        stack2e.move_to(2.5 * UP + 5.25 * LEFT)

        stack_image1 = ImageMobject("cropped.png").scale(0.25).move_to(4.5 * RIGHT)
        stack_image2 = ImageMobject("cropped (1).png").move_to(4.5 * LEFT)

        stack_r1 = (
            Rectangle(length=1, width=4).set_color(BLACK).scale(3).move_to(0.8 * DOWN)
        )

        stack_c2 = Circle(radius=0.75).move_to(0.75 * DOWN)
        stack_image3 = (
            ImageMobject("289-2896071_python-logo-png-165709.png")
            .scale(0.17)
            .move_to(0.75 * DOWN)
        )
        stack3 = Tex("Python").move_to(0.75 * DOWN).scale(0.8).set_color(BLACK)

        stack_l1 = Line().move_to(0.75 * DOWN + 1.75 * RIGHT).set_color(BLACK)
        stack_l2 = Line().move_to(0.75 * DOWN + 1.75 * LEFT).set_color(BLACK)
        stack_l3 = Line().scale(0.3).move_to(1.8 * DOWN).rotate(PI / 2).set_color(BLACK)
        stack_l4 = Line().scale(0.3).move_to(0.3 * UP).rotate(PI / 2).set_color(BLACK)

        stack_c3 = Circle(radius=0.75).next_to(stack_l1, RIGHT, buff=0.00001)
        stack_c4 = Circle(radius=0.75).next_to(stack_l2, LEFT, buff=0.00001)
        stack_c5 = Circle(radius=0.75).next_to(stack_l3, DOWN, buff=0.00001)
        stack_c6 = Circle(radius=0.75).next_to(stack_l4, UP, buff=0.00001)

        stack_image4 = ImageMobject("miktex2018.png").scale(0.18).move_to(1.35 * UP)
        stack4 = Tex("MikTEX").move_to(1.4 * UP).scale(0.7).set_color(BLACK)

        stack_image5 = (
            ImageMobject("729418.png").scale(0.7).move_to(0.75 * DOWN + 3.5 * LEFT)
        )
        stack5 = (
            Tex("FFmpeg").move_to(0.75 * DOWN + 3.5 * LEFT).scale(0.7).set_color(BLACK)
        )

        stack_image6 = (
            ImageMobject("cairo-banner.png")
            .scale(0.5)
            .move_to(0.75 * DOWN + 3.5 * RIGHT)
        )
        stack6 = (
            Tex("Cairo").move_to(0.75 * DOWN + 3.5 * RIGHT).scale(0.7).set_color(BLACK)
        )

        stack_image7 = ImageMobject("sox-logo.png").scale(1.5).move_to(2.85 * DOWN)
        stack7 = Tex("SoX").move_to(2.9 * DOWN).scale(0.7).set_color(BLACK)

        self.play(GrowFromCenter(stack1a, run_time=0.75))
        self.wait()
        self.play(ReplacementTransform(stack1a, stack1b))
        self.play(Write(stack_c1))
        self.play(Write(stack2a))
        self.play(Write(stack2b))
        self.play(Write(stack2c))
        self.play(Write(stack2d))
        self.play(GrowFromCenter(stack_image1), GrowFromCenter(stack_image2))
        self.wait()
        self.play(FadeOut(stack_image1), FadeOut(stack_image2))
        self.play(
            ReplacementTransform(stack_c1, stack_r1),
            FadeOut(stack2b),
            FadeOut(stack2c),
            FadeOut(stack2d),
            ReplacementTransform(stack2a, stack2e),
        )
        self.play(Write(stack_c2))
        self.play(GrowFromCenter(stack_image3))
        self.wait()
        self.play(FadeOut(stack_image3))
        self.play(Write(stack3))
        self.play(
            GrowFromEdge(stack_l1, LEFT),
            GrowFromEdge(stack_l2, RIGHT),
            GrowFromEdge(stack_l3, UP),
            GrowFromEdge(stack_l4, DOWN),
        )
        self.play(Write(stack_c3), Write(stack_c4), Write(stack_c5), Write(stack_c6))
        self.play(GrowFromCenter(stack_image4))
        self.play(FadeOut(stack_image4))
        self.play(Write(stack4))
        self.play(GrowFromCenter(stack_image5))
        self.play(FadeOut(stack_image5))
        self.play(Write(stack5))
        self.play(GrowFromCenter(stack_image6))
        self.play(FadeOut(stack_image6))
        self.play(Write(stack6))
        self.play(GrowFromCenter(stack_image7))
        self.play(FadeOut(stack_image7))
        self.play(Write(stack7))


class ShadowTesseract(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):

        g = NumberPlane()
        # self.add(g)
        self.add_sound("2016-11-20_-_Anticipation_-_David_Fesliyan.mp3")

        axes = ThreeDAxes().set_color(BLACK)
        s1 = Square().set_color(BLACK).scale(1.5).move_to(1 * LEFT + 1 * DOWN)
        s2 = Square().set_color(BLACK).scale(1.5).move_to(1 * RIGHT + 1 * UP)

        l1 = Line(start=0.5 * UP + 2.5 * LEFT, end=0.5 * LEFT + 2.5 * UP).set_color(
            BLACK
        )
        l2 = Line(start=2.5 * DOWN + 2.5 * LEFT, end=0.5 * LEFT + 0.5 * DOWN).set_color(
            BLACK
        )
        l3 = Line(end=2.5 * UP + 2.5 * RIGHT, start=0.5 * RIGHT + 0.5 * UP).set_color(
            BLACK
        )
        l4 = Line(
            start=0.5 * RIGHT + 2.5 * DOWN, end=0.5 * DOWN + 2.5 * RIGHT
        ).set_color(BLACK)

        c = Cube().set_color(BLACK)

        c1 = Cube().move_to(2 * DOWN)
        c2 = Cube().move_to(2.5 * UP)
        c1.set_z(-1)
        c2.set_z(2)

        line3d1 = Line3D(start=np.array([-1, -1, 0]), end=np.array([-1, 3.5, 3]))
        line3d2 = Line3D(start=np.array([-1, -3, 0]), end=np.array([-1, 1.5, 3]))
        line3d3 = Line3D(start=np.array([1, -1, 0]), end=np.array([1, 3.5, 3]))
        line3d4 = Line3D(start=np.array([1, -3, 0]), end=np.array([1, 1.5, 3]))
        line3d5 = Line3D(start=np.array([-1, -1, -2]), end=np.array([-1, 3.5, 1]))
        line3d6 = Line3D(start=np.array([-1, -3, -2]), end=np.array([-1, 1.5, 1]))
        line3d7 = Line3D(start=np.array([1, -1, -2]), end=np.array([1, 3.5, 1]))
        line3d8 = Line3D(start=np.array([1, -3, -2]), end=np.array([1, 1.5, 1]))

        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2)
        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
        )
        self.wait(2)

        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.play(Create(axes))
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        self.play(
            FadeOut(axes),
            FadeOut(s1),
            FadeOut(s2),
            FadeOut(l1),
            FadeOut(l2),
            FadeOut(l3),
            FadeOut(l4),
        )
        self.wait()
        self.play(Create(c))
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.play(Create(axes))
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        self.play(
            FadeOut(c),
        )
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(c1), Create(c2))
        self.wait(5)
        self.play(
            Write(line3d1, run_time=2),
            Write(line3d2, run_time=2),
            Write(line3d3, run_time=2),
            Write(line3d4, run_time=2),
            # Write(c2),
            Write(line3d5, run_time=2),
            Write(line3d6, run_time=2),
            Write(line3d7, run_time=2),
            Write(line3d8, run_time=2),
            # Write(c2)
        )
        self.wait(10)


class BuildingTesseract(Scene):
    config.background_color = YELLOW_C

    def construct(self):

        d1 = Dot().move_to(2 * LEFT).set_color(BLACK)
        d2 = Dot().move_to(2 * RIGHT).set_color(BLACK)

        l1 = Line(start=2 * LEFT, end=2 * RIGHT).set_color(BLACK)
        l2 = Line(start=2 * LEFT, end=2 * RIGHT).move_to(2 * UP).set_color(BLACK)
        l3 = Line(start=2 * DOWN, end=2 * UP).move_to(2 * RIGHT).set_color(BLACK)
        l4 = Line(start=2 * DOWN, end=2 * UP).move_to(2 * LEFT).set_color(BLACK)
        l5 = Line(start=2 * LEFT, end=2 * RIGHT).move_to(2 * DOWN).set_color(BLACK)

        s1 = Square().set_color(BLACK).scale(1.5).move_to(1 * LEFT + 1 * DOWN)
        s2 = Square().set_color(BLACK).scale(1.5).move_to(1 * RIGHT + 1 * UP)

        l21 = Line(start=0.5 * UP + 2.5 * LEFT, end=0.5 * LEFT + 2.5 * UP).set_color(
            BLACK
        )
        l22 = Line(
            start=2.5 * DOWN + 2.5 * LEFT, end=0.5 * LEFT + 0.5 * DOWN
        ).set_color(BLACK)
        l23 = Line(end=2.5 * UP + 2.5 * RIGHT, start=0.5 * RIGHT + 0.5 * UP).set_color(
            BLACK
        )
        l24 = Line(
            start=0.5 * RIGHT + 2.5 * DOWN, end=0.5 * DOWN + 2.5 * RIGHT
        ).set_color(BLACK)

        self.play(Write(d1), Write(d2))
        self.wait(2)
        self.play(Write(l1), FadeOut(d1), FadeOut(d2))
        self.wait(2)
        self.play(ReplacementTransform(l1, l2))
        self.play(Write(l3), Write(l4), Write(l5))
        self.wait(2)
        self.play(FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeOut(l5))
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2)
        self.play(
            Write(l21),
            Write(l22),
            Write(l23),
            Write(l24),
        )
        self.wait(2)


class Mobius(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):
        def mobius(t):
            return np.array(
                [
                    (10 + 2 * np.cos(t / 2)) * np.cos(t),
                    (10 + 2 * np.cos(t / 2)) * np.sin(t),
                    2 * np.sin(t / 2),
                ]
            )

        mob = ParametricFunction(
            mobius,
            color=BLUE,
            t_range=np.array([0, 4 * PI]),
            fill_opacity=50,
            # stroke_width=3
        )
        mob.scale(0.5).move_to(DOWN)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(Write(mob, run_time=3))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(30)


class Tess(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().set_color(BLACK)
        self.play(Create(axes))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Write(Cube(fill_opacity=0, stroke_width=2).scale(2).set_color(BLACK)))
        self.wait(5)
        self.play(Write(Cube(fill_opacity=0, stroke_width=2).set_color(BLACK)))
        self.wait(5)
        l1 = Line3D(start=np.array([-2, -2, -2]), end=np.array([-1, -1, -1]))
        l2 = Line3D(start=np.array([2, 2, 2]), end=np.array([1, 1, 1]))
        l3 = Line3D(start=np.array([-2, -2, 2]), end=np.array([-1, -1, 1]))
        l4 = Line3D(start=np.array([-2, 2, -2]), end=np.array([-1, 1, -1]))
        l5 = Line3D(start=np.array([2, -2, -2]), end=np.array([1, -1, -1]))
        l6 = Line3D(start=np.array([2, 2, -2]), end=np.array([1, 1, -1]))
        l7 = Line3D(start=np.array([-2, 2, 2]), end=np.array([-1, 1, 1]))
        l8 = Line3D(start=np.array([2, -2, 2]), end=np.array([1, -1, 1]))
        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
            Write(l5),
            Write(l6),
            Write(l7),
            Write(l8),
        )
        self.wait(5)


class TwoDCreature(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):
        # self.add(NumberPlane())
        # self.add_sound('Soft Inspirational Background Music for Videos & Presentation.mp3')

        axes = ThreeDAxes().set_color(BLACK)

        l1 = Line().scale(2).set_color(BLACK).rotate(PI / 2).move_to(4 * LEFT)
        l2 = Line().scale(2).set_color(BLACK).move_to(2 * UP + 2 * LEFT)
        l3 = Line().scale(2).set_color(BLACK).move_to(2 * DOWN + 2 * LEFT)
        l4 = (
            Line()
            .scale(2)
            .set_color(BLACK)
            .rotate(PI / 4)
            .move_to(1.4 * RIGHT + 0.6 * DOWN)
        )

        home = Tex("Home").move_to(2 * LEFT).set_color(BLACK)
        you = Tex("You").move_to(RIGHT + 2 * UP).set_color(BLACK)
        circ = Circle(radius=0.25).set_color(BLACK).move_to(RIGHT + UP)

        sph = Sphere().move_to(RIGHT + UP).set_z(2)

        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
        )

        self.play(Write(home))
        self.wait(2)
        self.play(Write(circ), Write(you))
        self.play(circ.animate.shift(UP))
        self.wait()
        self.play(circ.animate.shift(2 * DOWN))
        self.wait()
        self.play(circ.animate.shift(UP))
        self.wait()
        self.play(circ.animate.shift(LEFT))
        self.wait()
        self.play(circ.animate.shift(2 * RIGHT))
        self.wait()
        self.play(circ.animate.shift(LEFT))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.play(Create(axes))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.play(Write(sph))
        self.wait(2)
        self.play(sph.animate.set_z(1))
        self.wait(4)
        self.play(sph.animate.set_z(2), circ.animate.set_z(1))
        self.wait(4)
        self.play(circ.animate.set_z(0))
        self.wait(3)


class WAxis(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):
        # self.add(NumberPlane())
        # self.add_sound('Soft Inspirational Background Music for Videos & Presentation.mp3')

        axes = ThreeDAxes().set_color(BLACK)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.play(Create(axes))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Write(Line3D(start=np.array([-3, -3, -3]), end=np.array([3, 3, 3]))))
        self.wait(8)


def triangulate(n):
    """
    A program to calculate triangulations of a polygon.
    """
    if n == 3:
        return 1
    return (((4 * (n - 1)) - 6) / (n - 1)) * triangulate(n - 1)


print(triangulate(4))
