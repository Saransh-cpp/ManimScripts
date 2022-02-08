from manimlib.imports import *
class vid4(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project5a.m4a")
        image=ImageMobject("./road1.png")
        image.scale(5.6)
        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        car = ImageMobject("./car.png")
        car.move_to(1*DOWN+10*LEFT)
        car1 = ImageMobject("./car.png")
        car1.move_to(1*DOWN+3.5*LEFT)
        car2 = ImageMobject("./car.png")
        car2.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("Hi there!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome to the\\\\"
        "first episode\\\\",
        "of personal\\\\",
        "finance").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct1 = TextMobject("I would try my\\\\",
        "best to make it\\\\",
        "interesting and easy\\\\"
        "for you to understand").set_color(BLACK)
        tct1.move_to(3.5*LEFT+2.5*UP)
        tct1.scale(0.8)

        tct2 = TextMobject("So let's\\\\",
        "BEGIN!").set_color(BLACK)
        tct2.scale(2)
        tct2.move_to(3.5*LEFT+2.3*UP)


        thinker = ImageMobject("thinker.png")
        thinker.move_to(4*RIGHT)
        tc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        tc.next_to(thinker, UP, buff=0.1)


        t1 = TextMobject("Personal Finance"," is the financial management which an")
        t1[0].set_color(RED)
        t1[1].set_color(BLACK)
        t1.move_to(3.5*UP)

        ct1 = TextMobject("But what is\\\\",
        "personal\\\\" 
        "finance?").set_color(BLACK)
        ct1.scale(0.7)
        ct1.move_to(2.4*UP+4*RIGHT)

        indi = ImageMobject("./individual.png")
        group = ImageMobject("./group.png")
        indi.move_to(6*LEFT+1.5*UP)
        or1 = TextMobject("OR").set_color(BLACK)
        or1.scale(2)
        or1.move_to(4.3*LEFT+1.5*UP)
        group.move_to(2*LEFT+1.5*UP)

        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(group, RIGHT, buff=0.1)

        arrt = TextMobject("Performs to").set_color(BLACK)
        arrt.scale(0.5)
        arrt.next_to(arr1, UP, buff=0.01)

        arrt1 = TextMobject("Budget, Save and Spend\\\\",
        "Monetary resources over\\\\"
        "time").set_color(RED)
        arrt1.next_to(arr1, RIGHT, buff=0.1)

        t2 = TextMobject("In simple terms,\\\\",
        "personal finance ","is defined as")
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2.scale(1.5)
        t2.move_to(2.5*UP)

        m1 = ImageMobject("./money-bag.png")
        m1.scale(1.5)
        m1a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        m1a1.next_to(m1, RIGHT, buff=0.1)
        m1a1t = TextMobject("Management").set_color(RED)
        m1a1t.next_to(m1a1, RIGHT, buff=0.1)
        m1a2 = Arrow(RIGHT, LEFT).set_color(BLACK)
        m1a2.next_to(m1, LEFT, buff=0.1)
        m1a2t =TextMobject("Financial Decisions\\\\",
        "regarding it").set_color(RED)
        m1a2t.next_to(m1a2, LEFT, buff=0.1)

        t3 = TextMobject("Now let's come to, why\\\\"
        " is it ", "necessary?").scale(1.3)
        t3.move_to(3*UP)
        t3[0].set_color(BLACK)
        t3[1].set_color(RED)
        dot1 = Dot().set_color(BLACK)
        dot1.move_to(6*LEFT+3.5*DOWN)
        dot2 = Dot().set_color(BLACK)
        dot2.move_to(6*LEFT+2.5*UP)
        line1 = Line(dot1.get_top(), dot2.get_bottom(), buff=0.1).set_color(BLACK)

        t4 = TextMobject("Good ", "personal financing ", "helps you\\\\"
        "in the following ways-")
        t4.move_to(3*UP)
        t4[0].set_color(BLACK)
        t4[1].set_color(RED)
        t4[2].set_color(BLACK)

        pf1 = TextMobject("It keeps an eye on your financial goal").set_color(BLACK)
        pf2 = TextMobject("Retirement Planning").set_color(BLACK)
        pf3 = TextMobject("Budgeting").set_color(BLACK)
        pf4 = TextMobject("Savings").set_color(BLACK)
        pf5 = TextMobject("Financial independence").set_color(BLACK)
        pf6 = TextMobject("Manage your income").set_color(BLACK)
        pff = TextMobject("and so on").set_color(BLACK)

        pf1.move_to(2*UP+1.35*LEFT)
        pf2.move_to(UP+3.15*LEFT)
        pf3.move_to(4.3*LEFT)
        pf4.move_to(DOWN+4.6*LEFT)
        pf5.move_to(2*DOWN+2.95*LEFT)
        pf6.move_to(3*DOWN+3.2*LEFT)

        fgoal = ImageMobject("./fgoal.png").scale(1.5)
        retire = ImageMobject("./retirement.png")
        budget = ImageMobject("./budget.png").scale(1.5)
        saving = ImageMobject("./saving.png").scale(1.5)
        findep = ImageMobject("./findep.png")
        mincome = ImageMobject("./mincome.png").scale(1.5)

        wtf1 = TextMobject("Congratulations! You have taken the right decision\\\\",
        "by joining our course").set_color(BLACK)
        wtf1.move_to(2.75*UP)
        wtf2 = TextMobject("You must be wondering, what am I to\\\\",
        "benefit from this course?").set_color(BLACK)
        wtf2.move_to(2.75*UP)
        wtf3 = TextMobject("Well, by the end of the session, you will definitely\\\\",
        "realize that you did spend your time effectively by joining us").set_color(BLACK)
        wtf3.move_to(2.75*UP)



     








        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1))
        self.play(ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.play(FadeOut(thoughtcloud2text1), FadeOut(thoughtcloud2))
        self.play(Write(wtf1, run_time=4))
        self.play(FadeOut(wtf1))
        self.play(Write(wtf2, run_time=4))
        self.play(FadeOut(wtf2))
        self.play(Write(wtf3, run_time=4))
        self.play(FadeOut(wtf3))
        self.play(Write(tct1))
        self.wait()
        self.play(ReplacementTransform(tct1, tct2))
        self.play(FadeOut(thoughtcloud2), FadeOut(tct2), ReplacementTransform(car1, car2))
        self.play(FadeOut(trees))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(ct1))
        self.play(Write(t1))
        self.play(FadeOut(tc), FadeOut(ct1))
        self.play(GrowFromCenter(indi))
        self.play(Write(or1))
        self.play(GrowFromCenter(group))
        self.play(GrowArrow(arr1))
        self.play(Write(arrt))
        self.play(FadeOut(thinker))
        self.play(Write(arrt1))
        self.play(FadeOut(t1))
        self.play(FadeOut(arrt), FadeOut(indi), FadeOut(group), FadeOut(or1), FadeOut(arr1), FadeOut(arrt1))
        self.play(Write(t2))
        self.play(FadeInFromDown(m1))
        self.play(GrowArrow(m1a1), GrowArrow(m1a2))
        self.play(Write(m1a1t), Write(m1a2t))
        self.play(FadeOut(m1), FadeOut(m1a1), FadeOut(m1a2), FadeOut(m1a1t)
        , FadeOut(m1a2t), FadeOut(image), FadeOut(t2))
        self.play(Write(t3))
        self.play(FadeOut(t3))
        self.play(Write(t4))
        self.play(Write(dot1))
        self.play(ShowCreation(line1))
        self.play(Write(dot2))
        
        

        self.play(Write(pf1))
        self.play(GrowFromCenter(fgoal))
        self.play(FadeOut(pf1))
        self.play(FadeOut(fgoal))
        self.play(Write(pf2))
        self.play(GrowFromCenter(retire))
        self.play(FadeOut(pf2))
        self.play(FadeOut(retire))
        self.play(Write(pf3))
        self.play(GrowFromCenter(budget))
        self.play(FadeOut(pf3))
        self.play(FadeOut(budget))
        self.play(Write(pf4))
        self.play(GrowFromCenter(saving))
        self.play(FadeOut(pf4))
        self.play(FadeOut(saving))
        self.play(Write(pf5))
        self.play(GrowFromCenter(findep))
        self.play(FadeOut(pf5))
        self.play(FadeOut(findep))
        self.play(Write(pf6))
        self.play(GrowFromCenter(mincome))
        self.play(FadeOut(pf6))
        self.play(FadeOut(mincome))
        self.play(Write(pf1), Write(pf2), Write(pf3), Write(pf4)
        , Write(pf5), Write(pf6))
        self.play(FadeOut(pf1), FadeOut(pf2), FadeOut(pf3), FadeOut(pf4), FadeOut(pf5),
        FadeOut(pf6), FadeOut(dot1), FadeOut(dot2), FadeOut(line1), FadeOut(t4))

        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)

        gt1 = TextMobject("So, till now you know that").set_color(BLACK)
        gt1.move_to(3.5*UP+3*RIGHT)
        pft = TextMobject("Personal Finance").set_color(RED)
        pft.move_to(2*UP)
        pfarr = Arrow(LEFT, RIGHT).set_color(BLACK)
        pfarr.next_to(pft, RIGHT, buff=0.1)
        pfarrt = TextMobject("Important and\\\\",
        "necessary").set_color(BLACK)
        pfarrt.next_to(pfarr, RIGHT, buff=0.1)
        gt2 = TextMobject("And one should start planning\\\\",
        "in his/her initial age").set_color(BLACK)
        gt2.move_to(3*RIGHT)

        hman = ImageMobject("./hman.png")
        hman.move_to(3*RIGHT+2*DOWN)

        hmanc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        hmanc.scale(1.8)
        hmanc.next_to(hman, UP, buff=0.1)

        hmanct1 = TextMobject("So let's talk about\\\\",
        "how to implement\\\\"
        "all these and \\\\",
        "get yoursef a\\\\",
        "perfect plan later\\\\").set_color(BLACK)
        hmanct1.scale(0.75)
        hmanct1.move_to(3*RIGHT+1.3*UP)

        hmanct2 = TextMobject("First understand\\\\",
        "the importance\\\\",
        "of saving money").set_color(BLACK)
        hmanct2.scale(0.85)
        hmanct2.move_to(3*RIGHT+1.3*UP)

        gt3 = TextMobject("After hearing about savings you all\\\\",
        "would be thinking, huh I have hear this").set_color(BLACK)
        gt3.move_to(3*UP+2.5*RIGHT)

        mil = TextMobject("A Million Times!").set_color(RED)
        mil.scale(1.5)
        mil.move_to(1.7*UP+2.5*RIGHT)

        gt4 = TextMobject("So, yes there is a logic behind\\\\",
        "it an I'll tell you the logic that\\\\",
        "why you should save money!").set_color(BLACK)
        gt4.move_to(2.5*RIGHT)









        self.play(FadeInFromDown(gard))
        self.play(Write(gt1))
        self.play(Write(pft))
        self.play(GrowArrow(pfarr))
        self.play(Write(pfarrt))
        self.play(Write(gt2))
        self.wait()
        self.play(FadeInFromDown(hman))
        self.play(FadeOut(gt1), FadeOut(gt2), FadeOut(pft), FadeOut(pfarr), FadeOut(pfarrt))
        self.play(Write(hmanc))
        self.play(Write(hmanct1, run_time=3))
        self.play(FadeOut(hmanct1))
        self.play(Write(hmanct2))
        self.play(FadeOut(hmanct2), FadeOut(hmanc))
        self.play(Write(gt3))
        self.play(Write(mil))
        self.play(Write(gt4, run_time=2))
        self.play(FadeOut(gt3), FadeOut(gt4), FadeOut(mil), FadeOut(hman))

        et1 = TextMobject("For example -").set_color(BLACK)
        et1.move_to(5*LEFT+3*UP)

        kids = ImageMobject("./kids.png").scale(1.5)
        kids.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        rt1 = TextMobject("speedthrift").set_color(BLACK)
        st1 = TextMobject("Concerned regarding\\\\",
        "his personal finance").set_color(BLACK)
        rt1.next_to(exarr, UP, buff=0.1)
        st1.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("18").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 25 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)

        paisa1 = TextMobject("0").set_color(RED)
        paisa2 = TextMobject("0").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(500)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("6,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("7(6,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("42,000").set_color(RED)
        paisa6b = TextMobject("80,000").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)

        text = TextMobject("Now you all will be assuming that the numbers\\\\",
        "are not that great so let's take another example").set_color(BLACK)
        text.move_to(3*UP)
        



        self.add(gard)
        self.play(Write(et1))
        self.play(FadeInFromDown(kids))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2), FadeOut(et1))
        self.play(GrowArrow(exarr), FadeIn(rt1))
        self.play(FadeOut(exarr), FadeOut(rt1))
        self.play(GrowArrow(exarr1), FadeIn(st1))
        self.play(FadeOut(exarr1), FadeOut(st1))

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))

        self.play(FadeOut(paisa1), FadeOut(paisa2), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), 
        FadeOut(monname), FadeOut(monname1), FadeOut(f1), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1))
        self.play(Write(text, run_time=2))
        self.play(FadeOut(text)) 

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("23").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 34 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)
        montext4 = TextMobject("At the age of"," 60")
        montext4[0].set_color(BLACK)
        montext4[1].set_color(RED)
        montext4.move_to(0.5*DOWN+1.1*LEFT)
        montext4arr1 = Arrow(LEFT,RIGHT)
        montext4arr1.scale(0.5).set_color(BLACK)
        montext4arr1.next_to(montext4, RIGHT, buff=0.1)

        paisa1 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa2 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(5000)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("60,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("10(60,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("6 Lakh").set_color(RED)
        paisa6b = TextMobject("6L+14L").set_color(RED)
        paisa7 = TextMobject("0").set_color(RED)
        paisa8 = TextMobject("5 Crore").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)
        paisa1a = TextMobject("0").set_color(RED)
        paisa2a = TextMobject("0").set_color(RED)
        paisa1a.move_to(3*RIGHT+2.5*UP)
        paisa2a.move_to(5.5*RIGHT+2.5*UP)
        paisa7.move_to(3*RIGHT+0.5*DOWN)
        paisa8.move_to(5.5*RIGHT+0.5*DOWN)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)
        f2 = SurroundingRectangle(paisa8, buff=0.1).set_color(BLACK)

        tb = TextMobject("Decided to chill on first year").set_color(BLACK)
        
        tf1 = TextMobject("Seems interesting?").set_color(RED)
        tf1.scale(2)
        tf2 = TextMobject("IT IS!!!!!!!!").set_color(RED)
        tf2.scale(2)




        self.add(gard)
        self.play(FadeInFromDown(kids))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.play(Write(tb))
        self.play(ReplacementTransform(paisa1, paisa1a))
        self.play(ReplacementTransform(paisa2, paisa2a))
        self.play(FadeOut(tb))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))
        self.play(Write(montext4))
        self.play(GrowArrow(montext4arr1))
        self.play(Write(paisa7))
        self.play(Write(paisa8))
        self.wait()
        self.play(ReplacementTransform(f1, f2))
        self.wait()
        self.play(FadeOut(paisa1a), FadeOut(paisa2a), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), FadeOut(paisa7), FadeOut(paisa8),
        FadeOut(monname), FadeOut(monname1), FadeOut(f2), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1), FadeOut(montext4),  FadeOut(montext4arr1))
        self.play(GrowFromCenter(tf1))
        self.play(FadeOut(tf1))
        self.play(GrowFromCenter(tf2))
        self.play(FadeOut(tf2))
        self.play(FadeOut(gard), FadeIn(image), FadeInFromDown(trees))

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" So this was one\\\\"
        "simple reason that\\\\",
        "why you guys need\\\\",
        "to save money").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.4*UP)

        tcfy = TextMobject("Now on the next\\\\",
        "episode, we will be\\\\",
        "talking about the\\\\",
        "strategies to\\\\"
        "save money").set_color(BLACK)
        tcfy.scale(0.75)
        tcfy.move_to(3.5*LEFT+2.4*UP)

        lastf = TextMobject("Thank\\\\",
        "YOU!").set_color(BLACK)
        lastf.move_to(3.5*LEFT+2.4*UP).scale(2)



        
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.wait()
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tcfy, run_time=3))
        self.wait()
        self.play(FadeOut(tcfy))
        self.play(Write(lastf))
        self.wait()
        self.play(FadeOut(thoughtcloud2), FadeOut(lastf), ReplacementTransform(car1a, car2a))
        self.play(FadeOut(trees))
        self.play(FadeOut(image))








        self.wait()
        self.add(g)

class vid41(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("./project5a.m4a")
        self.wait(96)

        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)

        gt1 = TextMobject("So, till now you know that").set_color(BLACK)
        gt1.move_to(3.5*UP+3*RIGHT)
        pft = TextMobject("Personal Finance").set_color(RED)
        pft.move_to(2*UP)
        pfarr = Arrow(LEFT, RIGHT).set_color(BLACK)
        pfarr.next_to(pft, RIGHT, buff=0.1)
        pfarrt = TextMobject("Important and\\\\",
        "necessary").set_color(BLACK)
        pfarrt.next_to(pfarr, RIGHT, buff=0.1)
        gt2 = TextMobject("And one should start planning\\\\",
        "in his/her initial age").set_color(BLACK)
        gt2.move_to(3*RIGHT)

        hman = ImageMobject("./hman.png")
        hman.move_to(3*RIGHT+2*DOWN)

        hmanc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        hmanc.scale(1.8)
        hmanc.next_to(hman, UP, buff=0.1)

        hmanct1 = TextMobject("So let's talk about\\\\",
        "how to implement\\\\"
        "all these and \\\\",
        "get yoursef a\\\\",
        "perfect plan later\\\\").set_color(BLACK)
        hmanct1.scale(0.75)
        hmanct1.move_to(3*RIGHT+1.3*UP)

        hmanct2 = TextMobject("First understand\\\\",
        "the importance\\\\",
        "of saving money").set_color(BLACK)
        hmanct2.scale(0.85)
        hmanct2.move_to(3*RIGHT+1.3*UP)

        gt3 = TextMobject("After hearing about savings you all\\\\",
        "would be thinking, huh I have hear this").set_color(BLACK)
        gt3.move_to(3*UP+2.5*RIGHT)

        mil = TextMobject("A Million Times!").set_color(RED)
        mil.scale(1.5)
        mil.move_to(1.7*UP+2.5*RIGHT)

        gt4 = TextMobject("So, yes there is a logic behind\\\\",
        "it an I'll tell you the logic that\\\\",
        "why you should save money!").set_color(BLACK)
        gt4.move_to(2.5*RIGHT)









        self.play(FadeInFromDown(gard))
        self.play(Write(gt1, run_time=4))
        self.play(Write(pft))
        self.play(GrowArrow(pfarr))
        self.play(Write(pfarrt))
        self.play(Write(gt2))
        self.play(FadeInFromDown(hman), FadeOut(gt1), FadeOut(gt2), FadeOut(pft), FadeOut(pfarr), FadeOut(pfarrt), Write(hmanc))
        self.play(Write(hmanct1, run_time=4))
        self.play(FadeOut(hmanct1))
        self.play(Write(hmanct2, run_time=3))
        self.play(FadeOut(hmanct2), FadeOut(hmanc))
        self.wait(2)
        self.play(Write(gt3, run_time=4.5))
        self.wait()
        self.play(Write(mil, run_time=1.5))
        self.wait(3.5)
        self.play(Write(gt4, run_time=6))
        self.play(FadeOut(gt3), FadeOut(gt4), FadeOut(mil), FadeOut(hman))






        self.wait()
        self.add(g)

class vid42(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("./project5a.m4a")
        self.wait(138)

        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)

        et1 = TextMobject("For example -").set_color(BLACK)
        et1.move_to(5*LEFT+3*UP)

        kids = ImageMobject("./kids.png").scale(1.5)
        kids.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        rt1 = TextMobject("speedthrift").set_color(BLACK)
        st1 = TextMobject("Concerned regarding\\\\",
        "his personal finance").set_color(BLACK)
        rt1.next_to(exarr, UP, buff=0.1)
        st1.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("18").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 25 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)

        paisa1 = TextMobject("0").set_color(RED)
        paisa2 = TextMobject("0").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(500)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("6,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("7(6,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("42,000").set_color(RED)
        paisa6b = TextMobject("80,000").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)

        text = TextMobject("Now you all will be assuming that the numbers\\\\",
        "are not that great so let's take another example").set_color(BLACK)
        text.move_to(3*UP)
        



        self.add(gard)
        self.play(Write(et1, run_time=3))
        self.play(FadeInFromDown(kids))
        self.wait()
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2), FadeOut(et1))
        self.play(GrowArrow(exarr), FadeIn(rt1))
        self.play(FadeOut(exarr), FadeOut(rt1))
        self.wait(4)
        self.play(GrowArrow(exarr1), FadeIn(st1))
        self.wait(2)
        self.play(FadeOut(exarr1), FadeOut(st1))
        self.wait(2)

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.wait(4)
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.wait(4)
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))
        self.wait(6)

        self.play(FadeOut(paisa1), FadeOut(paisa2), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), 
        FadeOut(monname), FadeOut(monname1), FadeOut(f1), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1))
        self.play(Write(text, run_time=7))
        self.play(FadeOut(text))




        self.wait()
        self.add(g)

class vid43(Scene):

    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("./project5a.m4a")
        self.wait(207)
        kids = ImageMobject("./kids.png").scale(1.5)
        kids.move_to(2*RIGHT+2*DOWN)

        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("23").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 34 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)
        montext4 = TextMobject("At the age of"," 60")
        montext4[0].set_color(BLACK)
        montext4[1].set_color(RED)
        montext4.move_to(0.5*DOWN+1.1*LEFT)
        montext4arr1 = Arrow(LEFT,RIGHT)
        montext4arr1.scale(0.5).set_color(BLACK)
        montext4arr1.next_to(montext4, RIGHT, buff=0.1)

        paisa1 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa2 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(5000)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("60,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("10(60,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("6 Lakh").set_color(RED)
        paisa6b = TextMobject("6L+14L").set_color(RED)
        paisa7 = TextMobject("0").set_color(RED)
        paisa8 = TextMobject("5 Crore").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)
        paisa1a = TextMobject("0").set_color(RED)
        paisa2a = TextMobject("0").set_color(RED)
        paisa1a.move_to(3*RIGHT+2.5*UP)
        paisa2a.move_to(5.5*RIGHT+2.5*UP)
        paisa7.move_to(3*RIGHT+0.5*DOWN)
        paisa8.move_to(5.5*RIGHT+0.5*DOWN)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)
        f2 = SurroundingRectangle(paisa8, buff=0.1).set_color(BLACK)

        tb = TextMobject("Decided to chill on first year").set_color(BLACK)
        
        tf1 = TextMobject("Seems interesting?").set_color(RED)
        tf1.scale(2)
        tf2 = TextMobject("IT IS!!!!!!!!").set_color(RED)
        tf2.scale(2)




        self.add(gard)
        self.play(FadeInFromDown(kids))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.wait(3)
        self.play(Write(tb))
        self.wait(2)
        self.play(ReplacementTransform(paisa1, paisa1a))
        self.play(ReplacementTransform(paisa2, paisa2a))
        self.play(FadeOut(tb))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.wait(5)
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.wait(2)
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.wait(8)
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.wait(3)
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.wait(10)
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))
        self.wait(2)
        self.play(Write(montext4))
        self.play(GrowArrow(montext4arr1))
        self.wait(2)
        self.play(Write(paisa7))
        self.play(Write(paisa8))
        self.wait()
        self.play(ReplacementTransform(f1, f2))
        self.wait()
        self.play(FadeOut(paisa1a), FadeOut(paisa2a), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), FadeOut(paisa7), FadeOut(paisa8),
        FadeOut(monname), FadeOut(monname1), FadeOut(f2), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1), FadeOut(montext4),  FadeOut(montext4arr1))
        self.play(GrowFromCenter(tf1))
        self.play(FadeOut(tf1))
        self.play(GrowFromCenter(tf2))
        self.play(FadeOut(tf2))
        self.play(FadeOut(gard))

class vid44(Scene):

    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        
        self.add_sound("./project5a.m4a")
        self.wait(289)
        image=ImageMobject("./road1.png")
        image.scale(5.6)
        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" So this was one\\\\"
        "simple reason that\\\\",
        "why you guys need\\\\",
        "to save money").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.4*UP)

        tcfy = TextMobject("Now on the next\\\\",
        "episode, we will be\\\\",
        "talking about the\\\\",
        "strategies to\\\\"
        "save money").set_color(BLACK)
        tcfy.scale(0.75)
        tcfy.move_to(3.5*LEFT+2.4*UP)

        lastf = TextMobject("Thank\\\\",
        "YOU!").set_color(BLACK)
        lastf.move_to(3.5*LEFT+2.4*UP).scale(2)



        self.FadeIn((image))
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a), Write(thoughtcloud2))
        self.play(Write(thoughtcloud2text1, run_time=3))
        self.wait()
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tcfy, run_time=5))
        self.wait()
        self.play(FadeOut(tcfy))
        self.wait(3)
        self.play(Write(lastf))
        self.wait(3)
        self.play(FadeOut(thoughtcloud2), FadeOut(lastf), ReplacementTransform(car1a, car2a))
        


class vid45(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project5a.m4a")
        image=ImageMobject("./road1.png")
        image.scale(5.6)
        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        car = ImageMobject("./car.png")
        car.move_to(1*DOWN+10*LEFT)
        car1 = ImageMobject("./car.png")
        car1.move_to(1*DOWN+3.5*LEFT)
        car2 = ImageMobject("./car.png")
        car2.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("Hi there!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome to the\\\\"
        "first episode\\\\",
        "of personal\\\\",
        "finance").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct1 = TextMobject("I will try my\\\\",
        "best to make it\\\\",
        "interesting and easy\\\\"
        "for you to understand").set_color(BLACK)
        tct1.move_to(3.5*LEFT+2.5*UP)
        tct1.scale(0.8)

        tct2 = TextMobject("So let's\\\\",
        "BEGIN!").set_color(BLACK)
        tct2.scale(2)
        tct2.move_to(3.5*LEFT+2.3*UP)


        thinker = ImageMobject("thinker.png")
        thinker.move_to(4*RIGHT)
        tc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        tc.next_to(thinker, UP, buff=0.1)


        t1 = TextMobject("Personal Finance"," is the financial management which an")
        t1[0].set_color(RED)
        t1[1].set_color(BLACK)
        t1.move_to(3.5*UP)

        ct1 = TextMobject("But what is\\\\",
        "personal\\\\" 
        "finance?").set_color(BLACK)
        ct1.scale(0.7)
        ct1.move_to(2.4*UP+4*RIGHT)

        indi = ImageMobject("./individual.png")
        group = ImageMobject("./group.png")
        indi.move_to(6*LEFT+1.5*UP)
        or1 = TextMobject("OR").set_color(BLACK)
        or1.scale(2)
        or1.move_to(4.3*LEFT+1.5*UP)
        group.move_to(2*LEFT+1.5*UP)

        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(group, RIGHT, buff=0.1)

        arrt = TextMobject("Performs to").set_color(BLACK)
        arrt.scale(0.5)
        arrt.next_to(arr1, UP, buff=0.01)

        arrt1 = TextMobject("Budget, Save and Spend\\\\",
        "Monetary resources over\\\\"
        "time").set_color(RED)
        arrt1.next_to(arr1, RIGHT, buff=0.1)

        t2 = TextMobject("In simple terms,\\\\",
        "personal finance ","is defined as")
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2.scale(1.5)
        t2.move_to(2.5*UP)

        m1 = ImageMobject("./money-bag.png")
        m1.scale(1.5)
        m1a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        m1a1.next_to(m1, RIGHT, buff=0.1)
        m1a1t = TextMobject("Management").set_color(RED)
        m1a1t.next_to(m1a1, RIGHT, buff=0.1)
        m1a2 = Arrow(RIGHT, LEFT).set_color(BLACK)
        m1a2.next_to(m1, LEFT, buff=0.1)
        m1a2t =TextMobject("Financial Decisions\\\\",
        "regarding it").set_color(RED)
        m1a2t.next_to(m1a2, LEFT, buff=0.1)

        t3 = TextMobject("Now let's come to, why\\\\"
        " is it ", "necessary?").scale(1.3)
        t3.move_to(3*UP)
        t3[0].set_color(BLACK)
        t3[1].set_color(RED)
        dot1 = Dot().set_color(BLACK)
        dot1.move_to(6*LEFT+3.5*DOWN)
        dot2 = Dot().set_color(BLACK)
        dot2.move_to(6*LEFT+2.5*UP)
        line1 = Line(dot1.get_top(), dot2.get_bottom(), buff=0.1).set_color(BLACK)

        t4 = TextMobject("Good ", "personal financing ", "helps you\\\\"
        "in the following ways-")
        t4.move_to(3*UP)
        t4[0].set_color(BLACK)
        t4[1].set_color(RED)
        t4[2].set_color(BLACK)

        pf1 = TextMobject("It keeps an eye on your financial goal").set_color(BLACK)
        pf2 = TextMobject("Retirement Planning").set_color(BLACK)
        pf3 = TextMobject("Budgeting").set_color(BLACK)
        pf4 = TextMobject("Savings").set_color(BLACK)
        pf5 = TextMobject("Financial independence").set_color(BLACK)
        pf6 = TextMobject("Manage your income").set_color(BLACK)
        pff = TextMobject("and so on").set_color(BLACK)

        pf1.move_to(2*UP+1.35*LEFT)
        pf2.move_to(UP+3.15*LEFT)
        pf3.move_to(4.3*LEFT)
        pf4.move_to(DOWN+4.6*LEFT)
        pf5.move_to(2*DOWN+2.95*LEFT)
        pf6.move_to(3*DOWN+3.2*LEFT)

        fgoal = ImageMobject("./fgoal.png").scale(1.5)
        retire = ImageMobject("./retirement.png")
        budget = ImageMobject("./budget.png").scale(1.5)
        saving = ImageMobject("./saving.png").scale(1.5)
        findep = ImageMobject("./findep.png")
        mincome = ImageMobject("./mincome.png").scale(1.5)

        wtf1 = TextMobject("Congratulations! You have taken the right decision\\\\",
        "by joining our course").set_color(BLACK)
        wtf1.move_to(2.75*UP)
        wtf2 = TextMobject("You must be wondering, what am I to\\\\",
        "benefit from this course?").set_color(BLACK)
        wtf2.move_to(2.75*UP)
        wtf3 = TextMobject("Well, by the end of the session, you will definitely\\\\",
        "realize that you did spend your time effectively by joining us").set_color(BLACK)
        wtf3.move_to(2.75*UP)



     








        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1, run_time=2))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1))
        self.play(ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.play(FadeOut(thoughtcloud2text1), FadeOut(thoughtcloud2))
        self.play(Write(wtf1, run_time=5))
        self.play(FadeOut(wtf1))
        self.play(Write(wtf2, run_time=5))
        self.play(FadeOut(wtf2))
        self.play(Write(wtf3, run_time=6))
        self.play(FadeOut(wtf3))
        self.play(Write(thoughtcloud2))
        self.play(Write(tct1))
        self.wait(2)
        self.play(ReplacementTransform(tct1, tct2))
        self.wait()
        self.play(FadeOut(thoughtcloud2), FadeOut(tct2), ReplacementTransform(car1, car2))
        self.play(FadeOut(trees))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(ct1))
        self.play(Write(t1))
        self.play(FadeOut(tc), FadeOut(ct1))
        self.play(GrowFromCenter(indi))
        self.play(Write(or1))
        self.play(GrowFromCenter(group))
        self.play(GrowArrow(arr1))
        self.play(Write(arrt))
        self.play(FadeOut(thinker))
        self.play(Write(arrt1))
        self.play(FadeOut(t1))
        self.wait(4)
        self.play(FadeOut(arrt), FadeOut(indi), FadeOut(group), FadeOut(or1), FadeOut(arr1), FadeOut(arrt1))
        self.play(Write(t2, run_time=1.5))
        self.play(FadeInFromDown(m1))
        self.play(GrowArrow(m1a1), GrowArrow(m1a2))
        self.play(Write(m1a1t), Write(m1a2t))
        self.wait(4)
        self.play(FadeOut(m1), FadeOut(m1a1), FadeOut(m1a2), FadeOut(m1a1t)
        , FadeOut(m1a2t), FadeOut(image), FadeOut(t2))
        self.play(Write(t3, run_time=1.5))
        self.play(FadeOut(t3))
        self.play(Write(t4, run_time=3))
        self.play(Write(dot1))
        self.play(ShowCreation(line1))
        self.play(Write(dot2))
        
        

        self.play(Write(pf1))
        self.play(GrowFromCenter(fgoal))
        self.play(FadeOut(pf1))
        self.play(FadeOut(fgoal))
        self.play(Write(pf2), GrowFromCenter(retire))
        self.play(FadeOut(pf2), FadeOut(retire))
        self.play(Write(pf3), GrowFromCenter(budget))
        self.play(FadeOut(pf3), FadeOut(budget))
        self.play(Write(pf4), GrowFromCenter(saving))
        self.play(FadeOut(pf4), FadeOut(saving))
        self.play(Write(pf5), GrowFromCenter(findep))
        self.play(FadeOut(pf5), FadeOut(findep))
        self.play(Write(pf6), GrowFromCenter(mincome))
        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)
        self.play(FadeOut(t4), FadeOut(pf6), FadeOut(mincome), FadeInFromDown(gard))


        

        gt1 = TextMobject("So, far you know that").set_color(BLACK)
        gt1.move_to(3.5*UP+3*RIGHT)
        pft = TextMobject("Personal Finance").set_color(RED)
        pft.move_to(2*UP)
        pfarr = Arrow(LEFT, RIGHT).set_color(BLACK)
        pfarr.next_to(pft, RIGHT, buff=0.1)
        pfarrt = TextMobject("Important and\\\\",
        "necessary").set_color(BLACK)
        pfarrt.next_to(pfarr, RIGHT, buff=0.1)
        gt2 = TextMobject("And one should start planning\\\\",
        "as early as possible").set_color(BLACK)
        gt2.move_to(3*RIGHT)

        hman = ImageMobject("./hman.png")
        hman.move_to(3*RIGHT+2*DOWN)

        hmanc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        hmanc.scale(1.8)
        hmanc.next_to(hman, UP, buff=0.1)

        hmanct1 = TextMobject("So let's talk about\\\\",
        "how to implement\\\\"
        "all these and \\\\",
        "get yoursef a\\\\",
        "perfect plan later\\\\").set_color(BLACK)
        hmanct1.scale(0.75)
        hmanct1.move_to(3*RIGHT+1.3*UP)

        hmanct2 = TextMobject("First understand\\\\",
        "the importance\\\\",
        "of saving money").set_color(BLACK)
        hmanct2.scale(0.85)
        hmanct2.move_to(3*RIGHT+1.3*UP)

        gt3 = TextMobject("After hearing about savings you\\\\",
        "would be thinking, huh I have heard this").set_color(BLACK)
        gt3.move_to(3*UP+2.5*RIGHT)

        mil = TextMobject("A Million Times!").set_color(RED)
        mil.scale(1.5)
        mil.move_to(1.7*UP+2.5*RIGHT)

        gt4 = TextMobject("So, yes there is a logic behind\\\\",
        "it and I'll tell you the logic of\\\\",
        "why you should save!").set_color(BLACK)
        gt4.move_to(2.5*RIGHT)









        self.wait(2)
        self.play(Write(gt1, run_time=4))
        self.play(Write(pft))
        self.play(GrowArrow(pfarr))
        self.play(Write(pfarrt))
        self.play(Write(gt2))
        self.play(FadeInFromDown(hman), FadeOut(gt1), FadeOut(gt2), FadeOut(pft), FadeOut(pfarr), FadeOut(pfarrt), Write(hmanc))
        self.play(Write(hmanct1, run_time=4))
        self.play(FadeOut(hmanct1))
        self.play(Write(hmanct2, run_time=3))
        self.play(FadeOut(hmanct2), FadeOut(hmanc))
        self.wait(2)
        self.play(Write(gt3, run_time=4.5))
        self.wait()
        self.play(Write(mil, run_time=1.5))
        self.wait(3.5)
        self.play(Write(gt4, run_time=6))
        gard = ImageMobject("./scene1.png").scale(8)
        gard.move_to(4*UP)
        self.play(FadeOut(gt3), FadeOut(gt4), FadeOut(mil), FadeOut(hman), FadeIn(gard))
        



        

        et1 = TextMobject("For example -").set_color(BLACK)
        et1.move_to(5*LEFT+3*UP)

        kids = ImageMobject("./kids.png").scale(1.5)
        kids.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        rt1 = TextMobject("spendthrift").set_color(BLACK)
        st1 = TextMobject("Concerned regarding\\\\",
        "his personal finance").set_color(BLACK)
        rt1.next_to(exarr, UP, buff=0.1)
        st1.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("18").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 25 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)

        paisa1 = TextMobject("0").set_color(RED)
        paisa2 = TextMobject("0").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(500)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("6,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("7(6,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("42,000").set_color(RED)
        paisa6b = TextMobject("80,000").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)

        text = TextMobject("You  will be assuming that the numbers\\\\",
        "are not that great so let's take another example").set_color(BLACK)
        text.move_to(3*UP)
        



       
        self.play(Write(et1, run_time=3))
        self.play(FadeInFromDown(kids))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2), FadeOut(et1))
        self.play(GrowArrow(exarr), FadeIn(rt1))
        self.play(FadeOut(exarr), FadeOut(rt1))
        self.wait(4)
        self.play(GrowArrow(exarr1), FadeIn(st1))
        self.wait(2)
        self.play(FadeOut(exarr1), FadeOut(st1))
        self.wait(2)

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.wait(4)
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.wait(4)
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))
        self.wait(6)

        self.play(FadeOut(paisa1), FadeOut(paisa2), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), 
        FadeOut(monname), FadeOut(monname1), FadeOut(f1), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1))
        self.play(Write(text, run_time=7))
        self.play(FadeOut(text))



        kids.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.7*RIGHT)
        exarr1.move_to(2.3*RIGHT)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        montext1 = TextMobject("Present age").set_color(BLACK)
        montext1a = TextMobject("23").set_color(RED)
        montext1.move_to(2.5*UP+2*LEFT)
        montext1arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr1.scale(0.5)
        montext1arr1.next_to(montext1, RIGHT, buff=0.1)
        montext1a.next_to(montext1arr1, RIGHT, buff=0.1)
        montext1arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        montext1arr2.scale(0.5)
        montext1arr2.next_to(montext1a, RIGHT, buff=0.1)
        monname = TextMobject("Ram").set_color(BLACK)
        monname1 = TextMobject("Shyam").set_color(BLACK)
        monname.move_to(3*RIGHT+3.5*UP)
        monname1.move_to(5.5*RIGHT+3.5*UP)
        montext2 = TextMobject("Shyam saves").set_color(BLACK)
        montext2a = TextMobject("1 year").set_color(RED)
        montext2.move_to(1.5*UP+3*LEFT)
        montext2arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr1.scale(0.5)
        montext2arr1.next_to(montext2, RIGHT, buff=0.1)
        montext2a.next_to(montext2arr1, RIGHT, buff=0.1)
        montext2arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext2arr2.scale(0.5)
        montext2arr2.next_to(montext2a, RIGHT, buff=0.1)
        montext3 = TextMobject("At"," 34 ","years")
        montext3[0].set_color(BLACK)
        montext3[1].set_color(RED)
        montext3[2].set_color(BLACK)
        montext3.move_to(0.5*UP+0.7*LEFT)
        montext3arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        montext3arr1.scale(0.5)
        montext3arr1.next_to(montext3, RIGHT, buff=0.1)
        montext4 = TextMobject("At the age of"," 60")
        montext4[0].set_color(BLACK)
        montext4[1].set_color(RED)
        montext4.move_to(0.5*DOWN+1.1*LEFT)
        montext4arr1 = Arrow(LEFT,RIGHT)
        montext4arr1.scale(0.5).set_color(BLACK)
        montext4arr1.next_to(montext4, RIGHT, buff=0.1)

        paisa1 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa2 = TextMobject("30,000\\\\", "p.m.").set_color(RED)
        paisa3 = TextMobject("0").set_color(RED)
        paisa4 = TextMobject("12(5000)").set_color(RED)
        paisa3a = TextMobject("0").set_color(RED)
        paisa4a = TextMobject("60,000").set_color(RED)
        paisa5 = TextMobject("0").set_color(RED)
        paisa6 = TextMobject("10(60,000)").set_color(RED)
        paisa5a = TextMobject("0").set_color(RED)
        paisa6a = TextMobject("6 Lakh").set_color(RED)
        paisa6b = TextMobject("6L+14L").set_color(RED)
        paisa7 = TextMobject("0").set_color(RED)
        paisa8 = TextMobject("5 Crore").set_color(RED)
        paisa1.move_to(3*RIGHT+2.5*UP)
        paisa2.move_to(5.5*RIGHT+2.5*UP)
        paisa3.move_to(3*RIGHT+1.5*UP)
        paisa4.move_to(5.5*RIGHT+1.5*UP)
        paisa5.move_to(3*RIGHT+0.5*UP)
        paisa6.move_to(5.5*RIGHT+0.5*UP)
        paisa4a.move_to(5.5*RIGHT+1.5*UP)
        paisa3a.move_to(3*RIGHT+1.5*UP)
        paisa5a.move_to(3*RIGHT+0.5*UP)
        paisa6a.move_to(5.5*RIGHT+0.5*UP)
        paisa6b.move_to(5.5*RIGHT+0.5*UP)
        paisa1a = TextMobject("0").set_color(RED)
        paisa2a = TextMobject("0").set_color(RED)
        paisa1a.move_to(3*RIGHT+2.5*UP)
        paisa2a.move_to(5.5*RIGHT+2.5*UP)
        paisa7.move_to(3*RIGHT+0.5*DOWN)
        paisa8.move_to(5.5*RIGHT+0.5*DOWN)

        f1 = SurroundingRectangle(paisa6b, buff=0.1).set_color(BLACK)
        f1text = TextMobject("Because of investment").set_color(BLACK)
        f1text.scale(0.5)
        f1text.next_to(f1, DOWN, buff=0.1)
        f2 = SurroundingRectangle(paisa8, buff=0.1).set_color(BLACK)

        tb = TextMobject("Decided to chill on first year").set_color(BLACK)
        
        tf1 = TextMobject("Seems interesting?").set_color(RED)
        tf1.scale(2)
        tf2 = TextMobject("IT IS!!!!!!!!").set_color(RED)
        tf2.scale(2)




        
        self.play(FadeInFromDown(kids))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))

        self.play(Write(monname))
        self.play(Write(monname1))
        self.play(Write(montext1))
        self.play(GrowArrow(montext1arr1))
        self.play(Write(montext1a))
        self.play(GrowArrow(montext1arr2))
        self.play(Write(paisa1))
        self.play(Write(paisa2))
        self.wait(3)
        self.play(Write(tb))
        self.wait(2)
        self.play(ReplacementTransform(paisa1, paisa1a))
        self.play(ReplacementTransform(paisa2, paisa2a))
        self.play(FadeOut(tb))
        self.wait()
        self.play(Write(montext2))
        self.play(GrowArrow(montext2arr1))
        self.play(Write(montext2a))
        self.play(GrowArrow(montext2arr2))
        self.wait(5)
        self.play(Write(paisa3))
        self.play(Write(paisa4))
        self.wait(2)
        self.play(ReplacementTransform(paisa3, paisa3a))
        self.play(ReplacementTransform(paisa4, paisa4a))
        self.wait(8)
        self.play(Write(montext3))
        self.play(GrowArrow(montext3arr1))
        self.play(Write(paisa5))
        self.wait(3)
        self.play(Write(paisa6))
        self.play(ReplacementTransform(paisa5, paisa5a))
        self.play(ReplacementTransform(paisa6, paisa6a))
        self.wait(10)
        self.play(ReplacementTransform(paisa6a, paisa6b))
        self.play(ShowCreation(f1), FadeIn(f1text))
        self.wait(2)
        self.play(Write(montext4))
        self.play(GrowArrow(montext4arr1))
        self.wait(2)
        self.play(Write(paisa7))
        self.play(Write(paisa8))
        self.play(ReplacementTransform(f1, f2))
        self.play(FadeOut(paisa1a), FadeOut(paisa2a), FadeOut(kids), FadeOut(paisa3a), FadeOut(paisa4a), FadeOut(paisa5a), FadeOut(paisa6b), FadeOut(paisa7), FadeOut(paisa8),
        FadeOut(monname), FadeOut(monname1), FadeOut(f2), FadeOut(f1text), FadeOut(montext1), FadeOut(montext1a), FadeOut(montext1arr1), FadeOut(montext1arr2), 
        FadeOut(montext2), FadeOut(montext2a), FadeOut(montext2arr1),  FadeOut(montext2arr2),  FadeOut(montext3),  FadeOut(montext3arr1), FadeOut(montext4),  FadeOut(montext4arr1))
        self.play(GrowFromCenter(tf1))
        self.play(FadeOut(tf1))
        self.play(GrowFromCenter(tf2))
        self.play(FadeOut(tf2))
        self.play(FadeOut(gard), FadeIn(image))

        image=ImageMobject("./road1.png")
        image.scale(5.6)
        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" So this was one\\\\"
        "simple reason\\\\",
        "why you guys must\\\\",
        "save money").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.4*UP)

        tcfy = TextMobject("Now on the next\\\\",
        "episode, we will be\\\\",
        "talking about the\\\\",
        "strategies to\\\\"
        "save money").set_color(BLACK)
        tcfy.scale(0.75)
        tcfy.move_to(3.5*LEFT+2.4*UP)

        lastf = TextMobject("Thank\\\\",
        "YOU!").set_color(BLACK)
        lastf.move_to(3.5*LEFT+2.4*UP).scale(2)



        
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a), Write(thoughtcloud2))
        self.play(Write(thoughtcloud2text1, run_time=3))
        self.wait()
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tcfy, run_time=5))
        self.wait()
        self.play(FadeOut(tcfy))
        self.wait(3)
        self.play(Write(lastf))
        self.wait(3)
        self.play(FadeOut(thoughtcloud2), FadeOut(lastf), ReplacementTransform(car1a, car2a))
        

        



