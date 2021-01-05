from manimlib.imports import *
class vid6(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("project7a1.m4a")

        image=ImageMobject("./road1.png")
        image.scale(5.6)

        car = ImageMobject("./car.png")
        car.move_to(1*DOWN+10*LEFT)
        car1 = ImageMobject("./car.png")
        car1.move_to(1*DOWN+3.5*LEFT)
        car2 = ImageMobject("./car.png")
        car2.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("Oh Hi!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome to the\\\\"
        "episode of how you\\\\",
        "can choose the\\\\",
        "right funds").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.3*UP)

        thoughtcloud1a = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1a.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1a = TextMobject("and invest\\\\",
        "your money").set_color(BLACK)
        thoughtcloud1text1a.scale(0.75)
        thoughtcloud1text1a.move_to(3.5*LEFT+1.25*UP)

        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        text1 = TextMobject("Till now, we know ").set_color(BLACK)
        text1.move_to(2.5*UP)
        text2 = TextMobject("Invest").set_color(RED)
        text2.scale(1.3)
        text2.move_to(UP+1.5*LEFT)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(text2, RIGHT, buff=0.1)
        text3 = TextMobject("Where and\\\\", "Why").set_color(RED)
        text3.next_to(arr1, RIGHT, buff=0.1)

        text4 = TextMobject("But this is the most important stage\\\\",
        "where due to lack of").set_color(BLACK)
        text4.scale(1.2)
        text4.move_to(2.75*UP)

        know = ImageMobject("./creative.png")
        know.move_to(0.5*UP+4*LEFT)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.next_to(know, RIGHT, buff=0.1)
        text5 = TextMobject("Loose their\\\\",
        "motivation").set_color(RED)
        text5.next_to(arr2, RIGHT, buff=0.1)
        arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        arr3.next_to(text5, RIGHT, buff=0.1)
        text6 = TextMobject("End up keeping\\\\",
        "their money at\\\\",
        "home").set_color(BLACK)
        text6.next_to(arr3, RIGHT, buff=0.1)

        text7 = TextMobject("Don't worry we will guide\\\\",
        "you in the right path").set_color(RED)
        text7.scale(1.4)
        text7.move_to(UP)

        text8 = TextMobject("So the first thing is that index funds are the\\\\",
        "options to invest in").set_color(BLACK)
        text8.scale(1.3)
        text8.move_to(2.5*UP)
        text9 = TextMobject("There are two ways in which you can invest").set_color(RED)
        text9.scale(1.3)
        text9.move_to(1*UP)

        









        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1), ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.wait()
        self.play(FadeOut(thoughtcloud2text1), ReplacementTransform(thoughtcloud2, thoughtcloud1a))
        self.play(Write(thoughtcloud1text1a))
        self.play(FadeOut(thoughtcloud1text1a))
        self.play(FadeOut(thoughtcloud1a), FadeOut(trees), ReplacementTransform(car1, car2))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(arr1))
        self.play(Write(text3))
        self.play(FadeOut(text1), FadeOut(text3), FadeOut(text2), FadeOut(arr1))
        self.play(Write(text4))
        self.play(GrowFromCenter(know))
        self.play(Write(arr2))
        self.play(Write(text5))
        self.play(Write(arr3))
        self.play(Write(text6))
        self.play(FadeOut(text4), FadeOut(know), FadeOut(arr2), FadeOut(text5), FadeOut(arr3), FadeOut(text6))
        self.play(GrowFromCenter(text7))
        self.play(FadeOut(text7))
        self.play(Write(text8))
        self.play(GrowFromCenter(text9))
        inv = ImageMobject("./inv.png").scale(5)
        self.play(FadeOut(text8), FadeIn(inv), FadeOut(text9), FadeOut(image))


        
        corp = ImageMobject("./corp.png").scale(2)
        corp.move_to(2*LEFT+2*DOWN)

        t1 = TextMobject("The first one is through\\\\",
        "an", " AGENT").scale(1.2)
        t1[0].set_color(BLACK)
        t1[1].set_color(BLACK)
        t1[2].set_color(RED)
        t1.move_to(3*UP)

        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(corp, RIGHT, buff=0.1)
        t2 = TextMobject("Charge", " commission ", "on\\\\",
        "your investment").next_to(s2arr1, RIGHT, buff=0.1)
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2[3].set_color(BLACK)

        t2a = TextMobject("Commission depends upon\\\\",
        "agents to agents").set_color(BLACK)
        t2a.next_to(s2arr1, RIGHT, buff=0.1)

        t3 = TextMobject("In this Digital Era").set_color(BLACK)
        t3.scale(1.5)
        t3.move_to(2.5*UP)

        no = ImageMobject("./no.png").scale(2.5)
        no.move_to(2*LEFT+2*DOWN)

        t4 = TextMobject("Not recommended").set_color(BLACK)
        t4.next_to(s2arr1, RIGHT, buff=0.1)

        t5 = TextMobject("There are a lot of disadvantages,\\\\",
        "such as -").set_color(BLACK)
        t5.scale(1.2)
        t5.move_to(3*UP)

        paper = ImageMobject("./paperwork.png")
        paper.move_to(2*LEFT)
        time = ImageMobject("./timec.png")
        time.move_to(2*RIGHT)

        t6 = TextMobject("The commission which is charged\\\\",
        "piles up and becomes a huge amount in long term").set_color(BLACK)
        t6.move_to(3*DOWN)

        t7 = TextMobject("The other way is through\\\\",
        "Online Platforms").scale(1.2)
        t7[0].set_color(BLACK)
        t7[1].set_color(RED)
        t7.move_to(2.75*UP)

        grow = ImageMobject("./groww.png")
        upstox = ImageMobject("./upstox.png")
        grow.move_to(3*LEFT)
        upstox.move_to(3*RIGHT)

        dot1 = Dot().set_color(BLACK)
        dot2 = Dot().set_color(BLACK)
        dot1.move_to(3.7*DOWN+2*LEFT)
        dot2.move_to(DOWN+2*LEFT)
        line1 = Line(dot1.get_top(),dot2.get_bottom(),buff=0.1).set_color(BLACK)
       

        t8 = TextMobject("Without Commision").set_color(BLACK)
        t9 = TextMobject("Quite Easy").set_color(BLACK)
        t10 = TextMobject("User Friendly").set_color(BLACK)
        t8.move_to(1.5*DOWN+0.3*RIGHT)
        t9.move_to(2.5*DOWN+0.7*LEFT)
        t10.move_to(3.5*DOWN+0.4*LEFT)

        t11 = TextMobject("These were the 2 methods for investment but now comes the\\\\",
        "main part of choosing the right funds for your investment").set_color(BLACK)
        t11.move_to(2.75*UP)
        t12 = TextMobject("Plenty of").set_color(BLACK)
        t12.move_to(UP+2*LEFT)
        t2arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr2.next_to(t12, RIGHT, buff=0.1)
        t12a = TextMobject("Index Funds").set_color(RED)
        t12a.next_to(t2arr2, RIGHT, buff=0.1)

        t13 = TextMobject("For the right step").set_color(BLACK)
        t13.move_to(3*LEFT)
        t2arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr3.next_to(t13, RIGHT, buff=0.1)
        t13a = TextMobject("A Little Knowledge").set_color(RED)
        t13a.next_to(t2arr3, RIGHT, buff=0.1)






        
        self.play(Write(t1))
        self.play(GrowFromCenter(corp))
        self.play(Write(s2arr1))
        self.play(Write(t2))
        self.play(ReplacementTransform(t2, t2a))
        self.play(FadeOut(t2a), FadeOut(s2arr1), FadeOut(t1))
        self.play(Write(t3))
        self.play(Write(s2arr1))
        self.play(Write(t4))
        self.play(GrowFromCenter(no))
        self.play(FadeOut(no), FadeOut(corp), FadeOut(t3), FadeOut(t4), FadeOut(s2arr1))
        self.play(Write(t5))
        self.play(GrowFromCenter(paper))
        self.play(GrowFromCenter(time))
        self.play(Write(t6))
        self.play(FadeOut(t5), FadeOut(t6), FadeOut(paper), FadeOut(time))
        self.play(Write(t7))
        self.play(GrowFromCenter(grow))
        self.play(GrowFromCenter(upstox))
        self.play(Write(dot2))
        self.play(Write(line1))
        self.play(Write(dot1))
        self.play(Write(t8))
        self.play(Write(t9))
        self.play(Write(t10))
        self.play(FadeOut(t9), FadeOut(t10), FadeOut(t8), FadeOut(dot1), FadeOut(dot2),
        FadeOut(line1), FadeOut(grow), FadeOut(upstox), FadeOut(t7))
        self.play(Write(t11))
        self.play(Write(t12))
        self.play(Write(t2arr2))
        self.play(Write(t12a))
        self.play(Write(t13))
        self.play(Write(t2arr3))
        self.play(Write(t13a))
        inv2 = ImageMobject("./inva.png").scale(4)
        self.play(FadeOut(t11), FadeOut(t12), FadeOut(t2arr2), FadeOut(t12a), 
        FadeOut(t13), FadeOut(t13a), FadeOut(t2arr3), FadeOut(inv), FadeIn(inv2))


        

        s1 = TextMobject("The first thing before choosing\\\\",
        "the right fund is -").set_color(BLACK)
        s1.move_to(2.5*UP)
        s2 = TextMobject("FUND").set_color(BLACK)
        s2.move_to(1.5*UP+5*LEFT)
        sarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr1.next_to(s2, RIGHT, buff=0.1)
        s3 = TextMobject("Nifty or\\\\",
        "Sensex").set_color(YELLOW)
        s3.next_to(sarr1, RIGHT, buff=0.1)
        sarr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr2.next_to(s3, RIGHT, buff=0.1)
        s4 = TextMobject("Under DIRECT GROWTH").set_color(BLACK)
        s4.next_to(sarr2, RIGHT, buff=0.1)

        f1 = SurroundingRectangle(s3, buff=0.1)
        f2 = SurroundingRectangle(s4, buff=0.1)
        ft = TextMobject("REMEMBER THESE TERMS!").set_color(BLACK)
        ft.scale(2)

        s5 = TextMobject("The other thing you should keep in mind\\\\",
        "is ", "Expense Ratio ", "and ", "Exit Load")
        s5[0].set_color(BLACK)
        s5[1].set_color(BLACK)
        s5[2].set_color(YELLOW)
        s5[3].set_color(BLACK)
        s5[4].set_color(YELLOW)
        s5.move_to(2.5*UP)

        thinker = ImageMobject("./thinker.png").scale(1.5)
        thinker.move_to(2*DOWN+4*RIGHT)
        tc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        tc.next_to(thinker, UP, buff=0.1)

        tct1 = TextMobject("Now what is\\\\",
        "expense ratio?").set_color(BLACK)
        tct1.scale(0.7)
        tct1.move_to(4*RIGHT+0.9*UP)

        s6 = TextMobject("Charged over your\\\\",
        "investment").set_color(BLACK)
        s6.scale(0.9)
        s3arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash = ImageMobject("./tmoney.png")
        cash.move_to(5*LEFT)
        s3arr1.next_to(cash, RIGHT, buff=0.1)
        s6.next_to(s3arr1, RIGHT, buff=0.1)

        s7 = TextMobject("Lower Expense Ratio").set_color(BLACK)
        s7.scale(0.9)
        s7.move_to(5*LEFT+2*DOWN)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s7, RIGHT, buff=0.1)
        s8 = TextMobject("Higher Returns").set_color(BLACK)
        s8.scale(0.9)
        s8.next_to(s3arr2, RIGHT, buff=0.1)

        s9 = TextMobject("There are various funds having an expense ratio\\\\",
        "of 1-2 percent which is not at all\\\\"
        "Recommended").set_color(BLACK)
        s9.scale(1.3)
        s9.move_to(2.3*UP)
        s10 = TextMobject("These percentages make a huge difference\\\\",
        "in long run").set_color(BLACK)
        s10.next_to(s9, DOWN, buff=1)

        s11 = TextMobject("Always Go for Funds having\\\\",
        "having MIN Expense Ratio").set_color(BLACK)
        s11.scale(1.5)

        tct2 = TextMobject("So what is\\\\",
        "exit load?").set_color(BLACK)
        tct2.scale(0.7)
        tct2.move_to(4*RIGHT+0.9*UP)
        s12 = TextMobject("Exit Load is basically").set_color(BLACK)
        s12.scale(1.5)
        s12.move_to(2.3*UP)
        s6a = TextMobject("Charged while you\\\\",
        "sell off your funds").set_color(BLACK)
        s6a.scale(0.9)
        s3arr1a = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash1 = ImageMobject("./tmoney.png")
        cash1.move_to(5*LEFT)
        s3arr1a.next_to(cash1, RIGHT, buff=0.1)
        s6a.next_to(s3arr1a, RIGHT, buff=0.1)

        s13 = TextMobject("The funds that you've selected must have\\\\",
        "a minimum exit load or even NIL").set_color(BLACK)
        s13.scale(1.3)
        s13.move_to(2.3*UP)

        s14 = TextMobject("NIL exit load").set_color(BLACK)
        s14.scale(0.9)
        s14.move_to(5*LEFT+2*DOWN)
        s3arr4 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr4.next_to(s14, RIGHT, buff=0.1)
        s15 = TextMobject("PREFERRED!").set_color(BLACK)
        s15.scale(0.9)
        s15.next_to(s3arr4, RIGHT, buff=0.1)











        
        self.play(Write(s1))
        self.play(Write(s2))
        self.play(Write(sarr1))
        self.play(Write(s3))
        self.play(Write(sarr2))
        self.play(Write(s4))
        self.play(ShowCreation(f1))
        self.play(ShowCreation(f2))
        self.play(GrowFromCenter(ft))
        self.play(FadeOut(sarr1), FadeOut(sarr2), FadeOut(ft), FadeOut(f1),
        FadeOut(f2), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4))
        self.play(Write(s5))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct1))
        self.play(FadeIn(cash))
        self.play(Write(s3arr1))
        self.play(Write(s6))
        self.play(Write(s7))
        self.play(Write(s3arr2))
        self.play(Write(s8))
        self.play(FadeOut(s5), FadeOut(thinker), FadeOut(tc), FadeOut(tct1),
        FadeOut(cash), FadeOut(s6), FadeOut(s3arr1), FadeOut(s7), FadeOut(s8),
        FadeOut(s3arr2))
        self.play(Write(s9))
        self.play(Write(s10))
        self.play(FadeOut(s9), FadeOut(s10))
        self.play(GrowFromCenter(s11))
        self.play(FadeOut(s11))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct2))
        self.play(Write(s12))
        self.play(FadeIn(cash1))
        self.play(Write(s3arr1a))
        self.play(Write(s6a))
        self.play(ReplacementTransform(s12, s13))
        self.play(Write(s14))
        self.play(Write(s3arr4))
        self.play(Write(s15))
        inv3 = ImageMobject("./inv3r.png").scale(4.5)
        self.play(FadeOut(s14), FadeOut(s15), FadeOut(s3arr4), FadeOut(s13), 
        FadeOut(tc), FadeOut(tct2), FadeOut(thinker), FadeOut(cash1), FadeOut(s6a),
        FadeOut(s3arr1a), FadeOut(inv2), FadeIn(inv3))


        y1 = TextMobject("The other thing you can check before finalising\\\\",
        "your funds is it's").set_color(BLACK)
        y1.move_to(2.3*UP)

        rate = ImageMobject("./rating.png").move_to(3*LEFT)
        yarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        y2 = TextMobject("Higher the rating, more\\\\",
        "promising are the funds").set_color(BLACK)
        yarr1.next_to(rate, RIGHT, buff=0.1)
        y2.next_to(yarr1, RIGHT, buff=0.1)

        y3 = TextMobject("Some of the ideal index funds\\\\",
        "recommended by our mentors are -").set_color(BLACK)
        y3.move_to(2.3*UP)

        y3a = TextMobject("UTI NIFTY DIRECT GROWTH Index fund").set_color(BLACK)
        y3a.move_to(0.5*UP)
        y3b = TextMobject("HDFC SENSEX DIRECT GROWTH Index fund").set_color(BLACK)
        y3b.move_to(DOWN)

        y4 = TextMobject("Having low expense ratio and NIL exit load").set_color(BLACK)
        y4.move_to(2.5*DOWN)
        y5 = TextMobject("If all the criteria matches with your\\\\",
        "fund then it is ideal for you").set_color(BLACK)
        y5.move_to(2.2*UP)

        y6 = TextMobject("After choosing the right fund").set_color(BLACK)
        y6.move_to(2.3*UP)
        
        y7 = TextMobject("INVEST").set_color(BLACK)
        y7.scale(2)
        y7.move_to(2.3*UP)
        y8a = TextMobject("lump-sum").set_color(BLACK)
        y8a.move_to(4*LEFT)
        fa1 = Arrow(y7.get_bottom(), y8a.get_top(), buff=0.3).set_color(BLACK)
        y8b = TextMobject("SIP").set_color(BLACK)
        y8b.move_to(4*RIGHT)
        fa2 = Arrow(y7.get_bottom(), y8b.get_top(), buff=0.3).set_color(BLACK)
        fa3 = Arrow(UP,DOWN).set_color(BLACK)
        fa4 = Arrow(UP,DOWN).set_color(BLACK)
        fa3.next_to(y8a, DOWN, buff=0.1)
        fa4.next_to(y8b, DOWN, buff=0.1)

        fa3t = TextMobject("directly invest a\\\\"
        "big amount").set_color(BLACK)
        fa3t.next_to(fa3, DOWN, buff=0.1)
        fa4t = TextMobject("means on a fixed period\\\\",
        "an amount of money\\\\" 
        "would be deducted\\\\",
        "from your account").set_color(BLACK)
        fa4t.scale(0.8)
        fa4t.next_to(fa4, DOWN, buff=0.1)

        ff = TextMobject("The SIP option is highly recommended as it buys funds\\\\",
        "in all levels of the market which provides more promising results.").set_color(BLACK)

        

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud2a = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2a.scale(2)
        thoughtcloud2a.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1a = TextMobject("Now after registering\\\\"
        "with your personal\\\\",
        "details you are all\\\\",
        "set to go with your\\\\",
        "ideal funds.").set_color(BLACK)
        thoughtcloud2text1a.scale(0.8)
        thoughtcloud2text1a.move_to(3.5*LEFT+2.3*UP)

        
        thoughtcloud2text1aa = TextMobject("If you have reached till\\\\"
        "here you must have\\\\",
        "developed a financial\\\\",
        "goal and a step\\\\",
        "towards investment.").set_color(BLACK)
        thoughtcloud2text1aa.scale(0.8)
        thoughtcloud2text1aa.move_to(3.5*LEFT+2.3*UP)

        tcf = TextMobject("Be Proud\\\\",
        "Of Yourself!!").set_color(BLACK)
        tcf.scale(1.5)
        tcf.move_to(3.5*LEFT+2.3*UP)

        tcff = TextMobject("Thank You!\\\\",
        "for being\\\\",
        "with us").set_color(BLACK)
        tcff.scale(1.5)
        tcff.move_to(3.5*LEFT+2.3*UP)



        







        
        self.play(Write(y1))
        self.play(FadeIn(rate))
        self.play(Write(yarr1))
        self.play(Write(y2))
        self.play(ReplacementTransform(y1,y3))
        self.play(FadeOut(rate), FadeOut(yarr1), FadeOut(y2))
        self.play(GrowFromCenter(y3a))
        self.play(GrowFromCenter(y3b))
        self.play(Write(y4))
        self.play(ReplacementTransform(y3,y5))
        self.play(FadeOut(y5), FadeOut(y3a), FadeOut(y3b), FadeOut(y4))
        self.play(Write(y6))
        self.play(ReplacementTransform(y6,y7))
        self.play(GrowArrow(fa1), GrowArrow(fa2))
        self.play(Write(y8a), Write(y8b))
        self.play(GrowArrow(fa3), GrowArrow(fa4))
        self.play(Write(fa3t))
        self.play(Write(fa4t))
        self.play(FadeOut(fa1), FadeOut(fa2), FadeOut(fa3), FadeOut(fa4), FadeOut(fa3t),
        FadeOut(fa4t), FadeOut(y7), FadeOut(y8a), FadeOut(y8b))
        self.play(Write(ff))
        self.play(FadeOut(ff), FadeOut(inv3), FadeIn(image), FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2a))
        self.play(Write(thoughtcloud2text1a))
        self.wait()
        self.play(ReplacementTransform(thoughtcloud2text1a, thoughtcloud2text1aa))
        self.play(FadeOut(thoughtcloud2text1aa))
        self.play(Write(tcf))
        self.play(FadeOut(tcf))
        self.play(Write(tcff))
        self.play(FadeOut(tcff), FadeOut(thoughtcloud2a)) 
        self.play(ReplacementTransform(car1a, car2a))
        self.wait()



class vid61(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("project7a1.m4a")
        self.wait(39.5)


        inv = ImageMobject("./invr.png").scale(5)
        corp = ImageMobject("./corp.png").scale(2)
        corp.move_to(2*LEFT+2*DOWN)

        t1 = TextMobject("The first one is through\\\\",
        "an", " AGENT").scale(1.2)
        t1[0].set_color(BLACK)
        t1[1].set_color(BLACK)
        t1[2].set_color(RED)
        t1.move_to(3*UP)

        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(corp, RIGHT, buff=0.1)
        t2 = TextMobject("Charge", " commission ", "on\\\\",
        "your investment").next_to(s2arr1, RIGHT, buff=0.1)
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2[3].set_color(BLACK)

        t2a = TextMobject("Commission depends upon\\\\",
        "agents to agents").set_color(BLACK)
        t2a.next_to(s2arr1, RIGHT, buff=0.1)

        t3 = TextMobject("In this Digital Era").set_color(BLACK)
        t3.scale(1.5)
        t3.move_to(2.5*UP)

        no = ImageMobject("./no.png").scale(2.5)
        no.move_to(2*LEFT+2*DOWN)

        t4 = TextMobject("Not recommended").set_color(BLACK)
        t4.next_to(s2arr1, RIGHT, buff=0.1)

        t5 = TextMobject("There are a lot of disadvantages,\\\\",
        "such as -").set_color(BLACK)
        t5.scale(1.2)
        t5.move_to(3*UP)

        paper = ImageMobject("./paperwork.png")
        paper.move_to(2*LEFT)
        time = ImageMobject("./timec.png")
        time.move_to(2*RIGHT)

        t6 = TextMobject("The commission which is charged\\\\",
        "piles up and becomes a huge amount in long term").set_color(BLACK)
        t6.move_to(3*DOWN)

        t7 = TextMobject("The other way is through\\\\",
        "Online Platforms").scale(1.2)
        t7[0].set_color(BLACK)
        t7[1].set_color(RED)
        t7.move_to(2.75*UP)

        grow = ImageMobject("./groww.png")
        upstox = ImageMobject("./upstox.png")
        grow.move_to(3*LEFT)
        upstox.move_to(3*RIGHT)

        dot1 = Dot().set_color(BLACK)
        dot2 = Dot().set_color(BLACK)
        dot1.move_to(3.7*DOWN+2*LEFT)
        dot2.move_to(DOWN+2*LEFT)
        line1 = Line(dot1.get_top(),dot2.get_bottom(),buff=0.1).set_color(BLACK)
       

        t8 = TextMobject("Without Commision").set_color(BLACK)
        t9 = TextMobject("Quite Easy").set_color(BLACK)
        t10 = TextMobject("User Friendly").set_color(BLACK)
        t8.move_to(1.5*DOWN+0.3*RIGHT)
        t9.move_to(2.5*DOWN+0.7*LEFT)
        t10.move_to(3.5*DOWN+0.4*LEFT)

        t11 = TextMobject("These were the 2 methods for investment but now comes the\\\\",
        "main part of choosing the right funds for your investment").set_color(BLACK)
        t11.move_to(2.75*UP)
        t12 = TextMobject("Plenty of").set_color(BLACK)
        t12.move_to(UP+2*LEFT)
        t2arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr2.next_to(t12, RIGHT, buff=0.1)
        t12a = TextMobject("Index Funds").set_color(RED)
        t12a.next_to(t2arr2, RIGHT, buff=0.1)

        t13 = TextMobject("For the right step").set_color(BLACK)
        t13.move_to(3*LEFT)
        t2arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr3.next_to(t13, RIGHT, buff=0.1)
        t13a = TextMobject("A Little Knowledge").set_color(RED)
        t13a.next_to(t2arr3, RIGHT, buff=0.1)






        self.play(FadeIn(inv))
        self.play(Write(t1))
        self.play(GrowFromCenter(corp))
        self.play(Write(s2arr1))
        self.play(Write(t2))
        self.play(ReplacementTransform(t2, t2a))
        self.wait(3)
        self.play(FadeOut(t2a), FadeOut(s2arr1), FadeOut(t1))
        self.play(Write(t3))
        self.play(Write(s2arr1))
        self.play(Write(t4))
        self.play(GrowFromCenter(no))
        self.play(FadeOut(no), FadeOut(corp), FadeOut(t3), FadeOut(t4), FadeOut(s2arr1))
        self.play(Write(t5))
        self.play(GrowFromCenter(paper))
        self.play(GrowFromCenter(time))
        self.wait(2)
        self.play(Write(t6, run_time=8))
        self.play(FadeOut(t5), FadeOut(t6), FadeOut(paper), FadeOut(time))
        self.play(Write(t7))
        self.play(GrowFromCenter(grow))
        self.play(GrowFromCenter(upstox))
        self.wait()
        self.play(Write(dot2))
        self.play(Write(line1))
        self.play(Write(dot1))
        self.play(Write(t8))
        self.wait(4)
        self.play(Write(t9))
        self.play(Write(t10))
        self.wait(5.5)
        self.add_sound("./project7a2")
        self.play(FadeOut(t9), FadeOut(t10), FadeOut(t8), FadeOut(dot1), FadeOut(dot2),
        FadeOut(line1), FadeOut(grow), FadeOut(upstox), FadeOut(t7))
        self.play(Write(t11, run_time=7))
        self.play(Write(t12))
        self.play(Write(t2arr2))
        self.play(Write(t12a), Write(t13))
        self.play(Write(t2arr3, run_time=0.5))
        self.play(Write(t13a, run_time=0.5))
        self.play(FadeOut(t11), FadeOut(t12), FadeOut(t2arr2), FadeOut(t12a), 
        FadeOut(t13), FadeOut(t13a), FadeOut(t2arr3), FadeOut(inv))




        self.wait()
        self.add(g)

class vid62(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()

        self.add_sound("./project7a2")
        self.wait(13)

        inv2 = ImageMobject("./inva.png").scale(4)

        s1 = TextMobject("The first thing before choosing\\\\",
        "the right fund is -").set_color(BLACK)
        s1.move_to(2.5*UP)
        s2 = TextMobject("FUND").set_color(BLACK)
        s2.move_to(1*UP+5*LEFT)
        sarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr1.next_to(s2, RIGHT, buff=0.1)
        s3 = TextMobject("Nifty or\\\\",
        "Sensex").set_color(YELLOW)
        s3.next_to(sarr1, RIGHT, buff=0.1)
        sarr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr2.next_to(s3, RIGHT, buff=0.1)
        s4 = TextMobject("Under DIRECT GROWTH").set_color(BLACK)
        s4.next_to(sarr2, RIGHT, buff=0.1)

        f1 = SurroundingRectangle(s3, buff=0.1)
        f2 = SurroundingRectangle(s4, buff=0.1)
        ft = TextMobject("REMEMBER THESE TERMS!").set_color(BLACK)
        ft.scale(2)
        ft.move_to(0.5*DOWN)

        s5 = TextMobject("The other thing you should keep in mind\\\\",
        "is ", "Expense Ratio ", "and ", "Exit Load")
        s5[0].set_color(BLACK)
        s5[1].set_color(BLACK)
        s5[2].set_color(YELLOW)
        s5[3].set_color(BLACK)
        s5[4].set_color(YELLOW)
        s5.move_to(2.5*UP)

        thinker = ImageMobject("./thinker.png").scale(1.5)
        thinker.move_to(2*DOWN+4*RIGHT)
        tc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        tc.next_to(thinker, UP, buff=0.1)

        tct1 = TextMobject("Now what is\\\\",
        "expense ratio?").set_color(BLACK)
        tct1.scale(0.7)
        tct1.move_to(4*RIGHT+0.9*UP)

        s6 = TextMobject("Charged over your\\\\",
        "investment").set_color(BLACK)
        s6.scale(0.9)
        s3arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash = ImageMobject("./tmoney.png")
        cash.move_to(5*LEFT)
        s3arr1.next_to(cash, RIGHT, buff=0.1)
        s6.next_to(s3arr1, RIGHT, buff=0.1)

        s7 = TextMobject("Lower Expense Ratio").set_color(BLACK)
        s7.scale(0.9)
        s7.move_to(5*LEFT+2*DOWN)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s7, RIGHT, buff=0.1)
        s8 = TextMobject("Higher Returns").set_color(BLACK)
        s8.scale(0.9)
        s8.next_to(s3arr2, RIGHT, buff=0.1)

        s9 = TextMobject("There are various funds having an expense ratio\\\\",
        "of 1-2 percent which is not at all\\\\"
        "Recommended").set_color(BLACK)
        s9.scale(1.3)
        s9.move_to(2.3*UP)
        s10 = TextMobject("These percentages make a huge difference\\\\",
        "in long run").set_color(BLACK)
        s10.next_to(s9, DOWN, buff=1)

        s11 = TextMobject("Always Go for Funds having\\\\",
        "having MIN Expense Ratio").set_color(BLACK)
        s11.scale(1.5)

        tct2 = TextMobject("So what is\\\\",
        "exit load").set_color(BLACK)
        tct2.scale(0.7)
        tct2.move_to(4*RIGHT+0.9*UP)
        s12 = TextMobject("Exit Load is basically").set_color(BLACK)
        s12.scale(1.5)
        s12.move_to(2.3*UP)
        s6a = TextMobject("Charged while you\\\\",
        "sell off your funds").set_color(BLACK)
        s6a.scale(0.9)
        s3arr1a = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash1 = ImageMobject("./tmoney.png")
        cash1.move_to(5*LEFT)
        s3arr1a.next_to(cash1, RIGHT, buff=0.1)
        s6a.next_to(s3arr1a, RIGHT, buff=0.1)

        s13 = TextMobject("The funds that you've selected must have\\\\",
        "a minimum exit load or even NIL").set_color(BLACK)
        s13.scale(1.3)
        s13.move_to(2.3*UP)

        s14 = TextMobject("NIL exit load").set_color(BLACK)
        s14.scale(0.9)
        s14.move_to(5*LEFT+2*DOWN)
        s3arr4 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr4.next_to(s14, RIGHT, buff=0.1)
        s15 = TextMobject("PREFERRED!").set_color(BLACK)
        s15.scale(0.9)
        s15.next_to(s3arr4, RIGHT, buff=0.1)











        self.play(FadeIn(inv2))
        self.play(Write(s1, run_time=3))
        self.play(Write(s2))
        self.play(Write(sarr1))
        self.play(Write(s3))
        self.play(Write(sarr2))
        self.play(Write(s4))
        self.play(ShowCreation(f1))
        self.play(ShowCreation(f2))
        self.play(GrowFromCenter(ft))
        self.play(FadeOut(ft))
        self.wait(20)
        self.play(GrowFromCenter(ft))
        self.play(FadeOut(ft))
        self.play(FadeOut(sarr1), FadeOut(sarr2), FadeOut(f1),
        FadeOut(f2), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4))
        self.play(Write(s5))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct1))
        self.play(FadeIn(cash))
        self.play(Write(s3arr1))
        self.play(Write(s6))
        self.play(Write(s7))
        self.play(Write(s3arr2))
        self.play(Write(s8))
        self.play(FadeOut(s5), FadeOut(thinker), FadeOut(tc), FadeOut(tct1),
        FadeOut(cash), FadeOut(s6), FadeOut(s3arr1), FadeOut(s7), FadeOut(s8),
        FadeOut(s3arr2))
        self.play(Write(s9, run_time=4.5))
        self.play(Write(s10, run_time=4.5))
        self.play(FadeOut(s9), FadeOut(s10))
        self.play(GrowFromCenter(s11))
        self.wait()
        self.play(FadeOut(s11))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct2))
        self.play(Write(s12))
        self.play(FadeIn(cash1))
        self.play(Write(s3arr1a))
        self.play(Write(s6a))
        self.play(ReplacementTransform(s12, s13))
        self.play(Write(s14))
        self.play(Write(s3arr4))
        self.play(Write(s15))
        self.wait(3)
        self.play(FadeOut(s14), FadeOut(s15), FadeOut(s3arr4), FadeOut(s13), 
        FadeOut(tc), FadeOut(tct2), FadeOut(thinker), FadeOut(cash1), FadeOut(s6a),
        FadeOut(s3arr1a))

class vid63(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()

        self.add_sound("./project7a2")
        self.wait(96)

        inv3 = ImageMobject("./inv3r.png").scale(4.5)

        y1 = TextMobject("The other thing you can check before finalising\\\\",
        "your funds is it's").set_color(BLACK)
        y1.move_to(2.3*UP)

        rate = ImageMobject("./rating.png").move_to(3*LEFT)
        yarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        y2 = TextMobject("Higher the rating, more\\\\",
        "promising are the funds").set_color(BLACK)
        yarr1.next_to(rate, RIGHT, buff=0.1)
        y2.next_to(yarr1, RIGHT, buff=0.1)

        y3 = TextMobject("Some of the ideal index funds\\\\",
        "recommended by our mentors are -").set_color(BLACK)
        y3.move_to(2.3*UP)

        y3a = TextMobject("UTI NIFTY DIRECT GROWTH Index fund").set_color(BLACK)
        y3a.move_to(0.5*UP)
        y3b = TextMobject("HDFC SENSEX DIRECT GROWTH Index fund").set_color(BLACK)
        y3b.move_to(DOWN)

        y4 = TextMobject("Having low expense ratio and NIL exit load").set_color(BLACK)
        y4.move_to(2.5*DOWN)
        y5 = TextMobject("If all the criteria matches with your\\\\",
        "fund then it is ideal for you").set_color(BLACK)
        y5.move_to(2.2*UP)

        y6 = TextMobject("After choosing the right fund").set_color(BLACK)
        y6.move_to(2.3*UP)
        
        y7 = TextMobject("INVEST").set_color(BLACK)
        y7.scale(2)
        y7.move_to(2.3*UP)
        y8a = TextMobject("lump-sum").set_color(BLACK)
        y8a.move_to(4*LEFT)
        fa1 = Arrow(y7.get_bottom(), y8a.get_top(), buff=0.3).set_color(BLACK)
        y8b = TextMobject("SIP").set_color(BLACK)
        y8b.move_to(4*RIGHT)
        fa2 = Arrow(y7.get_bottom(), y8b.get_top(), buff=0.3).set_color(BLACK)
        fa3 = Arrow(UP,DOWN).set_color(BLACK)
        fa4 = Arrow(UP,DOWN).set_color(BLACK)
        fa3.next_to(y8a, DOWN, buff=0.1)
        fa4.next_to(y8b, DOWN, buff=0.1)

        fa3t = TextMobject("directly invest a\\\\"
        "big amount").set_color(BLACK)
        fa3t.next_to(fa3, DOWN, buff=0.1)
        fa4t = TextMobject("means on a fixed period\\\\",
        "an amount of money\\\\" 
        "would be deducted\\\\",
        "from your account").set_color(BLACK)
        fa4t.scale(0.8)
        fa4t.next_to(fa4, DOWN, buff=0.1)

        ff = TextMobject("The SIP option is highly recommended as it buys funds\\\\",
        "in all levels of the market which provides more promising results.").set_color(BLACK)

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

        thoughtcloud2a = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2a.scale(2)
        thoughtcloud2a.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1a = TextMobject("Now after registering\\\\"
        "with your personal\\\\",
        "details you are all\\\\",
        "set to go with your\\\\",
        "ideal funds.").set_color(BLACK)
        thoughtcloud2text1a.scale(0.8)
        thoughtcloud2text1a.move_to(3.5*LEFT+2.3*UP)

        
        thoughtcloud2text1aa = TextMobject("If you have reached till\\\\"
        "here you must have\\\\",
        "developed a financial\\\\",
        "goal and a step\\\\",
        "towards investment.").set_color(BLACK)
        thoughtcloud2text1aa.scale(0.8)
        thoughtcloud2text1aa.move_to(3.5*LEFT+2.3*UP)

        tcf = TextMobject("Be Proud\\\\",
        "Of Yourself!!").set_color(BLACK)
        tcf.scale(1.5)
        tcf.move_to(3.5*LEFT+2.3*UP)

        tcff = TextMobject("Thank You!\\\\",
        "for being\\\\",
        "with us").set_color(BLACK)
        tcff.scale(1.5)
        tcff.move_to(3.5*LEFT+2.3*UP)



        







        self.add(inv3)
        self.play(Write(y1, run_time=3))
        self.play(FadeIn(rate))
        self.wait(5)
        self.play(Write(yarr1))
        self.play(Write(y2, run_time=2))
        self.play(ReplacementTransform(y1,y3))
        self.wait(3)
        self.play(FadeOut(rate), FadeOut(yarr1), FadeOut(y2))
        self.play(GrowFromCenter(y3a))
        self.wait(3)
        self.play(GrowFromCenter(y3b))
        self.wait(3)
        self.play(Write(y4))
        self.play(ReplacementTransform(y3,y5))
        self.wait(4)
        self.play(FadeOut(y5), FadeOut(y3a), FadeOut(y3b), FadeOut(y4))
        self.play(Write(y6))
        self.wait(2)
        self.play(ReplacementTransform(y6,y7))
        self.play(GrowArrow(fa1), GrowArrow(fa2))
        self.play(Write(y8a))
        self.play(GrowArrow(fa3))
        self.play(Write(fa3t, run_time=2))
        self.play(Write(y8b))
        self.play(GrowArrow(fa4))
        self.play(Write(fa4t, run_time=6))
        self.wait(4)
        self.play(FadeOut(fa1), FadeOut(fa2), FadeOut(fa3), FadeOut(fa4), FadeOut(fa3t),
        FadeOut(fa4t), FadeOut(y7), FadeOut(y8a), FadeOut(y8b))
        self.play(Write(ff, run_time=8))
        self.play(FadeOut(ff), FadeOut(inv3), FadeIn(image), FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2a))
        self.play(Write(thoughtcloud2text1a, run_time=4))
        self.wait()
        self.play(ReplacementTransform(thoughtcloud2text1a, thoughtcloud2text1aa))
        self.play(FadeOut(thoughtcloud2text1aa, run_time=10))
        self.play(Write(tcf))
        self.play(FadeOut(tcf))
        self.play(Write(tcff))
        self.play(FadeOut(tcff), FadeOut(thoughtcloud2a)) 
        self.play(ReplacementTransform(car1a, car2a))
        self.wait()







        self.wait()
        self.add(g)

class vid64(Scene):

    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()

        inv3 = ImageMobject("./inv3r.png").scale(4.5)

        self.add(inv3)

class vid65(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g = NumberPlane()
        self.add_sound("project7a1.m4a")

        image=ImageMobject("./road1.png")
        image.scale(5.6)

        car = ImageMobject("./car.png")
        car.move_to(1*DOWN+10*LEFT)
        car1 = ImageMobject("./car.png")
        car1.move_to(1*DOWN+3.5*LEFT)
        car2 = ImageMobject("./car.png")
        car2.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("Oh Hi!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome to the\\\\"
        "episode of how you\\\\",
        "can choose the\\\\",
        "right funds").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.3*UP)

        thoughtcloud1a = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1a.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1a = TextMobject("and invest\\\\",
        "your money").set_color(BLACK)
        thoughtcloud1text1a.scale(0.75)
        thoughtcloud1text1a.move_to(3.5*LEFT+1.25*UP)

        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        text1 = TextMobject("Till now, we know ").set_color(BLACK)
        text1.move_to(2.5*UP)
        text2 = TextMobject("Invest").set_color(RED)
        text2.scale(1.3)
        text2.move_to(UP+1.5*LEFT)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(text2, RIGHT, buff=0.1)
        text3 = TextMobject("Where and\\\\", "Why").set_color(RED)
        text3.next_to(arr1, RIGHT, buff=0.1)

        text4 = TextMobject("But this is the most important stage\\\\",
        "where due to lack of").set_color(BLACK)
        text4.scale(1.2)
        text4.move_to(2.75*UP)

        know = ImageMobject("./creative.png")
        know.move_to(0.5*UP+4*LEFT)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.next_to(know, RIGHT, buff=0.1)
        text5 = TextMobject("Loose their\\\\",
        "motivation").set_color(RED)
        text5.next_to(arr2, RIGHT, buff=0.1)
        arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        arr3.next_to(text5, RIGHT, buff=0.1)
        text6 = TextMobject("End up keeping\\\\",
        "their money at\\\\",
        "home").set_color(BLACK)
        text6.next_to(arr3, RIGHT, buff=0.1)

        text7 = TextMobject("Don't worry we are here to guide\\\\",
        "you in the right path").set_color(RED)
        text7.scale(1.4)
        text7.move_to(UP)

        text8 = TextMobject("So the first thing is that index funds are the\\\\",
        "options to invest in").set_color(BLACK)
        text8.scale(1.3)
        text8.move_to(2.5*UP)
        text9 = TextMobject("There are two ways in which you can invest").set_color(RED)
        text9.scale(1.3)
        text9.move_to(1*UP)

        









        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1), ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.play(FadeOut(thoughtcloud2text1), ReplacementTransform(thoughtcloud2, thoughtcloud1a))
        self.play(Write(thoughtcloud1text1a, run_time=0.5))
        self.play(FadeOut(thoughtcloud1text1a, run_time=0.5))
        self.play(FadeOut(thoughtcloud1a), FadeOut(trees), ReplacementTransform(car1, car2))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(arr1))
        self.play(Write(text3))
        self.play(FadeOut(text1), FadeOut(text3), FadeOut(text2), FadeOut(arr1))
        self.play(Write(text4))
        self.play(GrowFromCenter(know))
        
        self.play(Write(arr2))
        self.play(Write(text5))
        self.play(Write(arr3))
        self.play(Write(text6, run_time=4))
        self.play(FadeOut(text4), FadeOut(know), FadeOut(arr2), FadeOut(text5), FadeOut(arr3), FadeOut(text6))
        self.play(GrowFromCenter(text7))
        self.wait(3)
        self.play(FadeOut(text7))
        self.play(Write(text8, run_time=3))
        self.play(GrowFromCenter(text9))
        self.wait(3)
        inv = ImageMobject("./invr.png").scale(5)
        self.play(FadeOut(text8), FadeIn(inv), FadeOut(text9), FadeOut(image))



        
        corp = ImageMobject("./corp.png").scale(2)
        corp.move_to(2*LEFT+2*DOWN)

        t1 = TextMobject("The first one is through\\\\",
        "an", " AGENT").scale(1.2)
        t1[0].set_color(BLACK)
        t1[1].set_color(BLACK)
        t1[2].set_color(RED)
        t1.move_to(3*UP)

        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(corp, RIGHT, buff=0.1)
        t2 = TextMobject("Charge", " commission ", "on\\\\",
        "your investment").next_to(s2arr1, RIGHT, buff=0.1)
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2[3].set_color(BLACK)

        t2a = TextMobject("Commission depends upon\\\\",
        "agents to agents").set_color(BLACK)
        t2a.next_to(s2arr1, RIGHT, buff=0.1)

        t3 = TextMobject("In this Digital Era").set_color(BLACK)
        t3.scale(1.5)
        t3.move_to(2.5*UP)

        no = ImageMobject("./no.png").scale(2.5)
        no.move_to(2*LEFT+2*DOWN)

        t4 = TextMobject("Not recommended").set_color(BLACK)
        t4.next_to(s2arr1, RIGHT, buff=0.1)

        t5 = TextMobject("There are a lot of disadvantages,\\\\",
        "such as -").set_color(BLACK)
        t5.scale(1.2)
        t5.move_to(3*UP)

        paper = ImageMobject("./paperwork.png")
        paper.move_to(2*LEFT)
        time = ImageMobject("./timec.png")
        time.move_to(2*RIGHT)

        t6 = TextMobject("The commission which is charged and it\\\\",
        "piles up to becomes a huge amount in long term").set_color(BLACK)
        t6.move_to(3*DOWN)

        t7 = TextMobject("The other way is through\\\\",
        "Online Platforms").scale(1.2)
        t7[0].set_color(BLACK)
        t7[1].set_color(RED)
        t7.move_to(2.75*UP)

        grow = ImageMobject("./groww.png")
        upstox = ImageMobject("./upstox.png")
        grow.move_to(3*LEFT)
        upstox.move_to(3*RIGHT)

        dot1 = Dot().set_color(BLACK)
        dot2 = Dot().set_color(BLACK)
        dot1.move_to(3.7*DOWN+2*LEFT)
        dot2.move_to(DOWN+2*LEFT)
        line1 = Line(dot1.get_top(),dot2.get_bottom(),buff=0.1).set_color(BLACK)
       

        t8 = TextMobject("Without Commision").set_color(BLACK)
        t9 = TextMobject("Quite Easy").set_color(BLACK)
        t10 = TextMobject("User Friendly").set_color(BLACK)
        t8.move_to(1.5*DOWN+0.3*RIGHT)
        t9.move_to(2.5*DOWN+0.7*LEFT)
        t10.move_to(3.5*DOWN+0.4*LEFT)

        t11 = TextMobject("These were the 2 methods for investment but now comes the\\\\",
        "main part of choosing the right funds for your investment").set_color(BLACK)
        t11.move_to(2.75*UP)
        t12 = TextMobject("Plenty of").set_color(BLACK)
        t12.move_to(UP+2*LEFT)
        t2arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr2.next_to(t12, RIGHT, buff=0.1)
        t12a = TextMobject("Index Funds").set_color(RED)
        t12a.next_to(t2arr2, RIGHT, buff=0.1)

        t13 = TextMobject("For the right step").set_color(BLACK)
        t13.move_to(3*LEFT)
        t2arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        t2arr3.next_to(t13, RIGHT, buff=0.1)
        t13a = TextMobject("A Little Knowledge").set_color(RED)
        t13a.next_to(t2arr3, RIGHT, buff=0.1)






        self.wait()
        self.play(Write(t1))
        self.play(GrowFromCenter(corp))
        self.play(Write(s2arr1))
        self.play(Write(t2))
        self.play(ReplacementTransform(t2, t2a))
        self.wait(3)
        self.play(FadeOut(t2a), FadeOut(s2arr1), FadeOut(t1))
        self.play(Write(t3))
        self.play(Write(s2arr1))
        self.play(Write(t4))
        self.play(GrowFromCenter(no))
        self.play(FadeOut(no), FadeOut(corp), FadeOut(t3), FadeOut(t4), FadeOut(s2arr1))
        self.play(Write(t5))
        self.play(GrowFromCenter(paper))
        self.play(GrowFromCenter(time))
        self.wait(2)
        self.play(Write(t6, run_time=8))
        self.play(FadeOut(t5), FadeOut(t6), FadeOut(paper), FadeOut(time))
        self.play(Write(t7))
        self.play(GrowFromCenter(grow))
        self.play(GrowFromCenter(upstox))
        self.wait()
        self.play(Write(dot2))
        self.play(Write(line1))
        self.play(Write(dot1))
        self.play(Write(t8))
        self.wait(4)
        self.play(Write(t9))
        self.play(Write(t10))
        self.wait(5.5)
        self.add_sound("./project7a2")
        self.play(FadeOut(t9), FadeOut(t10), FadeOut(t8), FadeOut(dot1), FadeOut(dot2),
        FadeOut(line1), FadeOut(grow), FadeOut(upstox), FadeOut(t7))
        self.play(Write(t11, run_time=7))
        self.play(Write(t12))
        self.play(Write(t2arr2))
        self.play(Write(t12a), Write(t13))
        self.play(Write(t2arr3, run_time=0.5))
        self.play(Write(t13a, run_time=0.5))
        inv2 = ImageMobject("./inva.png").scale(4)
        self.play(FadeOut(t11), FadeIn(inv2), FadeOut(t12), FadeOut(t2arr2), FadeOut(t12a), 
        FadeOut(t13), FadeOut(t13a), FadeOut(t2arr3), FadeOut(inv))


         

        s1 = TextMobject("The first thing before choosing\\\\",
        "the right fund is -").set_color(BLACK)
        s1.move_to(2.5*UP)
        s2 = TextMobject("FUND").set_color(BLACK)
        s2.move_to(1*UP+5*LEFT)
        sarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr1.next_to(s2, RIGHT, buff=0.1)
        s3 = TextMobject("Nifty or\\\\",
        "Sensex").set_color(YELLOW)
        s3.next_to(sarr1, RIGHT, buff=0.1)
        sarr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        sarr2.next_to(s3, RIGHT, buff=0.1)
        s4 = TextMobject("Under DIRECT GROWTH").set_color(BLACK)
        s4.next_to(sarr2, RIGHT, buff=0.1)

        f1 = SurroundingRectangle(s3, buff=0.1)
        f2 = SurroundingRectangle(s4, buff=0.1)
        ft = TextMobject("REMEMBER THESE TERMS!").set_color(BLACK)
        ft.scale(2)
        ft.move_to(0.5*DOWN)

        s5 = TextMobject("The other thing you should keep in mind\\\\",
        "is ", "Expense Ratio ", "and ", "Exit Load")
        s5[0].set_color(BLACK)
        s5[1].set_color(BLACK)
        s5[2].set_color(YELLOW)
        s5[3].set_color(BLACK)
        s5[4].set_color(YELLOW)
        s5.move_to(2.5*UP)

        thinker = ImageMobject("./thinker.png").scale(1.5)
        thinker.move_to(2*DOWN+4*RIGHT)
        tc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        tc.next_to(thinker, UP, buff=0.1)

        tct1 = TextMobject("Now what is\\\\",
        "expense ratio?").set_color(BLACK)
        tct1.scale(0.7)
        tct1.move_to(4*RIGHT+0.9*UP)

        s6 = TextMobject("Charged over your\\\\",
        "investment").set_color(BLACK)
        s6.scale(0.9)
        s3arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash = ImageMobject("./tmoney.png")
        cash.move_to(5*LEFT)
        s3arr1.next_to(cash, RIGHT, buff=0.1)
        s6.next_to(s3arr1, RIGHT, buff=0.1)

        s7 = TextMobject("Lower Expense Ratio").set_color(BLACK)
        s7.scale(0.9)
        s7.move_to(5*LEFT+2*DOWN)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s7, RIGHT, buff=0.1)
        s8 = TextMobject("Higher Returns").set_color(BLACK)
        s8.scale(0.9)
        s8.next_to(s3arr2, RIGHT, buff=0.1)

        s9 = TextMobject("There are various funds having an expense ratio\\\\",
        "of 1-2 percent which is not at all\\\\"
        "Recommended").set_color(BLACK)
        s9.scale(1.3)
        s9.move_to(2.3*UP)
        s10 = TextMobject("These percentages make a huge difference\\\\",
        "in long term").set_color(BLACK)
        s10.next_to(s9, DOWN, buff=1)

        s11 = TextMobject("Always Go for Funds having\\\\",
        "having MIN Expense Ratio").set_color(BLACK)
        s11.scale(1.5)

        tct2 = TextMobject("So what is\\\\",
        "exit load?").set_color(BLACK)
        tct2.scale(0.7)
        tct2.move_to(4*RIGHT+0.9*UP)
        s12 = TextMobject("Exit Load is basically").set_color(BLACK)
        s12.scale(1.5)
        s12.move_to(2.3*UP)
        s6a = TextMobject("Charged while you\\\\",
        "sell off your funds").set_color(BLACK)
        s6a.scale(0.9)
        s3arr1a = Arrow(LEFT,RIGHT).set_color(BLACK)
        cash1 = ImageMobject("./tmoney.png")
        cash1.move_to(5*LEFT)
        s3arr1a.next_to(cash1, RIGHT, buff=0.1)
        s6a.next_to(s3arr1a, RIGHT, buff=0.1)

        s13 = TextMobject("The funds that you've selected must have\\\\",
        "a minimum exit load or even NIL").set_color(BLACK)
        s13.scale(1.3)
        s13.move_to(2.3*UP)

        s14 = TextMobject("NIL exit load").set_color(BLACK)
        s14.scale(0.9)
        s14.move_to(5*LEFT+2*DOWN)
        s3arr4 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr4.next_to(s14, RIGHT, buff=0.1)
        s15 = TextMobject("PREFERRED!").set_color(BLACK)
        s15.scale(0.9)
        s15.next_to(s3arr4, RIGHT, buff=0.1)











        self.wait()
        self.play(Write(s1, run_time=3))
        self.play(Write(s2))
        self.play(Write(sarr1))
        self.play(Write(s3))
        self.play(Write(sarr2))
        self.play(Write(s4))
        self.play(ShowCreation(f1))
        self.play(ShowCreation(f2))
        self.play(GrowFromCenter(ft))
        self.play(FadeOut(ft))
        self.wait(20)
        self.play(GrowFromCenter(ft))
        self.play(FadeOut(ft))
        self.play(FadeOut(sarr1), FadeOut(sarr2), FadeOut(f1),
        FadeOut(f2), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4))
        self.play(Write(s5))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct1))
        self.play(FadeIn(cash))
        self.play(Write(s3arr1))
        self.play(Write(s6))
        self.play(Write(s7))
        self.play(Write(s3arr2))
        self.play(Write(s8))
        self.play(FadeOut(s5), FadeOut(thinker), FadeOut(tc), FadeOut(tct1),
        FadeOut(cash), FadeOut(s6), FadeOut(s3arr1), FadeOut(s7), FadeOut(s8),
        FadeOut(s3arr2))
        self.play(Write(s9, run_time=4.5))
        self.play(Write(s10, run_time=4.5))
        self.play(FadeOut(s9), FadeOut(s10))
        self.play(GrowFromCenter(s11))
        self.wait()
        self.play(FadeOut(s11))
        self.play(FadeInFromDown(thinker))
        self.play(Write(tc))
        self.play(Write(tct2))
        self.play(Write(s12))
        self.play(FadeIn(cash1))
        self.play(Write(s3arr1a))
        self.play(Write(s6a))
        self.play(ReplacementTransform(s12, s13))
        self.play(Write(s14))
        self.play(Write(s3arr4))
        self.play(Write(s15))
        self.wait(2)
        inv3 = ImageMobject("./inv3r.png").scale(4.5)
        self.play(FadeOut(s14), FadeOut(s15), FadeOut(s3arr4), FadeOut(s13), 
        FadeOut(tc), FadeOut(tct2), FadeOut(thinker), FadeOut(cash1), FadeOut(s6a),
        FadeOut(s3arr1a), FadeOut(inv2), FadeIn(inv3))



        
        

        y1 = TextMobject("The other thing you can check before finalising\\\\",
        "your funds is it's").set_color(BLACK)
        y1.move_to(2.3*UP)

        rate = ImageMobject("./rating.png").move_to(3*LEFT)
        yarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        y2 = TextMobject("Higher the rating, more\\\\",
        "reliable is the funds").set_color(BLACK)
        yarr1.next_to(rate, RIGHT, buff=0.1)
        y2.next_to(yarr1, RIGHT, buff=0.1)

        y3 = TextMobject("Some of the ideal index funds\\\\",
        "recommended by our mentors are -").set_color(BLACK)
        y3.move_to(2.3*UP)

        y3a = TextMobject("UTI NIFTY DIRECT GROWTH Index fund").set_color(BLACK)
        y3a.move_to(0.5*UP)
        y3b = TextMobject("HDFC SENSEX DIRECT GROWTH Index fund").set_color(BLACK)
        y3b.move_to(DOWN)

        y4 = TextMobject("Having low expense ratio and NIL exit load").set_color(BLACK)
        y4.move_to(2.5*DOWN)
        y5 = TextMobject("If all the criteria matches with your\\\\",
        "fund then it is ideal for you").set_color(BLACK)
        y5.move_to(2.2*UP)

        y6 = TextMobject("After choosing the right fund").set_color(BLACK)
        y6.move_to(2.3*UP)
        
        y7 = TextMobject("INVEST").set_color(BLACK)
        y7.scale(2)
        y7.move_to(2.3*UP)
        y8a = TextMobject("lump-sum").set_color(BLACK)
        y8a.move_to(4*LEFT)
        fa1 = Arrow(y7.get_bottom(), y8a.get_top(), buff=0.3).set_color(BLACK)
        y8b = TextMobject("SIP").set_color(BLACK)
        y8b.move_to(4*RIGHT)
        fa2 = Arrow(y7.get_bottom(), y8b.get_top(), buff=0.3).set_color(BLACK)
        fa3 = Arrow(UP,DOWN).set_color(BLACK)
        fa4 = Arrow(UP,DOWN).set_color(BLACK)
        fa3.next_to(y8a, DOWN, buff=0.1)
        fa4.next_to(y8b, DOWN, buff=0.1)

        fa3t = TextMobject("directly invest a\\\\"
        "big sum").set_color(BLACK)
        fa3t.next_to(fa3, DOWN, buff=0.1)
        fa4t = TextMobject("means on a fixed period\\\\",
        "an amount of money\\\\" 
        "would be deducted\\\\",
        "from your account").set_color(BLACK)
        fa4t.scale(0.8)
        fa4t.next_to(fa4, DOWN, buff=0.1)

        ff = TextMobject("The SIP option is highly recommended as it buys funds\\\\",
        "in all levels of the market which provides more promising results.").set_color(BLACK)

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

        thoughtcloud2a = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2a.scale(2)
        thoughtcloud2a.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1a = TextMobject("Now after registering\\\\"
        "with your personal\\\\",
        "details you are all\\\\",
        "set to go with your\\\\",
        "ideal funds.").set_color(BLACK)
        thoughtcloud2text1a.scale(0.8)
        thoughtcloud2text1a.move_to(3.5*LEFT+2.3*UP)

        
        thoughtcloud2text1aa = TextMobject("If you have reached till\\\\"
        "here you must have\\\\",
        "developed a financial\\\\",
        "goal and a step\\\\",
        "towards investment.").set_color(BLACK)
        thoughtcloud2text1aa.scale(0.8)
        thoughtcloud2text1aa.move_to(3.5*LEFT+2.3*UP)

        tcf = TextMobject("Be Proud\\\\",
        "Of Yourself!!").set_color(BLACK)
        tcf.scale(1.5)
        tcf.move_to(3.5*LEFT+2.3*UP)

        tcff = TextMobject("Thank You!\\\\",
        "for being\\\\",
        "with us").set_color(BLACK)
        tcff.scale(1.5)
        tcff.move_to(3.5*LEFT+2.3*UP)



        







        self.play(Write(y1, run_time=3))
        self.play(FadeIn(rate))
        self.wait(5)
        self.play(Write(yarr1))
        self.play(Write(y2, run_time=2))
        self.play(ReplacementTransform(y1,y3))
        self.wait(3)
        self.play(FadeOut(rate), FadeOut(yarr1), FadeOut(y2))
        self.play(GrowFromCenter(y3a))
        self.wait(3)
        self.play(GrowFromCenter(y3b))
        self.wait(3)
        self.play(Write(y4))
        self.play(ReplacementTransform(y3,y5))
        self.wait(4)
        self.play(FadeOut(y5), FadeOut(y3a), FadeOut(y3b), FadeOut(y4))
        self.play(Write(y6))
        self.wait(2)
        self.play(ReplacementTransform(y6,y7))
        self.play(GrowArrow(fa1), GrowArrow(fa2))
        self.play(Write(y8a))
        self.play(GrowArrow(fa3))
        self.play(Write(fa3t, run_time=2))
        self.play(Write(y8b))
        self.play(GrowArrow(fa4))
        self.play(Write(fa4t, run_time=6))
        self.wait(4)
        self.play(FadeOut(fa1), FadeOut(fa2), FadeOut(fa3), FadeOut(fa4), FadeOut(fa3t),
        FadeOut(fa4t), FadeOut(y7), FadeOut(y8a), FadeOut(y8b))
        self.play(Write(ff, run_time=8))
        self.play(FadeOut(ff), FadeOut(inv3), FadeIn(image), FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2a))
        self.play(Write(thoughtcloud2text1a, run_time=4))
        self.wait()
        self.play(ReplacementTransform(thoughtcloud2text1a, thoughtcloud2text1aa))
        self.play(FadeOut(thoughtcloud2text1aa, run_time=10))
        self.play(Write(tcf))
        self.play(FadeOut(tcf))
        self.play(Write(tcff))
        self.play(FadeOut(tcff), FadeOut(thoughtcloud2a)) 
        self.play(ReplacementTransform(car1a, car2a))
        self.wait()





        





        self.wait()
        self.add(g)