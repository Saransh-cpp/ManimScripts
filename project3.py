from manimlib.imports import *
class vid2(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
         
        g= NumberPlane()

        self.add_sound("project3a.m4a")

        officescene = ImageMobject("./building.png")
        officescene.scale(7.5)
        officescene.move_to(1.7*UP)

        fincar1 = ImageMobject("./car.png")
        fincar1.move_to(10*LEFT+3*DOWN)
        fincar = ImageMobject("./car.png")
        fincar.move_to(3*LEFT+3*DOWN)
        fincar2 = ImageMobject("./car.png")
        fincar2.move_to(10*RIGHT+3*DOWN)
        ecar1 = ImageMobject("./car.png")
        ecar1.move_to(10*RIGHT+3*DOWN)
        fincloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        fincloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        fincloud.next_to(fincar, UP, buff=0.1)
        fincloud1.scale(1.5)
        fincloud1.next_to(fincar, UP, buff=0.1)
        fincloudtext1 = TextMobject("Oh hi\\\\",
        "again!").set_color(BLACK)
        fincloudtext1.move_to(3*LEFT+0.7*DOWN)
        fincloudtext2 = TextMobject("Welcome back to\\\\",
        "the episode of\\\\"
        "different investment\\\\",
        "options in India!").set_color(BLACK)
        fincloudtext2.move_to(3*LEFT)
        fincloudtext2.scale(0.75)

        office = ImageMobject("./officebg.png")
        office.scale(4)
        officem = ImageMobject("./officem.png")
        officem.scale(2)
        officem.move_to(2*LEFT+2*DOWN)
        oc1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        oc1.scale(1.7)
        oc1.next_to(officem, UP, buff=0.1)
        oc1t1 = TextMobject("Till now we have\\\\",
        "learnt how to save\\\\",
        "money and the\\\\",
        "necessity to\\\\",
        "INVEST!").set_color(BLACK)
        oc1t1.scale(0.7)
        oc1t1.move_to(2*LEFT+2.3*UP)
        oc1t2 = TextMobject("But the next thought\\\\",
        "in your mind would\\\\",
        "be where should we\\\\",
        "invest our money?\\\\",
        "What are the options?\\\\",
        "So, here we go").set_color(BLACK)
        oc1t2.scale(0.6)
        oc1t2.move_to(2*LEFT+2.3*UP)
        oc1t3 = TextMobject("So, basically there are\\\\",
        "4 options where you\\\\",
        "could invest your\\\\",
        "money").set_color(BLACK)
        oc1t3.scale(0.7)
        oc1t3.move_to(2*LEFT+2.3*UP)

        
        
        city= ImageMobject("./city.png")
        city.scale(10)
        city.move_to(2.3*DOWN+1*LEFT)
        
        
        
        self.play(FadeInFromDown(officescene))
        self.play(ReplacementTransform(fincar1,fincar))
        self.play(Write(fincloud))
        self.play(Write(fincloudtext1))
        self.wait()
        self.play(ReplacementTransform(fincloud,fincloud1), ReplacementTransform(fincloudtext1,fincloudtext2))
        self.wait(2.5)
        self.play(FadeInFromDown(office), FadeInFromDown(officem), ReplacementTransform(fincar,ecar1), FadeOut(fincloud1), FadeOut(officescene), FadeOut(fincloudtext2))
        self.play(Write(oc1))
        self.play(Write(oc1t1, run_time=4))
        self.play(ReplacementTransform(oc1t1, oc1t2))
        self.wait(8)
        self.play(ReplacementTransform(oc1t2, oc1t3))
        self.wait(4)
        self.play(FadeIn(city), FadeOut(officem), FadeOut(oc1t3), FadeOut(office), FadeOut(oc1))
        
        
        
        bank = ImageMobject("./bank.png")
        bank.scale(2)
        g= NumberPlane()
        
        
        bank.move_to(4*RIGHT+2.4*DOWN)
        corp = ImageMobject("./corp.png")
        corp.move_to(3*DOWN+1.5*RIGHT)
        bucks = ImageMobject("./bucks.png")

        n1t1 = TextMobject("The first domain that we are talking about\\\\",
        "gives you fixed returns over your investment").set_color(BLACK)
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
        at2 = TextMobject("6-8 percent "
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
        bank2.scale(0.75)
        time.scale(0.75)
        bank2.next_to(a1, RIGHT, buff=0.1)
        time.next_to(a2, DOWN, buff=0.1)

        f1 = TextMobject("It is the\\\\"
        "safest investment\\\\" 
        "option\\\\", "among all").set_color(BLACK)
        f2 = TextMobject("The", " low risk\\\\","-"," low return\\\\","option!")
        f2[0].set_color(BLACK)
        f2[1].set_color(RED)
        f2[2].set_color(BLACK)
        f2[3].set_color(RED)
        f2[4].set_color(BLACK)
        f1.move_to(2*LEFT+2*UP)
        f2.move_to(2*LEFT+UP)
        f1.scale(0.5)
        f1.move_to(1.5*RIGHT+0.6*DOWN)
        f2.scale(0.7)
        f2.move_to(1.5*RIGHT+0.7*DOWN)
    



        bun = ImageMobject("./bungalow.png")
        bun.scale(5)




        self.play(FadeInFromDown(bank))
        self.play(Write(n1t1, run_time=6))
        self.play(FadeInFromDown(buck))
        self.play(GrowArrow(arr))
        self.play(Write(invest))
        self.play(FadeIn(t1))
        self.play(GrowArrow(arr1))
        self.play(Write(t2))
        self.wait()
        self.play(ReplacementTransform(n1t1, t3))
        self.wait(4)
        self.play(GrowFromEdge(corp,LEFT,run_time=0.5), Write(bcloud), Write(t4, run_time=3))
        self.play(Write(at1, run_time=1.5))
        self.play(GrowArrow(a))
        self.play(Write(at2, run_time=1.5))
        self.play(Write(d, run_time=1.5))
        self.play(GrowArrow(a1), GrowArrow(a2))
        self.play(GrowFromCenter(bank2), GrowFromCenter(time))
        self.play(FadeOut(t4))
        self.play(Write(f1))
        self.play(FadeOut(f1))
        self.play(Write(f2))
        self.wait(2)
        self.play(FadeOut(corp), FadeOut(at1), FadeOut(a), FadeOut(at2),
        FadeOut(bcloud), FadeOut(f2), FadeOut(t1), FadeOut(t2), FadeOut(t3),
        FadeOut(arr1), FadeOut(buck), FadeOut(invest), FadeOut(arr),
        FadeOut(bank), FadeInFromDown(bun), FadeOut(city), FadeOut(time), FadeOut(bank2), FadeOut(d), FadeOut(a1), FadeOut(a2))
        
        
        bm = ImageMobject("./bm.png")
        bm.move_to(3*RIGHT+1.5*DOWN)
        bmc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        bmc.scale(2)
        bmc.next_to(bm, UP, buff=0.1)


        s2ct1 = TextMobject("The other domain",
        " next here\\\\",
        "is real estate").set_color(BLACK)
        s2ct2 = TextMobject("Now what\\\\" 
        "is Real\\\\",
        "Estate?").set_color(BLACK)
        s2ct1.scale(1.3)
        s2ct1.move_to(3*UP)
        s2ct2.scale(1.2)
        s2ct2.move_to(3*RIGHT+2.3*UP)
        s2t1 = TextMobject("Suppose you saved a\\\\" 
        "lot of money and\\\\",
        "invested it to buy a\\\\"
        "plot. After a\\\\"
        "few years").set_color(BLACK)
        s2t1.scale(0.8)
        s2t1.move_to(3*RIGHT+2.2*UP)
        plot = ImageMobject("./housee.png")
        plot.move_to(RIGHT+3*UP)
        s2a1 = Arrow(RIGHT, LEFT).set_color(BLACK)
        s2a2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s2a1.scale(0.5)
        s2a2.scale(0.5)
        s2a1.next_to(plot, LEFT, buff=0.1)
        s2a2.next_to(plot, RIGHT, buff=0.1)
        a1t = TextMobject("Huge Return!").set_color(RED)
        a2t = TextMobject("Loss!").set_color(RED)
        a1t.next_to(s2a2, RIGHT, buff=0.1)
        a2t.next_to(s2a1, LEFT, buff=0.1)
        ur = TextMobject("Unpredicatable return").set_color(BLACK)
        ur.move_to(RIGHT+2*UP)
        sr1 = SurroundingRectangle(a1t, buff=0.1).set_color(BLACK)
        sr2 = SurroundingRectangle(a2t, buff=0.1).set_color(BLACK)
        sr = SurroundingRectangle(ur, buff=0.1).set_color(BLACK)

        s2f = TextMobject("Thus this option\\\\", 
        "is not ideal for\\\\",
        "students as huge\\\\",
        "investment is required").set_color(BLACK)
        s2f.scale(0.8)
        s2f.move_to(3*RIGHT+2.2*UP)





        self.play(Write(s2ct1, run_time=2))
        self.play(FadeOut(s2ct1), FadeInFromDown(bm))
        self.play(Write(bmc), Write(s2ct2, run_time=3))
        self.play(FadeOut(s2ct2))
        self.play(Write(s2t1, run_time=5))
        self.play(FadeOut(bmc), FadeOut(s2t1))
        self.play(FadeInFromDown(plot))
        self.play(GrowArrow(s2a1), GrowArrow(s2a2))
        self.play(Write(a1t, run_time=3), Write(a2t, run_time=3))
        self.play(ShowCreation(sr1), ShowCreation(sr2))
        self.play(Write(ur, run_time=2))
        self.play(ReplacementTransform(sr1, sr), ReplacementTransform(sr2, sr))
        self.play(FadeOut(ur), FadeOut(sr), FadeOut(plot), FadeOut(a1t)
        , FadeOut(a2t), FadeOut(s2a1), FadeOut(s2a2))
        self.play(Write(bmc, run_time=0.5))
        self.play(Write(s2f, run_time=7))
        self.play(FadeInFromDown(office), FadeInFromDown(officem), FadeOut(bun), FadeOut(bm), FadeOut(bmc), FadeOut(s2f))
        
        
        
        
        s3t1 = TextMobject("The third\\\\",
        "domain here\\\\",
        "is equity").set_color(BLACK)
        s3t2 = TextMobject("Equity provides you\\\\",
        "the highest return\\\\"
        "among all the options\\\\",
        "from past analysis\\\\").set_color(BLACK)
        s3t3 = TextMobject("If you invest it\\\\",
        "right it is the smartest\\\\"
        "investment option you\\\\",
        "could go for").set_color(BLACK)
        s3t4 = TextMobject("Now what\\\\",
        "is equity?").set_color(BLACK)
        s3t2.scale(0.7)
        s3t3.scale(0.7)
        s3t1.move_to(2*LEFT+2.3*UP)
        s3t2.move_to(2*LEFT+2.3*UP)
        s3t3.move_to(2*LEFT+2.3*UP)
        s3t4.move_to(2*LEFT+2.3*UP)

        eet = TextMobject("Equity basically means investing\\\\",
        "in a company").set_color(BLACK)
        ee1 = TextMobject("Invest").set_color(BLACK)
        ee2 = TextMobject("mutual funds").set_color(BLACK)
        ec = TextMobject("Company").set_color(BLACK)
        eet.move_to(2*LEFT+2*UP)
        ee1.move_to(3.5*LEFT+0.5*UP)
        ec.move_to(2*RIGHT)
        ee2.move_to(1*LEFT+1*DOWN)
        eea1 = Arrow(ee1.get_right(), ec.get_left(), buff=0.1).set_color(BLACK)
        eea2 = Arrow(ee1.get_bottom(), ee2.get_left(), buff=0.1).set_color(BLACK)
        eea3 = Arrow(ee2.get_right(), ec.get_left(), buff=0.1).set_color(BLACK)

        eq1 = TextMobject("It just requires a bit of\\\\",
        "information and any amount of money\\\\",
        "could be invested").set_color(BLACK)
        eq2 = TextMobject("If you are new here,don't\\\\",
        "worry, we are here to guide you").set_color(BLACK)
        eq3 = TextMobject("We will be talking about it\\\\",
        "in detail in our upcoming episodes").set_color(BLACK)
        eq1.move_to(2*LEFT+2*UP)
        eq2.move_to(2*LEFT+0.4*UP)
        eq3.move_to(2*LEFT+DOWN)
        calc = ImageMobject("./calc.png")
        calc.scale(2)
        calc.move_to(4*RIGHT+DOWN)
        bu = ImageMobject("./bucks.png")
        bu.move_to(3*UP+2*RIGHT)
        buar = Arrow(LEFT,RIGHT).set_color(BLACK)
        buar.scale(0.5)
        buar.next_to(bu, RIGHT, buff=0.1)
        any = TextMobject("Any amount!").set_color(BLACK)
        any.next_to(buar, RIGHT, buff=0.1)

        j = ImageMobject("./jewel.png")
        j.scale(4)


        self.play(Write(oc1, run_time=0.1))
        self.play(Write(s3t1, run_time=2))
        self.play(FadeOut(s3t1))
        self.play(Write(s3t2, run_time=6))
        self.wait(3)
        self.play(FadeOut(s3t2))
        self.play(Write(s3t3, run_time=6))
        self.play(FadeOut(s3t3))
        self.play(Write(s3t4))
        self.play(FadeOut(s3t4))
        self.play(FadeOut(officem), FadeOut(oc1))
        self.play(Write(eet))
        self.play(Write(ee1))
        self.play(GrowArrow(eea1), GrowArrow(eea2))
        self.play(Write(ee2))
        self.play(GrowArrow(eea3))
        self.play(Write(ec))
        self.play(FadeOut(eet), FadeOut(ee1), FadeOut(ee2), FadeOut(ec), FadeOut(eea1), FadeOut(eea2), FadeOut(eea3))
        self.play(AnimationGroup(Write(eq1, run_time=3), FadeIn(bu), GrowArrow(buar), Write(any), lag_ratio=0.3))
        self.play(AnimationGroup(Write(eq2, run_time=8), FadeIn(calc), lag_ratio=0.3))
        self.play(Write(eq3, run_time=3))
        self.wait()
        self.play(FadeInFromDown(j), FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(calc), FadeOut(bu), FadeOut(any), FadeOut(buar), FadeOut(office))






        

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

        
        
        
        
        
        
        
        self.play(Write(s4t1, run_time=4))
        self.play(Write(c4))
        self.play(Write(s4t2, run_time=1.5))
        self.play(FadeOut(s4t2))
        self.play(Write(s4t3, run_time=3))
        self.play(GrowFromCenter(silver))
        self.wait(0.5)
        self.play(GrowFromCenter(gold))
        self.wait(0.5)
        self.play(GrowFromCenter(platinum))
        self.wait(0.5)
        self.play(Write(avg, run_time=3))
        self.play(GrowArrow(avga))
        self.play(Write(avg1, run_time=3))
        self.play(FadeOut(avg), FadeOut(avga), FadeOut(avg1))
        self.play(Write(s4t4, run_time=4))
        self.play(FadeOut(s4t4), FadeOut(gold), FadeOut(silver), FadeOut(platinum)
        , FadeOut(c4), FadeInFromDown(officescene), FadeOut(s4t3), FadeOut(s4t1), FadeOut(j))

        
        
        
        
        ft = TextMobject("So, these are the\\\\",
        "general investment\\\\",
        "options one can\\\\",
        "opt for").set_color(BLACK)
        ft.scale(0.7)
        fta = TextMobject("And if we talk about the best in\\\\",
        "terms of returns is equity").set_color(BLACK)
        ftb = TextMobject("As it provides you the highest return of\\\\",
        "15-16 percent over your investment\\\\"
        "which is pretty good").set_color(BLACK)
        fta.move_to(3*UP)
        ftb.move_to(2.5*UP)
        ft.move_to(3*LEFT)

        ft1 = TextMobject("Thank you for\\\\" "being with us").set_color(BLACK)
        ft2 = TextMobject("We will meet\\\\", "you in the\\\\", "next episode of\\\\","personal finance").set_color(BLACK)
        ft2.scale(0.7)
        ft1.move_to(3*LEFT)
        ft2.move_to(3*LEFT)
        fincar1a = ImageMobject("./car.png")
        fincar1a.move_to(10*LEFT+3*DOWN)
        fincara = ImageMobject("./car.png")
        fincara.move_to(3*LEFT+3*DOWN)
        fincar2a = ImageMobject("./car.png")
        fincar2a.move_to(10*RIGHT+3*DOWN)
        ecar1a = ImageMobject("./car.png")
        ecar1a.move_to(10*RIGHT+3*DOWN)


        self.play(ReplacementTransform(fincar1a, fincara))
        self.play(Write(fincloud1), Write(ft, run_time=3.5))
        self.play(Write(fta, run_time=5))
        self.play(ReplacementTransform(fta, ftb))
        self.wait(7)
        self.play(FadeOut(ft), FadeOut(ftb))
        
        
        self.play(Write(ft1, run_time=1.5))
        self.play(FadeOut(ft1))
        self.play(Write(ft2, run_time=2))
        self.play(FadeOut(ft2))
        self.play(ReplacementTransform(fincara, fincar2a), FadeOut(fincloud1))

 

        



        
        

        

        




        self.wait()
        self.add(g)
