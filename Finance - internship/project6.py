from manimlib.imports import *
class vid5(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project6a.m4a")
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

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject("From the previous\\\\"
        "episode of different\\\\",
        "investment options we\\\\",
        "came to know that").set_color(BLACK)
        thoughtcloud2text1.scale(0.8)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct = TextMobject("Equity provides the\\\\",
        "higest returns, then\\\\",
        "why don't we go for\\\\"
        "equity?").set_color(BLACK)
        tct.scale(0.8)
        tct.move_to(3.5*LEFT+2.3*UP)

        t1 = TextMobject("You would have heard people about").set_color(BLACK)
        t1.scale(1.5)
        t1.move_to(3*UP)

        stockm = ImageMobject("./stockm.png").scale(1.3)
        stockm.move_to(UP+2.5*LEFT)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(stockm, RIGHT, buff=0.1)
        arr1t = TextMobject("High risk and\\\\",
        "losing money").set_color(RED)
        arr1t.next_to(arr1, RIGHT, buff=0.1)

        t2 = TextMobject("But what if I say it's the ", "smartest\\\\",
        "investment option in the list?")
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2.move_to(3*UP)

        t3 = TextMobject("Requires only a bit of Information").set_color(RED)
        t3.scale(1.5)
        t3.move_to(UP)

        sadm = ImageMobject("./sadm.png").scale(1.5)
        sadm.move_to(0.5*UP)
        t4 = TextMobject("Invest in a\\\\",
        "particular\\\\", "company").set_color(RED)
        t5 = TextMobject("Invest for\\\\",
        "a short term").set_color(RED)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.next_to(sadm, RIGHT, buff=0.1)
        t4.next_to(arr2, RIGHT, buff=0.1)
        arr3 = Arrow(RIGHT,LEFT).set_color(BLACK)
        arr3.next_to(sadm, LEFT, buff=0.1)
        t5.next_to(arr3, LEFT, buff=0.1)

        t6 = TextMobject("Invest in").set_color(BLACK)
        t6.scale(1.5)
        t6.move_to(3*UP+2.5*LEFT)
        t7 = TextMobject("Top companies").set_color(RED)
        t7.scale(1.5)
        arr4= Arrow(LEFT, RIGHT).set_color(BLACK)
        arr4.next_to(t6, RIGHT, buff=0.1)
        t7.next_to(arr4, RIGHT, buff=0.1)

        t8 = TextMobject("Having a loss").set_color(RED)
        t8.move_to(UP+2.5*LEFT)
        t9 = TextMobject("Won't be at the top").set_color(BLACK)
        arr5= Arrow(LEFT, RIGHT).set_color(BLACK)
        arr5.next_to(t8, RIGHT, buff=0.1)
        t9.next_to(arr5, RIGHT, buff=0.1)

        corp = ImageMobject("./corp.png").scale(1.5)
        corp.move_to(4*RIGHT+DOWN)
        corpc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpc.scale(1.5)
        corpc.next_to(corp, UP, buff=0.1)
        corpct1 = TextMobject("But then you would\\\\",
        "be thinking that\\\\",
        "investment in all the\\\\",
        "top companies would\\\\",
        "require a huge capital").set_color(BLACK)
        corpct1.scale(0.62)
        corpct1.move_to(4*RIGHT+2.5*UP)

        corpct2 = TextMobject("You can just start\\\\",
        "investing in all the\\\\",
        "top companies with\\\\",
        " RS 100!!!").set_color(BLACK)
        corpct2.scale(0.75)
        corpct2.move_to(4*RIGHT+2.5*UP)

        no = TextMobject("NO!").set_color(RED)
        no.scale(2)
        no.move_to(UP)

        t10 = TextMobject("How?", " Let's come to the point\\\\",
        "where to ", "invest")
        t10[0].set_color(RED)
        t10[1].set_color(BLACK)
        t10[2].set_color(BLACK)
        t10[3].set_color(RED)
        t10.scale(1.2)
        t10.move_to(3*UP)

        if1 = TextMobject("INDEX FUNDS").set_color(RED)
        if1.scale(1.5)
        if1.move_to(UP)


        












        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.wait()
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tct))
        self.wait()
        self.play(FadeOut(thoughtcloud2), FadeOut(tct), ReplacementTransform(car1, car2))
        self.play(FadeOut(trees))
        self.play(Write(t1))
        self.play(FadeInFromDown(stockm))
        self.play(GrowArrow(arr1))
        self.play(Write(arr1t))
        self.play(FadeOut(arr1), FadeOut(arr1t), FadeOut(stockm), FadeOut(t1))
        self.play(Write(t2))
        self.play(GrowFromCenter(t3))
        self.play(FadeOut(t3))
        self.play(FadeInFromDown(sadm))
        self.play(GrowArrow(arr2))
        self.play(GrowArrow(arr3))
        self.play(Write(t4))
        self.play(Write(t5))
        
        self.play(FadeOut(sadm), FadeOut(arr2), FadeOut(arr3), FadeOut(t4), FadeOut(t2), FadeOut(t5))
        self.play(Write(t6))
        self.play(GrowArrow(arr4))
        self.play(Write(t7))
        self.play(Write(t8))
        self.play(GrowArrow(arr5))
        self.play(Write(t9))
        self.play(FadeOut(arr5), FadeOut(arr4), FadeOut(t6), FadeOut(t7), FadeOut(t8), FadeOut(t9))
        self.play(FadeInFromDown(corp))
        self.play(Write(corpc))
        self.play(Write(corpct1))
        self.wait()
        self.play(GrowFromCenter(no))
        self.play(FadeOut(no), FadeOut(corpct1))
        self.play(Write(corpct2))
        self.play(FadeOut(corp), FadeOut(corpc), FadeOut(corpct2))
        self.play(Write(t10))
        self.play(GrowFromCenter(if1))
        bbg = ImageMobject("./bbg.png")
        bbg.scale(4)
        self.play(FadeOut(t10), FadeOut(if1), FadeOut(image), FadeIn(bbg))


        

        s2t1 = TextMobject("So let's understand the", " basics ", "first\\\\",
        "by entering in the world of", " stock market")
        s2t1[0].set_color(BLACK)
        s2t1[1].set_color(RED)
        s2t1[2].set_color(BLACK)
        s2t1[3].set_color(BLACK)
        s2t1[4].set_color(RED)
        s2t1.move_to(3*UP)

        stonk = ImageMobject("./stockm.png")
        stonk.move_to(4*LEFT)
        e = TextMobject("=").set_color(BLACK)
        e.next_to(stonk, RIGHT, buff=0.3)
        vmarket = ImageMobject("./vmarket.png")
        vmarket.next_to(e, RIGHT, buff=0.3)
        p = TextMobject("OR").set_color(BLACK)
        p.next_to(vmarket, RIGHT, buff=0.3)
        cmarket = ImageMobject("./cmarket.png")
        cmarket.next_to(p, RIGHT, buff=0.3)

        s2t2 = TextMobject("Buy", " or ", "Sell").scale(1.5)
        s2t2.move_to(2.5*UP+4*LEFT)
        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(s2t2, RIGHT, buff=0.1)
        s2t3 = TextMobject("Shares", " of a company").scale(1.5)
        s2t3.next_to(s2arr1, RIGHT, buff=0.1)
        s2t2[0].set_color(RED)
        s2t2[1].set_color(BLACK)
        s2t2[2].set_color(RED)
        s2t3[0].set_color(RED)
        s2t3[1].set_color(BLACK)

        s2t4 = TextMobject("We will not go too deep as to how\\\\",
        "how the", " stock market ", "works or functions")
        s2t4[0].set_color(BLACK)
        s2t4[1].set_color(BLACK)
        s2t4[2].set_color(RED)
        s2t4[3].set_color(BLACK)
        s2t4.move_to(3*UP)

        s2t5 = TextMobject("Basic is enough as there are professionals\\\\",
        "studying in depth knowledge about it").set_color(BLACK)
        s2t5.next_to(s2t4, DOWN, buff=0.5)

        s2t6 = TextMobject("Right?, So why do\\\\", "we need to?").set_color(RED)
        s2t6.scale(1.7)
        s2t6.move_to(UP)


        
        

        






        
        self.play(Write(s2t1))
        self.play(GrowFromCenter(stonk))
        self.play(Write(e))
        self.play(GrowFromCenter(vmarket))
        self.play(Write(p))
        self.play(GrowFromCenter(cmarket))
        self.play(FadeOut(s2t1))
        self.play(Write(s2t2))
        self.play(GrowArrow(s2arr1))
        self.play(Write(s2t3))
        self.play(FadeOut(s2t2), FadeOut(s2t3), FadeOut(s2arr1), FadeOut(cmarket), FadeOut(vmarket),
        FadeOut(e), FadeOut(p), FadeOut(stonk))
        self.play(Write(s2t4))
        self.play(Write(s2t5))
        self.play(FadeOut(s2t4))
        self.play(FadeOut(s2t5))
        self.play(Write(s2t6))
        self.play(FadeOut(s2t6))
        fbg = ImageMobject("./fbg.png")
        fbg.scale(5)
        self.play(FadeOut(bbg), FadeIn(fbg))

        
        


        s3t1 = TextMobject("Vegetable Market").set_color(BLACK)
        s3t1.scale(1.7)
        s3t1.move_to(3*UP)

        ram = ImageMobject("./f1.png").scale(2)
        shyam = ImageMobject("./f2.png").scale(2.5)
        shyam.move_to(5*RIGHT+1.8*DOWN)
        ram.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.5*RIGHT+0.5*UP)
        exarr1.move_to(5*RIGHT+UP)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        s3t2 = TextMobject("There were about", " 500 ", " varieties\\\\",
        "of ", "vegetables").scale(1.3)
        s3t2[0].set_color(BLACK)
        s3t2[1].set_color(RED)
        s3t2[2].set_color(BLACK)
        s3t2[3].set_color(BLACK)
        s3t2[4].set_color(RED)
        s3t2.move_to(3*UP)

        exname1a = TextMobject("Top 50 high\\\\",
        "high quality").set_color(BLACK)
        exname1a.scale(0.7)
        exname2a = TextMobject("Top 30 high\\\\",
        "high quality").set_color(BLACK)
        exname2a.scale(0.7)
        exname1a.next_to(exarr, UP, buff=0.1)
        exname2a.next_to(exarr1, UP, buff=0.1)

        s3t3 = TextMobject("And if the", " quality ", "of any vegetable decreases\\\\",
        "they keep on changing with the other", " high\\\\",
        "quality vegetables").scale(1.3)
        s3t3.move_to(2.5*UP)
        s3t3[0].set_color(BLACK)
        s3t3[1].set_color(RED)
        s3t3[2].set_color(BLACK)
        s3t3[3].set_color(BLACK)
        s3t3[4].set_color(RED)
        s3t3[5].set_color(RED)

        s3t4 = TextMobject("Does ", "NOT ", "exceed the list of 30 and 50").scale(1.3)
        s3t4[0].set_color(BLACK)
        s3t4[1].set_color(RED)
        s3t4[2].set_color(BLACK)
        s3t4.move_to(2*UP)

        prof = ImageMobject("./prof.png")
        s3t5 = TextMobject("Quality").set_color(BLACK)
        s3t5.move_to(2*UP+4*LEFT)
        s3arr1 =Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr1.next_to(s3t5, RIGHT, buff=0.1)
        ana = TextMobject("Analysed by").set_color(BLACK)
        ana.scale(0.4)
        ana.next_to(s3arr1, UP, buff=0.1)
        s3t6 = TextMobject("Demand\\\\",
        "Performance\\\\",
        "and analysis").set_color(BLACK)
        s3t6.next_to(s3arr1, RIGHT, buff=0.1)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s3t6, RIGHT, buff=0.1)
        prof.next_to(s3arr2, RIGHT, buff=0.1)

        s3t7 = TextMobject("Now why will I search for one good quality vegetable\\\\",
        "in the whole market consisting of 500 vegetables\\\\",
        "when there are people having the list!!").set_color(BLACK)
        s3t7.move_to(2*UP)

        s3t8 = TextMobject("So in the world of Stock Market").set_color(BLACK)
        s3t8.move_to(3*UP)

        exname1b = TextMobject("Nifty 50").set_color(RED)
        exname2b = TextMobject("Sensex").set_color(RED)
        exname1b.next_to(exarr, UP, buff=0.1)
        exname2b.next_to(exarr1, UP, buff=0.1)

        s3t9 = TextMobject("They are called the index that is the\\\\",
        "representatives of stock market").set_color(BLACK)
        s3t9.move_to(2.5*UP)

        sen = TextMobject("Sensex").set_color(BLACK)
        sen.move_to(UP+1.5*LEFT)
        senarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        senarr1.next_to(sen)
        sen1 = TextMobject("Top 30 companies\\\\",
        "of India").set_color(BLACK)
        sen1.next_to(senarr1, RIGHT, buff=0.1)

        nif = TextMobject("Nifty 50").set_color(BLACK)
        nif.move_to(UP+1.5*LEFT)
        nifarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        nifarr1.next_to(nif)
        nif1 = TextMobject("Top 50 companies\\\\",
        "of India").set_color(BLACK)
        nif1.next_to(nifarr1, RIGHT, buff=0.1)

        s3t10 = TextMobject("After hearing all this wouldn't it be great").set_color(BLACK)
        s3t10.move_to(2.5*UP)
        s3t11 = TextMobject("Invest").set_color(BLACK)
        s3t11.move_to(UP+1.5*LEFT)
        s3a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3a1.next_to(s3t11)
        s3t12 = TextMobject("In whole sensex\\\\",
        "or nifty").set_color(BLACK)
        s3t12.next_to(s3a1)

        s3f = TextMobject("Get best returns with minimum risk!").set_color(BLACK)
        s3f.move_to(2.5*UP)
        














        
        self.play(Write(s3t1))
        self.play(FadeOut(s3t1))
        self.play(FadeInFromDown(ram), FadeInFromDown(shyam))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))
        self.wait()
        self.play(Write(s3t2))
        self.play(GrowArrow(exarr1), FadeIn(exname2a))
        self.play(FadeOut(exarr1), FadeOut(exname2a))
        self.play(GrowArrow(exarr), FadeIn(exname1a))
        self.play(FadeOut(exarr), FadeOut(exname1a))
        self.play(FadeOut(s3t2))
        self.play(Write(s3t3))
        self.play(FadeOut(s3t3))
        self.play(Write(s3t4))
        self.play(FadeOut(s3t4))
        self.play(Write(s3t5))
        self.play(GrowArrow(s3arr1))
        self.play(Write(ana))
        self.play(Write(s3t6))
        self.play(GrowArrow(s3arr2))
        self.play(GrowFromCenter(prof))
        self.play(FadeOut(s3t5), FadeOut(s3arr1), FadeOut(ana), FadeOut(s3t6), 
        FadeOut(s3arr2), FadeOut(prof))
        self.play(Write(s3t7, run_time=4))
        self.play(FadeOut(s3t7))
        self.play(Write(s3t8))
        self.play(GrowArrow(exarr1), FadeIn(exname2b))
        self.play(FadeOut(exarr1), FadeOut(exname2b))
        self.play(GrowArrow(exarr), FadeIn(exname1b))
        self.play(FadeOut(exarr), FadeOut(exname1b))
        self.play(FadeOut(s3t8))
        self.play(Write(s3t9))
        self.play(FadeOut(s3t9))
        self.play(Write(sen))
        self.play(GrowArrow(senarr1))
        self.play(Write(sen1))
        self.play(FadeOut(sen), FadeOut(senarr1), FadeOut(sen1))
        self.play(Write(nif))
        self.play(GrowArrow(nifarr1))
        self.play(Write(nif1))
        self.play(FadeOut(nif), FadeOut(nifarr1), FadeOut(nif1))
        self.play(Write(s3t10))
        self.play(Write(s3t11))
        self.play(GrowArrow(s3a1))
        self.play(Write(s3t12))
        self.play(ReplacementTransform(s3t10, s3f))
        self.play(FadeOut(s3f), FadeOut(s3t11), FadeOut(s3a1), FadeOut(s3t12))
        sbg = ImageMobject("./sbg.png").scale(4)
        self.play(FadeOut(fbg), FadeIn(sbg), FadeOut(ram), FadeOut(shyam))


        
        
        s4t1 = TextMobject("Now let's come to\\\\"
        "Index Funds").set_color(BLACK)
        s4t1.scale(1.3)
        s4t1.move_to(3*UP)

        s4t2 = TextMobject("Investment in\\\\",
        "index funds").set_color(BLACK)
        s4t2.move_to(UP+5*LEFT)
        s4arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s4arr1.next_to(s4t2, RIGHT, buff=0.1)
        s4t3 = TextMobject("Investing in\\\\",
        "the top companies").set_color(BLACK)
        s4t3.next_to(s4arr1, RIGHT, buff=0.1)

        s4t4 = TextMobject("Investing in all\\\\",
        "top companies individually").set_color(BLACK)
        s4t4.move_to(0.5*DOWN+5*LEFT)
        s4arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr2.next_to(s4t4, RIGHT, buff=0.1)
        s4t5 = ImageMobject("./tmoney.png")
        s4t5.next_to(s4arr2, RIGHT, buff=0.1)

        s4t6 = TextMobject("So ,pool your\\\\",
        "money").set_color(BLACK)
        s4t6.move_to(2*DOWN+5*LEFT)
        s4arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr3.next_to(s4t6, RIGHT, buff=0.1)
        s4t7 = TextMobject("To invest in\\\\",
        "these index").set_color(BLACK)
        s4t7.next_to(s4arr3, RIGHT, buff=0.1)

        win = ImageMobject("./winner.png").scale(2)
        win.move_to(2*DOWN)
        s4t8 = TextMobject("Investment in Index Funds is done proportionally").set_color(BLACK)
        s4t8.scale(1.3)
        s4t8.move_to(2.7*UP)

        a1 = Arrow(DOWN, UP).set_color(BLACK)
        a1.scale(0.5)
        a1.move_to(0.5*UP+0.25*RIGHT)
        a1t = TextMobject("More\\\\",
        "investment").set_color(BLACK)
        a1t.scale(0.6)
        a1t.next_to(a1, UP, buff=0.1)

        a2 = Arrow(DOWN, UP).set_color(BLACK)
        a2.move_to(1.5*RIGHT+0.25*DOWN)
        a2.scale(0.5)
        a2t = TextMobject("Less\\\\",
        "investment").set_color(BLACK)
        a2t.scale(0.6)
        a2t.next_to(a2, UP, buff=0.1)








        
        self.play(Write(s4t1))
        self.play(Write(s4t2))
        self.play(Write(s4arr1))
        self.play(Write(s4t3))
        self.play(Write(s4t4))
        self.play(Write(s4arr2))
        self.play(FadeInFromDown(s4t5))
        self.play(Write(s4t6))
        self.play(Write(s4arr3))
        self.play(Write(s4t7))
        self.play(FadeOut(s4t1), FadeOut(s4t2), FadeOut(s4t3), FadeOut(s4t4), FadeOut(s4t5),
        FadeOut(s4t6), FadeOut(s4t7), FadeOut(s4arr1), FadeOut(s4arr2), FadeOut(s4arr3))
        self.play(Write(s4t8))
        self.play(FadeIn(win))
        self.play(GrowArrow(a1), FadeIn(a1t))
        self.play(FadeOut(a1), FadeOut(a1t))
        self.play(GrowArrow(a2), FadeIn(a2t))
        gdp = ImageMobject("./gdp.png")
        gdp.scale(4)
        self.play(FadeOut(a2), FadeIn(gdp), FadeOut(a2t), FadeOut(sbg))


        

        text1 = TextMobject("The other reason why should you choose\\\\",
        "index funds as your investment option\\\\",
        "is because of it's contribution to GDP").set_color(BLACK)
        text1.move_to(2.5*UP)

        text2 = TextMobject("GDP").set_color(BLACK)
        text2.move_to(4*LEFT)
        text3 = TextMobject("Market value\\\\",
        "of").set_color(BLACK)
        la1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la1.next_to(text2, RIGHT, buff=0.1)
        text3.next_to(la1, RIGHT, buff=0.1)
        la1t = TextMobject("Measure of").set_color(BLACK)
        la1t.scale(0.5)
        la1t.next_to(la1, UP, buff=0.1)

        la2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la2.next_to(text3, RIGHT, buff=0.1)
        good = ImageMobject("./good.png")
        good.next_to(la2,RIGHT,buff=0.1)
        

        good1 = ImageMobject("./good.png")
        good1.move_to(2*DOWN+2*LEFT)
        la3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la3.next_to(good1, RIGHT, buff=0.1)
        la3t = TextMobject("Sum total").set_color(BLACK)
        la3t.scale(0.5)
        la3t.next_to(la3, UP, buff=0.1)
        text4 = TextMobject("GDP").set_color(BLACK)
        text4.next_to(la3, RIGHT, buff=0.1)

        text5 = TextMobject("Approx GDP").set_color(BLACK)
        text5.move_to(3*UP+2*LEFT)
        la4 = Arrow(LEFT, RIGHT).set_color(BLACK)
        la4.next_to(text5, RIGHT, buff=0.1)
        text6 = TextMobject("210 lakh crore").set_color(BLACK)
        text6.next_to(la4, RIGHT, buff=0.1)
        text7 = TextMobject("If we talk about the contribution of top\\\\",
        "companies in GDP, it plays a vital role").set_color(BLACK)
        text7.move_to(UP)

        rel = ImageMobject("./reliance.png").scale(1.5)
        rel.move_to(DOWN+3.5*LEFT)
        la5 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la5.next_to(rel, RIGHT, buff=0.1)
        la5t = TextMobject("Contribution").set_color(BLACK)
        la5t.scale(0.5)
        la5t.next_to(la5,UP,buff=0.1)
        text8 = TextMobject("10 lakh crore").set_color(BLACK)
        text8.next_to(la5, RIGHT, buff=0.1)
        text8a = TextMobject("Which is 4-5 percent").set_color(BLACK)
        text8a.next_to(la5, RIGHT, buff=0.1)

        text9 = TextMobject("GDP").set_color(BLACK)
        text9.scale(1.5)
        text9.move_to(2*UP+1.5*LEFT)
        laf = Arrow(LEFT, RIGHT).set_color(BLACK)
        laf.next_to(text9, RIGHT, buff=0.1)
        grow = ImageMobject("./growth.png")
        grow.next_to(laf, RIGHT, buff=0.1)

        text10 = TextMobject("And India is among the top developing countries\\\\",
        "which means Growth is assured!").set_color(BLACK)
        text10.move_to(0.5*UP)
        text11 = TextMobject("So can we say that these top companies plays an\\\\",
        "important role in growth?").set_color(BLACK)
        text11.move_to(DOWN)
        yes = TextMobject("YES!").set_color(RED)
        yes.scale(2)

        corpa = ImageMobject("./corp.png").scale(1.5)
        corpa.move_to(4*LEFT+DOWN)
        corpca = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpca.scale(1.5)
        corpca.next_to(corpa, UP, buff=0.1)
        corpct1a = TextMobject("So now you\\\\",
        "must have understood\\\\",
        "that you get the best\\\\",
        " returns in equity").set_color(BLACK)
        corpct1a.scale(0.62)
        corpct1a.move_to(4*LEFT+2.5*UP)

        corpct2a = TextMobject("And investment in\\\\",
        "index funds is the\\\\",
        "safest and smartest\\\\",
        "option one could go\\\\",
        "for").set_color(BLACK)
        corpct2a.scale(0.68)
        corpct2a.move_to(4*LEFT+2.5*UP)

        textf1 = TextMobject("Let us now check the graph of 'SENSEX' in\\\\",
        "the past 40 years").set_color(BLACK)
        textf1.scale(1.3)
        textf1.move_to(3*UP)

        sensex = ImageMobject("./sensex.png").scale(2)
        textf2 = TextMobject("It's cleary stating that it started from RS 100 in the year\\\\",
        "1980 and has given a high upto RS 42300").set_color(BLACK)
        textf2.move_to(3*DOWN)
        textf3 = TextMobject("So a person who invested his money in a span of minimum 5-10\\\\",
        "years he got high returns").set_color(BLACK)
        textf3.move_to(3*UP)
        textf4 = TextMobject("while short period investments led to\\\\",
        "loses also.").set_color(BLACK)
        textf4.move_to(3*DOWN)

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

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("That was it\\\\",
        "for now, Thank\\\\",
        "you for being\\\\",
        "with us").set_color(BLACK)
        thoughtcloud1text1.scale(0.57)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)
        tct = TextMobject("Let us meet\\\\",
        "in the next\\\\",
        "episode of the\\\\",
        "return analysis").set_color(BLACK)
        tct.scale(0.57)
        tct.move_to(3.5*LEFT+1.25*UP)











        
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(GrowArrow(la1))
        self.play(Write(la1t))
        self.play(Write(text3))
        self.play(Write(la2))
        self.play(FadeInFromDown(good))
        self.play(FadeInFromDown(good1))
        self.play(GrowArrow(la3))
        self.play(Write(la3t))
        self.play(Write(text4))
        self.play(FadeOut(la1), FadeOut(la2), FadeOut(la1t), FadeOut(la3), FadeOut(la3t),
        FadeOut(good), FadeOut(good1), FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.play(Write(text5))
        self.play(GrowArrow(la4))
        self.play(Write(text6))
        self.play(Write(text7))
        self.play(FadeIn(rel))
        self.play(GrowArrow(la5))
        self.play(Write(la5t))
        self.play(Write(text8))
        self.play(ReplacementTransform(text8, text8a))
        self.play(FadeOut(text5), FadeOut(text6), FadeOut(text7), FadeOut(text8a),
        FadeOut(rel), FadeOut(la4), FadeOut(la5), FadeOut(la5t))
        self.play(Write(text9))
        self.play(GrowArrow(laf))
        self.play(FadeIn(grow))
        self.play(Write(text10))
        self.play(Write(text11))
        self.play(FadeOut(text10), FadeOut(text11), FadeOut(laf), FadeOut(grow), FadeOut(text9))
        self.play(GrowFromCenter(yes))
        self.play(FadeOut(yes))
        
        self.play(FadeIn(corpa))
        self.play(Write(corpca))
        self.play(Write(corpct1a))
        self.wait()
        self.play(FadeOut(corpct1a))
        self.play(Write(corpct2a))
        self.play(FadeOut(corpa), FadeOut(corpca), FadeOut(corpct2a))
        self.play(Write(textf1))
        self.play(GrowFromCenter(sensex))
        self.play(Write(textf2))
        self.play(FadeOut(textf1))
        self.play(Write(textf3))
        self.play(FadeOut(textf2))
        self.play(Write(textf4))
        self.play(FadeOut(textf4), FadeOut(textf3), FadeOut(sensex), FadeOut(gdp), FadeIn(image), FadeInFromDown(trees))
        
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1))
        self.play(Write(tct))
        self.wait()
        self.play(FadeOut(thoughtcloud1), FadeOut(tct), ReplacementTransform(car1a, car2a))
        

        



        self.wait()
        self.add(g)

class vid51(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project6a.m4a")
        self.wait(82)

        bbg = ImageMobject("./bbg.png")
        bbg.scale(4)

        s2t1 = TextMobject("So let's understand the", " basics ", "first\\\\",
        "by entering in the world of", " stock market")
        s2t1[0].set_color(BLACK)
        s2t1[1].set_color(RED)
        s2t1[2].set_color(BLACK)
        s2t1[3].set_color(BLACK)
        s2t1[4].set_color(RED)
        s2t1.move_to(3*UP)

        stonk = ImageMobject("./stockm.png")
        stonk.move_to(4*LEFT)
        e = TextMobject("=").set_color(BLACK)
        e.next_to(stonk, RIGHT, buff=0.3)
        vmarket = ImageMobject("./vmarket.png")
        vmarket.next_to(e, RIGHT, buff=0.3)
        p = TextMobject("OR").set_color(BLACK)
        p.next_to(vmarket, RIGHT, buff=0.3)
        cmarket = ImageMobject("./cmarket.png")
        cmarket.next_to(p, RIGHT, buff=0.3)

        s2t2 = TextMobject("Buy", " or ", "Sell").scale(1.5)
        s2t2.move_to(2.5*UP+4*LEFT)
        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(s2t2, RIGHT, buff=0.1)
        s2t3 = TextMobject("Shares", " of a company").scale(1.5)
        s2t3.next_to(s2arr1, RIGHT, buff=0.1)
        s2t2[0].set_color(RED)
        s2t2[1].set_color(BLACK)
        s2t2[2].set_color(RED)
        s2t3[0].set_color(RED)
        s2t3[1].set_color(BLACK)

        s2t4 = TextMobject("We will not go too deep as to how\\\\",
        "how the", " stock market ", "works or functions")
        s2t4[0].set_color(BLACK)
        s2t4[1].set_color(BLACK)
        s2t4[2].set_color(RED)
        s2t4[3].set_color(BLACK)
        s2t4.move_to(3*UP)

        s2t5 = TextMobject("Basic is enough as there are professionals\\\\",
        "studying in depth knowledge about it").set_color(BLACK)
        s2t5.next_to(s2t4, DOWN, buff=0.5)

        s2t6 = TextMobject("Right?, So why do\\\\", "we need to?").set_color(RED)
        s2t6.scale(1.7)
        s2t6.move_to(UP)


        
        

        






        self.play(FadeIn(bbg))
        self.play(Write(s2t1, run_time=5))
        self.play(GrowFromCenter(stonk))
        self.play(Write(e))
        self.play(GrowFromCenter(vmarket))
        self.play(Write(p))
        self.play(GrowFromCenter(cmarket))
        self.play(FadeOut(s2t1))
        self.wait(2)
        self.play(Write(s2t2))
        self.play(GrowArrow(s2arr1))
        self.play(Write(s2t3))
        self.play(FadeOut(s2t2), FadeOut(s2t3), FadeOut(s2arr1), FadeOut(cmarket), FadeOut(vmarket),
        FadeOut(e), FadeOut(p), FadeOut(stonk))
        self.play(Write(s2t4, run_time=5))
        self.play(Write(s2t5, run_time=3))
        self.play(FadeOut(s2t4))
        self.play(FadeOut(s2t5))
        self.play(Write(s2t6, run_time=4))
        self.play(FadeOut(s2t6))
        self.play(FadeOut(bbg))
        
        






        self.wait()
        self.add(g)

class vid52(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project6a.m4a")
        self.wait(114)
        fbg = ImageMobject("./fbg.png")
        fbg.scale(5)
        


        s3t1 = TextMobject("Vegetable Market").set_color(BLACK)
        s3t1.scale(1.7)
        s3t1.move_to(3*UP)

        ram = ImageMobject("./f1.png").scale(2)
        shyam = ImageMobject("./f2.png").scale(2.5)
        shyam.move_to(5*RIGHT+1.8*DOWN)
        ram.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.5*RIGHT+0.5*UP)
        exarr1.move_to(5*RIGHT+UP)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        s3t2 = TextMobject("There were about", " 500 ", " varieties\\\\",
        "of ", "vegetables").scale(1.3)
        s3t2[0].set_color(BLACK)
        s3t2[1].set_color(RED)
        s3t2[2].set_color(BLACK)
        s3t2[3].set_color(BLACK)
        s3t2[4].set_color(RED)
        s3t2.move_to(3*UP)

        exname1a = TextMobject("Top 50 high\\\\",
        "high quality").set_color(BLACK)
        exname1a.scale(0.7)
        exname2a = TextMobject("Top 30 high\\\\",
        "high quality").set_color(BLACK)
        exname2a.scale(0.7)
        exname1a.next_to(exarr, UP, buff=0.1)
        exname2a.next_to(exarr1, UP, buff=0.1)

        s3t3 = TextMobject("And if the", " quality ", "of any vegetable decreases\\\\",
        "they keep on changing with the other", " high\\\\",
        "quality vegetables").scale(1.3)
        s3t3.move_to(2.5*UP)
        s3t3[0].set_color(BLACK)
        s3t3[1].set_color(RED)
        s3t3[2].set_color(BLACK)
        s3t3[3].set_color(BLACK)
        s3t3[4].set_color(RED)
        s3t3[5].set_color(RED)

        s3t4 = TextMobject("Does ", "NOT ", "exceed the list of 30 and 50").scale(1.3)
        s3t4[0].set_color(BLACK)
        s3t4[1].set_color(RED)
        s3t4[2].set_color(BLACK)
        s3t4.move_to(2*UP)

        prof = ImageMobject("./prof.png")
        s3t5 = TextMobject("Quality").set_color(BLACK)
        s3t5.move_to(2*UP+4*LEFT)
        s3arr1 =Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr1.next_to(s3t5, RIGHT, buff=0.1)
        ana = TextMobject("Analysed by").set_color(BLACK)
        ana.scale(0.4)
        ana.next_to(s3arr1, UP, buff=0.1)
        s3t6 = TextMobject("Demand\\\\",
        "Performance\\\\",
        "and analysis").set_color(BLACK)
        s3t6.next_to(s3arr1, RIGHT, buff=0.1)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s3t6, RIGHT, buff=0.1)
        prof.next_to(s3arr2, RIGHT, buff=0.1)

        s3t7 = TextMobject("Now why will I search for one good quality vegetable\\\\",
        "in the whole market consisting of 500 vegetables\\\\",
        "when there are people having the list!!").set_color(BLACK)
        s3t7.move_to(2*UP)

        s3t8 = TextMobject("So in the world of Stock Market").set_color(BLACK)
        s3t8.move_to(3*UP)

        exname1b = TextMobject("Nifty 50").set_color(RED)
        exname2b = TextMobject("Sensex").set_color(RED)
        exname1b.next_to(exarr, UP, buff=0.1)
        exname2b.next_to(exarr1, UP, buff=0.1)

        s3t9 = TextMobject("They are called the index that is the\\\\",
        "representatives of stock market").set_color(BLACK)
        s3t9.move_to(2.5*UP)

        sen = TextMobject("Sensex").set_color(BLACK)
        sen.move_to(UP+1.5*LEFT)
        senarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        senarr1.next_to(sen)
        sen1 = TextMobject("Top 30 companies\\\\",
        "of India").set_color(BLACK)
        sen1.next_to(senarr1, RIGHT, buff=0.1)

        nif = TextMobject("Nifty 50").set_color(BLACK)
        nif.move_to(UP+1.5*LEFT)
        nifarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        nifarr1.next_to(nif)
        nif1 = TextMobject("Top 50 companies\\\\",
        "of India").set_color(BLACK)
        nif1.next_to(nifarr1, RIGHT, buff=0.1)

        s3t10 = TextMobject("After hearing all this wouldn't it be great").set_color(BLACK)
        s3t10.move_to(2.5*UP)
        s3t11 = TextMobject("Invest").set_color(BLACK)
        s3t11.move_to(UP+1.5*LEFT)
        s3a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3a1.next_to(s3t11)
        s3t12 = TextMobject("In whole sensex\\\\",
        "or nifty").set_color(BLACK)
        s3t12.next_to(s3a1)

        s3f = TextMobject("Get best returns with minimum risk!").set_color(BLACK)
        s3f.move_to(2.5*UP)
        














        self.play(FadeIn(fbg))
        self.play(Write(s3t1))
        self.play(FadeOut(s3t1))
        self.play(FadeInFromDown(ram), FadeInFromDown(shyam))
        self.wait(3)
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))
        self.wait()
        self.play(Write(s3t2))
        self.wait(2)
        self.play(GrowArrow(exarr1), FadeIn(exname2a))
        self.play(FadeOut(exarr1), FadeOut(exname2a))
        self.wait(3)
        self.play(GrowArrow(exarr), FadeIn(exname1a))
        self.play(FadeOut(exarr), FadeOut(exname1a))
        self.play(FadeOut(s3t2))
        self.play(Write(s3t3, run_time=7.5))
        self.play(FadeOut(s3t3))
        self.play(Write(s3t4, run_time=4))
        self.play(FadeOut(s3t4))
        self.play(Write(s3t5))
        self.play(GrowArrow(s3arr1))
        self.play(Write(ana))
        self.play(Write(s3t6, run_time=2))
        self.play(GrowArrow(s3arr2))
        self.play(GrowFromCenter(prof))
        self.play(FadeOut(s3t5), FadeOut(s3arr1), FadeOut(ana), FadeOut(s3t6), 
        FadeOut(s3arr2), FadeOut(prof))
        self.play(Write(s3t7, run_time=9))
        self.play(FadeOut(s3t7))
        self.play(Write(s3t8, run_time=2))
        self.wait(2)
        self.play(GrowArrow(exarr1), FadeIn(exname2b))
        self.play(FadeOut(exarr1), FadeOut(exname2b))
        self.wait(2)
        self.play(GrowArrow(exarr), FadeIn(exname1b))
        self.play(FadeOut(exarr), FadeOut(exname1b))
        self.play(FadeOut(s3t8))
        self.play(Write(s3t9, run_time=5))
        self.play(FadeOut(s3t9))
        self.play(Write(sen))
        self.play(GrowArrow(senarr1))
        self.play(Write(sen1, run_time=1.5))
        self.play(FadeOut(sen), FadeOut(senarr1), FadeOut(sen1))
        self.wait()
        self.play(Write(nif))
        self.play(GrowArrow(nifarr1))
        self.play(Write(nif1, run_time=1.5))
        self.play(FadeOut(nif), FadeOut(nifarr1), FadeOut(nif1))
        self.wait(10)
        self.play(Write(s3t10))
        self.play(Write(s3t11))
        self.play(GrowArrow(s3a1))
        self.play(Write(s3t12))
        self.wait(1.5)
        self.play(ReplacementTransform(s3t10, s3f))
        self.wait(1.5)
        self.play(FadeOut(s3f), FadeOut(s3t11), FadeOut(s3a1), FadeOut(s3t12))
        self.play(FadeOut(fbg), FadeOut(ram), FadeOut(shyam))




        

       






        self.wait()
        self.add(g)

class vid53(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()

        self.add_sound("./project6a.m4a")
        self.wait(219)

        sbg = ImageMobject("./sbg.png").scale(4)
        
        s4t1 = TextMobject("Now let's come to\\\\"
        "Index Funds").set_color(BLACK)
        s4t1.scale(1.3)
        s4t1.move_to(3*UP)

        s4t2 = TextMobject("Investment in\\\\",
        "index funds").set_color(BLACK)
        s4t2.move_to(UP+5*LEFT)
        s4arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s4arr1.next_to(s4t2, RIGHT, buff=0.1)
        s4t3 = TextMobject("Investing in\\\\",
        "the top companies").set_color(BLACK)
        s4t3.next_to(s4arr1, RIGHT, buff=0.1)

        s4t4 = TextMobject("Investing in all\\\\",
        "top companies individually").set_color(BLACK)
        s4t4.move_to(0.5*DOWN+5*LEFT)
        s4arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr2.next_to(s4t4, RIGHT, buff=0.1)
        s4t5 = ImageMobject("./tmoney.png")
        s4t5.next_to(s4arr2, RIGHT, buff=0.1)

        s4t6 = TextMobject("So ,pool your\\\\",
        "money").set_color(BLACK)
        s4t6.move_to(2*DOWN+5*LEFT)
        s4arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr3.next_to(s4t6, RIGHT, buff=0.1)
        s4t7 = TextMobject("To invest in\\\\",
        "these index").set_color(BLACK)
        s4t7.next_to(s4arr3, RIGHT, buff=0.1)

        win = ImageMobject("./winner.png").scale(2)
        win.move_to(2*DOWN)
        s4t8 = TextMobject("Investment in Index Funds is done proportionally").set_color(BLACK)
        s4t8.scale(1.3)
        s4t8.move_to(2.7*UP)

        a1 = Arrow(DOWN, UP).set_color(BLACK)
        a1.scale(0.5)
        a1.move_to(0.5*UP+0.25*RIGHT)
        a1t = TextMobject("More\\\\",
        "investment").set_color(BLACK)
        a1t.scale(0.6)
        a1t.next_to(a1, UP, buff=0.1)

        a2 = Arrow(DOWN, UP).set_color(BLACK)
        a2.move_to(1.5*RIGHT+0.25*DOWN)
        a2.scale(0.5)
        a2t = TextMobject("Less\\\\",
        "investment").set_color(BLACK)
        a2t.scale(0.6)
        a2t.next_to(a2, UP, buff=0.1)








        self.play(FadeIn(sbg))
        self.play(Write(s4t1))
        self.play(Write(s4t2))
        self.play(Write(s4arr1))
        self.play(Write(s4t3))
        self.wait()
        self.play(Write(s4t4, run_time=1.5))
        self.play(Write(s4arr2))
        self.wait()
        self.play(FadeInFromDown(s4t5))
        self.wait()
        self.play(Write(s4t6, run_time=1.5))
        self.play(Write(s4arr3))
        self.play(Write(s4t7, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(s4t1), FadeOut(s4t2), FadeOut(s4t3), FadeOut(s4t4), FadeOut(s4t5),
        FadeOut(s4t6), FadeOut(s4t7), FadeOut(s4arr1), FadeOut(s4arr2), FadeOut(s4arr3))
        self.play(Write(s4t8))
        self.wait(2)
        self.play(FadeIn(win))
        self.play(GrowArrow(a1), FadeIn(a1t))
        self.play(FadeOut(a1), FadeOut(a1t))
        self.play(GrowArrow(a2), FadeIn(a2t))
        self.play(FadeOut(a2), FadeOut(a2t))
        self.play(FadeOut(win),FadeOut(s4t8), FadeOut(sbg))




        self.wait()
        self.add(g)

class vid54(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()

        self.add_sound("./project6a.m4a")
        self.wait(251)
        gdp = ImageMobject("./gdp.png")
        gdp.scale(4)
        

        text1 = TextMobject("The other reason why should you choose\\\\",
        "index funds as your investment option\\\\",
        "is because of it's contribution to GDP").set_color(BLACK)
        text1.move_to(2.5*UP)

        text2 = TextMobject("GDP").set_color(BLACK)
        text2.move_to(4*LEFT)
        text3 = TextMobject("Market value\\\\",
        "of").set_color(BLACK)
        la1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la1.next_to(text2, RIGHT, buff=0.1)
        text3.next_to(la1, RIGHT, buff=0.1)
        la1t = TextMobject("Measure of").set_color(BLACK)
        la1t.scale(0.5)
        la1t.next_to(la1, UP, buff=0.1)

        la2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la2.next_to(text3, RIGHT, buff=0.1)
        good = ImageMobject("./good.png")
        good.next_to(la2,RIGHT,buff=0.1)
        

        good1 = ImageMobject("./good.png")
        good1.move_to(2*DOWN+2*LEFT)
        la3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la3.next_to(good1, RIGHT, buff=0.1)
        la3t = TextMobject("Sum total").set_color(BLACK)
        la3t.scale(0.5)
        la3t.next_to(la3, UP, buff=0.1)
        text4 = TextMobject("GDP").set_color(BLACK)
        text4.next_to(la3, RIGHT, buff=0.1)

        text5 = TextMobject("Approx GDP").set_color(BLACK)
        text5.move_to(3*UP+2*LEFT)
        la4 = Arrow(LEFT, RIGHT).set_color(BLACK)
        la4.next_to(text5, RIGHT, buff=0.1)
        text6 = TextMobject("210 lakh crore").set_color(BLACK)
        text6.next_to(la4, RIGHT, buff=0.1)
        text7 = TextMobject("If we talk about the contribution of top\\\\",
        "companies in GDP, it plays a vital role").set_color(BLACK)
        text7.move_to(UP)

        rel = ImageMobject("./reliance.png").scale(1.5)
        rel.move_to(DOWN+3.5*LEFT)
        la5 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la5.next_to(rel, RIGHT, buff=0.1)
        la5t = TextMobject("Contribution").set_color(BLACK)
        la5t.scale(0.5)
        la5t.next_to(la5,UP,buff=0.1)
        text8 = TextMobject("10 lakh crore").set_color(BLACK)
        text8.next_to(la5, RIGHT, buff=0.1)
        text8a = TextMobject("Which is 4-5 percent").set_color(BLACK)
        text8a.next_to(la5, RIGHT, buff=0.1)

        text9 = TextMobject("GDP").set_color(BLACK)
        text9.scale(1.5)
        text9.move_to(2*UP+1.5*LEFT)
        laf = Arrow(LEFT, RIGHT).set_color(BLACK)
        laf.next_to(text9, RIGHT, buff=0.1)
        grow = ImageMobject("./growth.png")
        grow.next_to(laf, RIGHT, buff=0.1)

        text10 = TextMobject("And India is among the top developing countries\\\\",
        "which means Growth is assured!").set_color(BLACK)
        text10.move_to(0.5*UP)
        text11 = TextMobject("So can we say that these top companies plays an\\\\",
        "important role in growth?").set_color(BLACK)
        text11.move_to(DOWN)
        yes = TextMobject("YES!").set_color(RED)
        yes.scale(2)

        corpa = ImageMobject("./corp.png").scale(1.5)
        corpa.move_to(4*LEFT+DOWN)
        corpca = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpca.scale(1.5)
        corpca.next_to(corpa, UP, buff=0.1)
        corpct1a = TextMobject("So now you\\\\",
        "must have understood\\\\",
        "that you get the best\\\\",
        " returns in equity").set_color(BLACK)
        corpct1a.scale(0.62)
        corpct1a.move_to(4*LEFT+2.5*UP)

        corpct2a = TextMobject("And investment in\\\\",
        "index funds is the\\\\",
        "safest and smartest\\\\",
        "option one could go\\\\",
        "for").set_color(BLACK)
        corpct2a.scale(0.68)
        corpct2a.move_to(4*LEFT+2.5*UP)

        textf1 = TextMobject("Let us now check the graph of 'SENSEX' in\\\\",
        "the past 40 years").set_color(BLACK)
        textf1.scale(1.3)
        textf1.move_to(3*UP)

        sensex = ImageMobject("./sensex.png").scale(2)
        textf2 = TextMobject("It's cleary stating that it started from RS 100 in the year\\\\",
        "1980 and has given a high upto RS 42300").set_color(BLACK)
        textf2.move_to(3*DOWN)
        textf3 = TextMobject("So a person who invested his money in a span of minimum 5-10\\\\",
        "years he got high returns").set_color(BLACK)
        textf3.move_to(3*UP)
        textf4 = TextMobject("while short period investments led to\\\\",
        "loses also.").set_color(BLACK)
        textf4.move_to(3*DOWN)

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

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("That was it\\\\",
        "for now, Thank\\\\",
        "you for being\\\\",
        "with us").set_color(BLACK)
        thoughtcloud1text1.scale(0.6)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)
        tct = TextMobject("Let us meet\\\\",
        "in the next\\\\",
        "episode of the\\\\",
        "return analysis").set_color(BLACK)
        tct.scale(0.6)
        tct.move_to(3.5*LEFT+1.25*UP)











        self.play(FadeIn(gdp))
        self.wait(4)
        self.play(Write(text1, run_time=8))
        self.play(Write(text2, run_time=1.5))
        self.play(GrowArrow(la1))
        self.play(Write(la1t))
        self.play(Write(text3, run_time=1.5))
        self.play(Write(la2))
        self.play(FadeInFromDown(good))
        self.wait(4)
        self.play(FadeInFromDown(good1))
        self.play(GrowArrow(la3))
        self.play(Write(la3t))
        self.play(Write(text4))
        self.wait(5)
        self.play(FadeOut(la1), FadeOut(la2), FadeOut(la1t), FadeOut(la3), FadeOut(la3t),
        FadeOut(good), FadeOut(good1), FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.play(Write(text5))
        self.play(GrowArrow(la4))
        self.wait(6)
        self.play(Write(text6, run_time=1.5))
        self.play(Write(text7, run_time=6))
        self.play(FadeIn(rel))
        self.play(GrowArrow(la5))
        self.play(Write(la5t))
        self.wait(3)
        self.play(Write(text8, run_time=2))
        self.play(ReplacementTransform(text8, text8a))
        self.wait(2.5)
        self.play(FadeOut(text5), FadeOut(text6), FadeOut(text7), FadeOut(text8a),
        FadeOut(rel), FadeOut(la4), FadeOut(la5), FadeOut(la5t))
        self.play(Write(text9))
        self.play(GrowArrow(laf))
        self.play(FadeIn(grow))
        self.wait()
        self.play(Write(text10, run_time=3))
        self.wait(1.5)
        self.play(Write(text11, run_time=6))
        self.play(FadeOut(text10, run_time=0.5), FadeOut(text11, run_time=0.5), FadeOut(laf, run_time=0.5), FadeOut(grow, run_time=0.5), FadeOut(text9, run_time=0.5))
        self.play(GrowFromCenter(yes, run_time=0.5))
        self.play(FadeOut(yes, run_time=0.5))
        
        self.play(FadeIn(corpa), Write(corpca))
        self.play(Write(corpct1a, run_time=4.5))
        self.play(FadeOut(corpct1a))
        self.play(Write(corpct2a, run_time=6))
        self.play(FadeOut(corpa), FadeOut(corpca), FadeOut(corpct2a))
        self.play(Write(textf1, run_time=4))
        self.play(GrowFromCenter(sensex))
        self.play(Write(textf2, run_time=10))
        self.play(FadeOut(textf1))
        self.play(Write(textf3, run_time=8))
        self.play(FadeOut(textf2))
        self.play(Write(textf4, run_time=4))
        self.play(FadeOut(textf4, run_time=0.5), FadeOut(textf3, run_time=0.5), FadeOut(sensex, run_time=0.5), FadeOut(gdp, run_time=0.5), FadeIn(image, run_time=0.5), FadeInFromDown(trees, run_time=0.5), ReplacementTransform(cara, car1a))
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1))
        self.play(Write(tct))
        self.wait()
        self.play(FadeOut(thoughtcloud1), FadeOut(tct), ReplacementTransform(car1a, car2a))
        





        self.wait()
        self.add(g)
        
class vid55(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project6a.m4a")
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
        thoughtcloud1text1 = TextMobject("Oh Hi!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject("From the previous\\\\"
        "episode of different\\\\",
        "investment options we\\\\",
        "are familiar with the fact").set_color(BLACK)
        thoughtcloud2text1.scale(0.8)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct = TextMobject("Equity provides the\\\\",
        "higest returns, then\\\\",
        "why don't we go for\\\\"
        "equity?").set_color(BLACK)
        tct.scale(0.8)
        tct.move_to(3.5*LEFT+2.3*UP)

        t1 = TextMobject("You would have heard people about").set_color(BLACK)
        t1.scale(1.5)
        t1.move_to(3*UP)

        stockm = ImageMobject("./stockm.png").scale(1.3)
        stockm.move_to(UP+2.5*LEFT)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.next_to(stockm, RIGHT, buff=0.1)
        arr1t = TextMobject("High risk and\\\\",
        "losing money").set_color(RED)
        arr1t.next_to(arr1, RIGHT, buff=0.1)

        t2 = TextMobject("But what if I say it's the ", "smartest\\\\",
        "investment option in the list?")
        t2[0].set_color(BLACK)
        t2[1].set_color(RED)
        t2[2].set_color(BLACK)
        t2.move_to(3*UP)

        t3 = TextMobject("Requires only a bit of Information").set_color(RED)
        t3.scale(1.5)
        t3.move_to(UP)

        sadm = ImageMobject("./sadm.png").scale(1.5)
        sadm.move_to(0.5*UP)
        t4 = TextMobject("Invest in a\\\\",
        "particular\\\\", "company").set_color(RED)
        t5 = TextMobject("Invest for\\\\",
        "a short term").set_color(RED)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.next_to(sadm, RIGHT, buff=0.1)
        t4.next_to(arr2, RIGHT, buff=0.1)
        arr3 = Arrow(RIGHT,LEFT).set_color(BLACK)
        arr3.next_to(sadm, LEFT, buff=0.1)
        t5.next_to(arr3, LEFT, buff=0.1)

        t6 = TextMobject("Invest in").set_color(BLACK)
        t6.scale(1.5)
        t6.move_to(3*UP+2.5*LEFT)
        t7 = TextMobject("Top companies").set_color(RED)
        t7.scale(1.5)
        arr4= Arrow(LEFT, RIGHT).set_color(BLACK)
        arr4.next_to(t6, RIGHT, buff=0.1)
        t7.next_to(arr4, RIGHT, buff=0.1)

        t8 = TextMobject("Having a loss").set_color(RED)
        t8.move_to(UP+2.5*LEFT)
        t9 = TextMobject("Won't be at the top").set_color(BLACK)
        arr5= Arrow(LEFT, RIGHT).set_color(BLACK)
        arr5.next_to(t8, RIGHT, buff=0.1)
        t9.next_to(arr5, RIGHT, buff=0.1)

        corp = ImageMobject("./corp.png").scale(1.5)
        corp.move_to(4*RIGHT+DOWN)
        corpc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpc.scale(1.5)
        corpc.next_to(corp, UP, buff=0.1)
        corpct1 = TextMobject("But now you might\\\\",
        "be thinking that\\\\",
        "investment in all the\\\\",
        "top companies would\\\\",
        "require a huge capital").set_color(BLACK)
        corpct1.scale(0.62)
        corpct1.move_to(4*RIGHT+2.5*UP)

        corpct2 = TextMobject("You can start\\\\",
        "investing in all\\\\",
        "these companies with\\\\",
        " just RS 100!!!").set_color(BLACK)
        corpct2.scale(0.75)
        corpct2.move_to(4*RIGHT+2.5*UP)

        no = TextMobject("NO!").set_color(RED)
        no.scale(2)
        no.move_to(UP)

        t10 = TextMobject("How?", " Let's come to the point\\\\",
        "where to ", "invest")
        t10[0].set_color(RED)
        t10[1].set_color(BLACK)
        t10[2].set_color(BLACK)
        t10[3].set_color(RED)
        t10.scale(1.2)
        t10.move_to(3*UP)

        if1 = TextMobject("INDEX FUNDS").set_color(RED)
        if1.scale(1.5)
        if1.move_to(UP)


        












        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1), ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1, run_time=4))
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tct, run_time=6))
        self.play(FadeOut(thoughtcloud2), FadeOut(tct), ReplacementTransform(car1, car2))
        self.play(FadeOut(trees))
        self.play(Write(t1, run_time=2))
        self.play(FadeInFromDown(stockm))
        self.play(GrowArrow(arr1))
        self.play(Write(arr1t, run_time=2))
        self.play(FadeOut(arr1), FadeOut(arr1t), FadeOut(stockm), FadeOut(t1))
        self.play(Write(t2, run_time=3))
        self.play(GrowFromCenter(t3))
        self.wait(4)
        self.play(FadeOut(t3))
        self.play(FadeInFromDown(sadm))
        self.wait()
        self.play(GrowArrow(arr2))
        self.play(Write(t4, run_time=2))
        self.play(GrowArrow(arr3))
        self.play(Write(t5, run_time=2))
        
        self.play(FadeOut(sadm), FadeOut(arr2), FadeOut(arr3), FadeOut(t4), FadeOut(t2), FadeOut(t5))
        self.play(Write(t6))
        self.play(GrowArrow(arr4))
        self.play(Write(t7))
        self.play(Write(t8))
        self.play(GrowArrow(arr5))
        self.play(Write(t9))
        self.play(FadeOut(arr5), FadeOut(arr4), FadeOut(t6), FadeOut(t7), FadeOut(t8), FadeOut(t9))
        self.play(FadeInFromDown(corp))
        self.play(Write(corpc))
        self.play(Write(corpct1, run_time=8))
        self.play(GrowFromCenter(no))
        self.wait(3)
        self.play(FadeOut(no), FadeOut(corpct1))
        self.play(Write(corpct2, run_time=5))
        self.play(FadeOut(corp), FadeOut(corpc), FadeOut(corpct2))
        self.wait()
        self.play(Write(t10, run_time=5))
        self.wait(3)
        self.play(GrowFromCenter(if1))
        bbg = ImageMobject("./bbg.png")
        bbg.scale(4)
        self.play(FadeOut(t10), FadeOut(if1), FadeOut(image), FadeIn(bbg))

        

        s2t1 = TextMobject("So let's understand the", " basics ", "first\\\\",
        "by entering in the world of", " stock market")
        s2t1[0].set_color(BLACK)
        s2t1[1].set_color(RED)
        s2t1[2].set_color(BLACK)
        s2t1[3].set_color(BLACK)
        s2t1[4].set_color(RED)
        s2t1.move_to(3*UP)

        stonk = ImageMobject("./stockm.png")
        stonk.move_to(4*LEFT)
        e = TextMobject("=").set_color(BLACK)
        e.next_to(stonk, RIGHT, buff=0.3)
        vmarket = ImageMobject("./vmarket.png")
        vmarket.next_to(e, RIGHT, buff=0.3)
        p = TextMobject("OR").set_color(BLACK)
        p.next_to(vmarket, RIGHT, buff=0.3)
        cmarket = ImageMobject("./cmarket.png")
        cmarket.next_to(p, RIGHT, buff=0.3)

        s2t2 = TextMobject("Buy", " or ", "Sell").scale(1.5)
        s2t2.move_to(2.5*UP+4*LEFT)
        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(s2t2, RIGHT, buff=0.1)
        s2t3 = TextMobject("Shares", " of a company").scale(1.5)
        s2t3.next_to(s2arr1, RIGHT, buff=0.1)
        s2t2[0].set_color(RED)
        s2t2[1].set_color(BLACK)
        s2t2[2].set_color(RED)
        s2t3[0].set_color(RED)
        s2t3[1].set_color(BLACK)

        s2t4 = TextMobject("We will not go too deep as to how\\\\",
        "how the", " stock market ", "works or functions")
        s2t4[0].set_color(BLACK)
        s2t4[1].set_color(BLACK)
        s2t4[2].set_color(RED)
        s2t4[3].set_color(BLACK)
        s2t4.move_to(3*UP)

        s2t5 = TextMobject("Basic knowledge would do good enough as\\\\",
        "we are not professionals studying in depth").set_color(BLACK)
        s2t5.next_to(s2t4, DOWN, buff=0.5)

        s2t6 = TextMobject("Right?, So why do\\\\", "we need to?").set_color(RED)
        s2t6.scale(1.7)
        s2t6.move_to(UP)


        
        

        






        
        self.play(Write(s2t1, run_time=5))
        self.play(GrowFromCenter(stonk))
        self.play(Write(e))
        self.play(GrowFromCenter(vmarket))
        self.play(Write(p))
        self.play(GrowFromCenter(cmarket))
        self.play(FadeOut(s2t1))
        self.wait(2)
        self.play(Write(s2t2))
        self.play(GrowArrow(s2arr1))
        self.play(Write(s2t3))
        self.play(FadeOut(s2t2), FadeOut(s2t3), FadeOut(s2arr1), FadeOut(cmarket), FadeOut(vmarket),
        FadeOut(e), FadeOut(p), FadeOut(stonk))
        self.play(Write(s2t4, run_time=5))
        self.play(Write(s2t5, run_time=3))
        self.play(FadeOut(s2t4))
        self.play(FadeOut(s2t5))
        self.play(Write(s2t6, run_time=4))
        self.play(FadeOut(s2t6))
        fbg = ImageMobject("./fbg.png")
        fbg.scale(5)
        self.play(FadeOut(bbg), FadeIn(fbg))


        
        


        s3t1 = TextMobject("Vegetable Market").set_color(BLACK)
        s3t1.scale(1.7)
        s3t1.move_to(3*UP)

        ram = ImageMobject("./f1.png").scale(2)
        shyam = ImageMobject("./f2.png").scale(2.5)
        shyam.move_to(5*RIGHT+1.8*DOWN)
        ram.move_to(2*RIGHT+2*DOWN)

        exname1 = TextMobject("Ram").set_color(BLACK)
        exname2 = TextMobject("Shyam").set_color(BLACK)
        exarr = Arrow(DOWN,UP).set_color(BLACK)
        exarr1 = Arrow(DOWN,UP).set_color(BLACK)
        exarr.scale(0.5)
        exarr1.scale(0.5)
        exarr.move_to(1.5*RIGHT+0.5*UP)
        exarr1.move_to(5*RIGHT+UP)
        exname1.next_to(exarr, UP, buff=0.1)
        exname2.next_to(exarr1, UP, buff=0.1)

        s3t2 = TextMobject("There were about", " 500 ", " varieties\\\\",
        "of ", "vegetables").scale(1.3)
        s3t2[0].set_color(BLACK)
        s3t2[1].set_color(RED)
        s3t2[2].set_color(BLACK)
        s3t2[3].set_color(BLACK)
        s3t2[4].set_color(RED)
        s3t2.move_to(3*UP)

        exname1a = TextMobject("Top 50 high\\\\",
        "high quality").set_color(BLACK)
        exname1a.scale(0.7)
        exname2a = TextMobject("Top 30 high\\\\",
        "high quality").set_color(BLACK)
        exname2a.scale(0.7)
        exname1a.next_to(exarr, UP, buff=0.1)
        exname2a.next_to(exarr1, UP, buff=0.1)

        s3t3 = TextMobject("And if the", " quality ", "of any vegetable decreases\\\\",
        "they keep on changing with the other", " high\\\\",
        "quality vegetables").scale(1.3)
        s3t3.move_to(2.5*UP)
        s3t3[0].set_color(BLACK)
        s3t3[1].set_color(RED)
        s3t3[2].set_color(BLACK)
        s3t3[3].set_color(BLACK)
        s3t3[4].set_color(RED)
        s3t3[5].set_color(RED)

        s3t4 = TextMobject("Does ", "NOT ", "exceed the list of 30 and 50").scale(1.3)
        s3t4[0].set_color(BLACK)
        s3t4[1].set_color(RED)
        s3t4[2].set_color(BLACK)
        s3t4.move_to(2*UP)

        prof = ImageMobject("./prof.png")
        s3t5 = TextMobject("Quality").set_color(BLACK)
        s3t5.move_to(2*UP+4*LEFT)
        s3arr1 =Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr1.next_to(s3t5, RIGHT, buff=0.1)
        ana = TextMobject("Analysed by").set_color(BLACK)
        ana.scale(0.4)
        ana.next_to(s3arr1, UP, buff=0.1)
        s3t6 = TextMobject("Demand\\\\",
        "Performance\\\\",
        "and analysis").set_color(BLACK)
        s3t6.next_to(s3arr1, RIGHT, buff=0.1)
        s3arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s3arr2.next_to(s3t6, RIGHT, buff=0.1)
        prof.next_to(s3arr2, RIGHT, buff=0.1)

        s3t7 = TextMobject("Now why will I search for one good quality vegetable\\\\",
        "in the whole market consisting of 500 vegetables\\\\",
        "when there are people having the list!!").set_color(BLACK)
        s3t7.move_to(2*UP)

        s3t8 = TextMobject("So in the world of Stock Market").set_color(BLACK)
        s3t8.move_to(3*UP)

        exname1b = TextMobject("Nifty 50").set_color(RED)
        exname2b = TextMobject("Sensex").set_color(RED)
        exname1b.next_to(exarr, UP, buff=0.1)
        exname2b.next_to(exarr1, UP, buff=0.1)

        s3t9 = TextMobject("They are called the index that is the\\\\",
        "representatives of stock market").set_color(BLACK)
        s3t9.move_to(2.5*UP)

        sen = TextMobject("Sensex").set_color(BLACK)
        sen.move_to(UP+1.5*LEFT)
        senarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        senarr1.next_to(sen)
        sen1 = TextMobject("Top 30 companies\\\\",
        "of India").set_color(BLACK)
        sen1.next_to(senarr1, RIGHT, buff=0.1)

        nif = TextMobject("Nifty 50").set_color(BLACK)
        nif.move_to(UP+1.5*LEFT)
        nifarr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        nifarr1.next_to(nif)
        nif1 = TextMobject("Top 50 companies\\\\",
        "of India").set_color(BLACK)
        nif1.next_to(nifarr1, RIGHT, buff=0.1)

        s3t10 = TextMobject("After hearing all this wouldn't it be great").set_color(BLACK)
        s3t10.move_to(2.5*UP)
        s3t11 = TextMobject("Invest").set_color(BLACK)
        s3t11.move_to(UP+1.5*LEFT)
        s3a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3a1.next_to(s3t11)
        s3t12 = TextMobject("In whole sensex\\\\",
        "or nifty").set_color(BLACK)
        s3t12.next_to(s3a1)

        s3f = TextMobject("Get best returns with minimum risk!").set_color(BLACK)
        s3f.move_to(2.5*UP)
        














        
        self.play(Write(s3t1))
        self.play(FadeOut(s3t1))
        self.play(FadeInFromDown(ram), FadeInFromDown(shyam))
        self.play(GrowArrow(exarr), FadeIn(exname1))
        self.play(FadeOut(exarr), FadeOut(exname1))
        self.play(GrowArrow(exarr1), FadeIn(exname2))
        self.play(FadeOut(exarr1), FadeOut(exname2))
        self.wait()
        self.play(Write(s3t2))
        self.wait(2)
        self.play(GrowArrow(exarr1), FadeIn(exname2a))
        self.play(FadeOut(exarr1), FadeOut(exname2a))
        self.wait(3)
        self.play(GrowArrow(exarr), FadeIn(exname1a))
        self.play(FadeOut(exarr), FadeOut(exname1a))
        self.play(FadeOut(s3t2))
        self.play(Write(s3t3, run_time=7.5))
        self.play(FadeOut(s3t3))
        self.play(Write(s3t4, run_time=4))
        self.play(FadeOut(s3t4))
        self.play(Write(s3t5))
        self.play(GrowArrow(s3arr1))
        self.play(Write(ana))
        self.play(Write(s3t6, run_time=2))
        self.play(GrowArrow(s3arr2))
        self.play(GrowFromCenter(prof))
        self.play(FadeOut(s3t5), FadeOut(s3arr1), FadeOut(ana), FadeOut(s3t6), 
        FadeOut(s3arr2), FadeOut(prof))
        self.play(Write(s3t7, run_time=9))
        self.play(FadeOut(s3t7))
        self.play(Write(s3t8, run_time=2))
        self.wait(2)
        self.play(GrowArrow(exarr1), FadeIn(exname2b))
        self.play(FadeOut(exarr1), FadeOut(exname2b))
        self.wait(2)
        self.play(GrowArrow(exarr), FadeIn(exname1b))
        self.play(FadeOut(exarr), FadeOut(exname1b))
        self.play(FadeOut(s3t8))
        self.play(Write(s3t9, run_time=5))
        self.play(FadeOut(s3t9))
        self.play(Write(sen))
        self.play(GrowArrow(senarr1))
        self.play(Write(sen1, run_time=1.5))
        self.play(FadeOut(sen), FadeOut(senarr1), FadeOut(sen1))
        self.wait()
        self.play(Write(nif))
        self.play(GrowArrow(nifarr1))
        self.play(Write(nif1, run_time=1.5))
        self.play(FadeOut(nif), FadeOut(nifarr1), FadeOut(nif1))
        self.wait(10)
        self.play(Write(s3t10))
        self.play(Write(s3t11))
        self.play(GrowArrow(s3a1))
        self.play(Write(s3t12))
        self.wait(1.5)
        self.play(ReplacementTransform(s3t10, s3f))
        self.wait(1.5)
        sbg = ImageMobject("./sbg.png").scale(4)
        self.play(FadeOut(s3f), FadeOut(s3t11), FadeOut(s3a1), FadeOut(s3t12))
        self.play(FadeOut(fbg), FadeIn(sbg), FadeOut(ram), FadeOut(shyam))

        

        
        
        s4t1 = TextMobject("Now let's come to\\\\"
        "Index Funds").set_color(BLACK)
        s4t1.scale(1.3)
        s4t1.move_to(3*UP)

        s4t2 = TextMobject("Investment in\\\\",
        "index funds").set_color(BLACK)
        s4t2.move_to(UP+5*LEFT)
        s4arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s4arr1.next_to(s4t2, RIGHT, buff=0.1)
        s4t3 = TextMobject("Investing in\\\\",
        "the top companies").set_color(BLACK)
        s4t3.next_to(s4arr1, RIGHT, buff=0.1)

        s4t4 = TextMobject("Investing in all\\\\",
        "top companies individually").set_color(BLACK)
        s4t4.move_to(0.5*DOWN+5*LEFT)
        s4arr2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr2.next_to(s4t4, RIGHT, buff=0.1)
        s4t5 = ImageMobject("./tmoney.png")
        s4t5.next_to(s4arr2, RIGHT, buff=0.1)

        s4t6 = TextMobject("So ,pool your\\\\",
        "money").set_color(BLACK)
        s4t6.move_to(2*DOWN+5*LEFT)
        s4arr3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s4arr3.next_to(s4t6, RIGHT, buff=0.1)
        s4t7 = TextMobject("To invest in\\\\",
        "these index").set_color(BLACK)
        s4t7.next_to(s4arr3, RIGHT, buff=0.1)

        win = ImageMobject("./winner.png").scale(2)
        win.move_to(2*DOWN)
        s4t8 = TextMobject("Investment in Index Funds is done proportionally").set_color(BLACK)
        s4t8.scale(1.3)
        s4t8.move_to(2.7*UP)

        a1 = Arrow(DOWN, UP).set_color(BLACK)
        a1.scale(0.5)
        a1.move_to(0.5*UP+0.25*RIGHT)
        a1t = TextMobject("More\\\\",
        "investment").set_color(BLACK)
        a1t.scale(0.6)
        a1t.next_to(a1, UP, buff=0.1)

        a2 = Arrow(DOWN, UP).set_color(BLACK)
        a2.move_to(1.5*RIGHT+0.25*DOWN)
        a2.scale(0.5)
        a2t = TextMobject("Less\\\\",
        "investment").set_color(BLACK)
        a2t.scale(0.6)
        a2t.next_to(a2, UP, buff=0.1)








        
        self.play(Write(s4t1))
        self.play(Write(s4t2))
        self.play(Write(s4arr1))
        self.play(Write(s4t3))
        self.wait()
        self.play(Write(s4t4, run_time=1.5))
        self.play(Write(s4arr2))
        self.wait()
        self.play(FadeInFromDown(s4t5))
        self.wait()
        self.play(Write(s4t6, run_time=1.5))
        self.play(Write(s4arr3))
        self.play(Write(s4t7, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(s4t1), FadeOut(s4t2), FadeOut(s4t3), FadeOut(s4t4), FadeOut(s4t5),
        FadeOut(s4t6), FadeOut(s4t7), FadeOut(s4arr1), FadeOut(s4arr2), FadeOut(s4arr3))
        self.play(Write(s4t8, run_time=3))
        self.wait()
        self.play(FadeIn(win))
        self.play(GrowArrow(a1), FadeIn(a1t))
        self.play(FadeOut(a1), FadeOut(a1t))
        self.play(GrowArrow(a2), FadeIn(a2t))
        self.play(FadeOut(a2), FadeOut(a2t))
        gdp = ImageMobject("./gdp.png")
        gdp.scale(4)
        self.play(FadeOut(win), FadeIn(gdp), FadeOut(s4t8), FadeOut(sbg))



        
        

        text1 = TextMobject("The other reason why should you choose\\\\",
        "index funds as your investment option\\\\",
        "is because of it's contribution to GDP").set_color(BLACK)
        text1.move_to(2.5*UP)

        text2 = TextMobject("GDP").set_color(BLACK)
        text2.move_to(4*LEFT)
        text3 = TextMobject("Market value\\\\",
        "of").set_color(BLACK)
        la1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la1.next_to(text2, RIGHT, buff=0.1)
        text3.next_to(la1, RIGHT, buff=0.1)
        la1t = TextMobject("Measure of").set_color(BLACK)
        la1t.scale(0.5)
        la1t.next_to(la1, UP, buff=0.1)

        la2 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la2.next_to(text3, RIGHT, buff=0.1)
        good = ImageMobject("./good.png")
        good.next_to(la2,RIGHT,buff=0.1)
        

        good1 = ImageMobject("./good.png")
        good1.move_to(2*DOWN+2*LEFT)
        la3 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la3.next_to(good1, RIGHT, buff=0.1)
        la3t = TextMobject("Sum total").set_color(BLACK)
        la3t.scale(0.5)
        la3t.next_to(la3, UP, buff=0.1)
        text4 = TextMobject("GDP").set_color(BLACK)
        text4.next_to(la3, RIGHT, buff=0.1)

        text5 = TextMobject("Approx GDP").set_color(BLACK)
        text5.move_to(3*UP+2*LEFT)
        la4 = Arrow(LEFT, RIGHT).set_color(BLACK)
        la4.next_to(text5, RIGHT, buff=0.1)
        text6 = TextMobject("210 lakh crore").set_color(BLACK)
        text6.next_to(la4, RIGHT, buff=0.1)
        text7 = TextMobject("If we talk about the contribution of top\\\\",
        "companies in GDP, it plays a vital role").set_color(BLACK)
        text7.move_to(UP)

        rel = ImageMobject("./reliance.png").scale(1.5)
        rel.move_to(DOWN+3.5*LEFT)
        la5 = Arrow(LEFT,RIGHT).set_color(BLACK)
        la5.next_to(rel, RIGHT, buff=0.1)
        la5t = TextMobject("Contribution").set_color(BLACK)
        la5t.scale(0.5)
        la5t.next_to(la5,UP,buff=0.1)
        text8 = TextMobject("10 lakh crore").set_color(BLACK)
        text8.next_to(la5, RIGHT, buff=0.1)
        text8a = TextMobject("Which is 4-5 percent").set_color(BLACK)
        text8a.next_to(la5, RIGHT, buff=0.1)

        text9 = TextMobject("GDP").set_color(BLACK)
        text9.scale(1.5)
        text9.move_to(2*UP+1.5*LEFT)
        laf = Arrow(LEFT, RIGHT).set_color(BLACK)
        laf.next_to(text9, RIGHT, buff=0.1)
        grow = ImageMobject("./growth.png")
        grow.next_to(laf, RIGHT, buff=0.1)

        text10 = TextMobject("And India is among the top developing countries\\\\",
        "which means Growth is assured!").set_color(BLACK)
        text10.move_to(0.5*UP)
        text11 = TextMobject("So can we say that these top companies plays an\\\\",
        "important role in growth?").set_color(BLACK)
        text11.move_to(DOWN)
        yes = TextMobject("YES!").set_color(RED)
        yes.scale(2)

        corpa = ImageMobject("./corp.png").scale(1.5)
        corpa.move_to(4*LEFT+DOWN)
        corpca = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpca.scale(1.5)
        corpca.next_to(corpa, UP, buff=0.1)
        corpct1a = TextMobject("So now you\\\\",
        "must have understood\\\\",
        "that you get the best\\\\",
        " returns in equity").set_color(BLACK)
        corpct1a.scale(0.62)
        corpct1a.move_to(4*LEFT+2.5*UP)

        corpct2a = TextMobject("And investment in\\\\",
        "index funds is the\\\\",
        "safest and smartest\\\\",
        "option one could go\\\\",
        "for").set_color(BLACK)
        corpct2a.scale(0.68)
        corpct2a.move_to(4*LEFT+2.5*UP)

        textf1 = TextMobject("Let us now check the graph of 'SENSEX' in\\\\",
        "the past 40 years").set_color(BLACK)
        textf1.scale(1.3)
        textf1.move_to(3*UP)

        sensex = ImageMobject("./sensex.png").scale(2)
        textf2 = TextMobject("It's cleary stating that it started from RS 100 in the year\\\\",
        "1980 and has given a high upto RS 42300").set_color(BLACK)
        textf2.move_to(3*DOWN)
        textf3 = TextMobject("So a person who invested his money in a span of minimum 5-10\\\\",
        "years he got high returns").set_color(BLACK)
        textf3.move_to(3*UP)
        textf4 = TextMobject("while short period investments may\\\\",
        "lead to loss").set_color(BLACK)
        textf4.move_to(3*DOWN)

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

        thoughtcloud1 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud1.move_to(1*UP+3.5*LEFT)
        thoughtcloud1text1 = TextMobject("That was it\\\\",
        "for now, Thank\\\\",
        "you for being\\\\",
        "with us").set_color(BLACK)
        thoughtcloud1text1.scale(0.6)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)
        tct = TextMobject("Let us meet\\\\",
        "in the next\\\\",
        "episode of the\\\\",
        "return analysis").set_color(BLACK)
        tct.scale(0.6)
        tct.move_to(3.5*LEFT+1.25*UP)











        
        self.wait(6)
        self.play(Write(text1, run_time=8))
        self.play(Write(text2, run_time=1.5))
        self.play(GrowArrow(la1))
        self.play(Write(la1t))
        self.play(Write(text3, run_time=1.5))
        self.play(Write(la2))
        self.play(FadeInFromDown(good))
        self.wait(4)
        self.play(FadeInFromDown(good1))
        self.play(GrowArrow(la3))
        self.play(Write(la3t))
        self.play(Write(text4))
        self.wait(5)
        self.play(FadeOut(la1), FadeOut(la2), FadeOut(la1t), FadeOut(la3), FadeOut(la3t),
        FadeOut(good), FadeOut(good1), FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.play(Write(text5))
        self.play(GrowArrow(la4))
        self.wait(6)
        self.play(Write(text6, run_time=1.5))
        self.play(Write(text7, run_time=6))
        self.play(FadeIn(rel))
        self.play(GrowArrow(la5))
        self.play(Write(la5t))
        self.wait(3)
        self.play(Write(text8, run_time=2))
        self.play(ReplacementTransform(text8, text8a))
        self.wait(2.5)
        self.play(FadeOut(text5), FadeOut(text6), FadeOut(text7), FadeOut(text8a),
        FadeOut(rel), FadeOut(la4), FadeOut(la5), FadeOut(la5t))
        self.play(Write(text9))
        self.play(GrowArrow(laf))
        self.play(FadeIn(grow))
        self.wait()
        self.play(Write(text10, run_time=3))
        self.wait(1.5)
        self.play(Write(text11, run_time=6))
        self.play(FadeOut(text10, run_time=0.5), FadeOut(text11, run_time=0.5), FadeOut(laf, run_time=0.5), FadeOut(grow, run_time=0.5), FadeOut(text9, run_time=0.5))
        self.play(GrowFromCenter(yes, run_time=0.5))
        self.play(FadeOut(yes, run_time=0.5))
        
        self.play(FadeIn(corpa), Write(corpca))
        self.play(Write(corpct1a, run_time=4.5))
        self.play(FadeOut(corpct1a))
        self.play(Write(corpct2a, run_time=6))
        self.play(FadeOut(corpa), FadeOut(corpca), FadeOut(corpct2a))
        self.play(Write(textf1, run_time=4))
        self.play(GrowFromCenter(sensex))
        self.play(Write(textf2, run_time=10))
        self.play(FadeOut(textf1))
        self.play(Write(textf3, run_time=8))
        self.play(FadeOut(textf2))
        self.play(Write(textf4, run_time=4))
        self.play(FadeOut(textf4, run_time=0.5), FadeOut(textf3, run_time=0.5), FadeOut(sensex, run_time=0.5), FadeOut(gdp, run_time=0.5), FadeIn(image, run_time=0.5), FadeInFromDown(trees, run_time=0.5), ReplacementTransform(cara, car1a))
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1))
        self.play(Write(tct))
        self.wait()
        self.play(FadeOut(thoughtcloud1), FadeOut(tct), ReplacementTransform(car1a, car2a))
        

