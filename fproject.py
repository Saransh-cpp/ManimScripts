from manimlib.imports import *
class vidf1(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
         
        g= NumberPlane()

        self.add_sound("fprojecta.m4a")

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
        thoughtcloud2text1 = TextMobject("Welcome back to the\\\\",
        "second episode of\\\\",
        "strategies and tricks\\\\",
        "you can apply to save\\\\",
        "your money").set_color(BLACK)
        
        thoughtcloud2text1.scale(0.7)
        thoughtcloud2text1.move_to(3.5*LEFT+2.3*UP)

        s1t1 = TextMobject("Till now I am sure that you know the importance\\\\",
        "of saving money but your next question would be\\\\",
        "what all can I do to start savings.?").set_color(BLACK)
        s1t1.move_to(2.5*UP)

        s1t2 = TextMobject("The answer is simple first of all").set_color(BLACK)
        s1t2.scale(1.5)
        s1t2.move_to(2.5*UP)

        indi = ImageMobject("./individual.png")
        s1arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s1arr1.next_to(indi, RIGHT, buff=0.1)
        s1arr1t = TextMobject("self motivated").set_color(BLACK)
        s1arr2 = Arrow(RIGHT, LEFT).set_color(BLACK)
        s1arr2.next_to(indi, LEFT, buff=0.1)
        s1arr2t = TextMobject("have a financial\\\\",
        "dream or a\\\\"
        "goal").set_color(BLACK)
        s1arr1t.next_to(s1arr1, RIGHT, buff=0.1)
        s1arr2t.next_to(s1arr2, LEFT, buff=0.1)

        s1tf = TextMobject("Apart from this there are several strategies\\\\",
        "and tricks you can apply to start\\\\",
        "your savings from today.").set_color(BLACK)
        s1tf.move_to(2.5*UP)






        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1), ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1, run_time=9))
        self.play(FadeOut(thoughtcloud2), FadeOut(thoughtcloud2text1), ReplacementTransform(car1, car2))
        self.play(Write(s1t1, run_time=10))
        self.play(FadeOut(s1t1))
        self.play(Write(s1t2, run_time=4))
        self.play(FadeOut(trees))
        self.play(FadeIn(indi))
        self.play(GrowArrow(s1arr1), GrowArrow(s1arr2))
        self.play(Write(s1arr1t, run_time=3))
        self.play(Write(s1arr2t, run_time=3))
        self.play(FadeOut(s1arr1), FadeOut(s1arr2), FadeOut(s1arr1t), FadeOut(s1arr2t), FadeOut(s1t2))
        self.play(Write(s1tf, run_time=9))
        bbg = ImageMobject("./bbg.png")
        budget = ImageMobject("./budget.png")

        bbg.scale(4)
        self.play(FadeIn(bbg), FadeOut(indi), FadeOut(s1tf), FadeOut(image))


        

        s2t1 = TextMobject("Lets start with the first one").set_color(BLACK)
        s2t1.scale(1.5)
        s2t1.move_to(2.5*UP)

        s2t2 = TextMobject("Build yourself").set_color(BLACK)
        s2t2.move_to(2*LEFT)
        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(s2t2, RIGHT, buff=0.1)
        budget.next_to(s2arr1, RIGHT, buff=0.1)

        s2t3 = TextMobject("This chart will consist of all the\\\\",
        "expenses that you spend every month.").set_color(BLACK)
        s2t3.move_to(2*DOWN)
        
        s2t4 = TextMobject("Doing this you will come to know").set_color(BLACK)
        s2t4.scale(1.3)
        s2t4.move_to(2.5*UP)
        mon = ImageMobject("./tmoney.png")
        mon.move_to(2*LEFT)
        monarr = Arrow(LEFT,RIGHT).set_color(BLACK)
        monarr.next_to(mon, RIGHT, buff=0.1)
        s2t5 = TextMobject("left or spend").set_color(BLACK)
        s2t5.next_to(monarr, RIGHT, buff=0.1)

        s2t6 = TextMobject("After that give a look to your expense and budget\\\\"
        "things up,\\\\",
        "that means check if you can").set_color(BLACK)
        s2t6.scale(1.3)
        s2t6.move_to(2.5*UP)

        te1 = TextMobject("Any expense").set_color(BLACK)
        te1.move_to(2*LEFT)
        te2 = TextMobject("Can add a\\\\",
        "cheaper alternative").set_color(BLACK)
        te2.move_to(2*RIGHT)
        no = ImageMobject("./no.png")
        no.move_to(2*LEFT)

        s2tf = TextMobject("So, make a point to save 25-30 percent of your\\\\",
        "salary or pocket money as a student,if not that\\\\",
        "much atleast 20 percent should be marked.").set_color(BLACK)
        s2tf.move_to(2*DOWN)

        s2t = TextMobject("Your next question would be that at \\\\",
        "the end of the month there is no money left \\\\",
        "so how will I save my money?").set_color(BLACK)
        s2t.move_to(2*UP)

        s2t7 = TextMobject("Keep up the\\\\",
        "reserve aside").set_color(BLACK)
        s2t7.move_to(2*LEFT)
        s2t7a = Arrow(LEFT, RIGHT).set_color(BLACK)
        s2t7a.next_to(s2t7, RIGHT, buff=0.1)
        at = TextMobject("Starting period\\\\",
        "of the month").set_color(BLACK)
        at.next_to(s2t7a, RIGHT, buff=0.1)
        s2t8 = TextMobject("This will not only save your money but will\\\\",
        "also give you a financial discipline.").set_color(BLACK)
        s2t8.move_to(2*DOWN)

        s2tff = TextMobject("The next thing you can do is add a").set_color(BLACK)
        s2tff.move_to(2.7*UP)
        s2tff1 = TextMobject("Believe me this helps a lot in your savings!").set_color(BLACK)
        s2tff1.move_to(2*DOWN)
        gul = ImageMobject("./gul.png").move_to(2*LEFT)
        bag = ImageMobject("./moneye.png").move_to(2*RIGHT)














        self.wait(2)
        self.play(Write(s2t1, run_time=4))
        self.play(Write(s2t2))
        self.play(GrowArrow(s2arr1))
        self.play(FadeIn(budget))
        self.play(Write(s2t3, run_time=5))
        self.play(FadeOut(s2t1), FadeOut(s2t2), FadeOut(s2arr1), FadeOut(budget), FadeOut(s2t3))
        self.play(Write(s2t4, run_time=4))
        self.play(FadeIn(mon))
        self.wait()
        self.play(GrowArrow(monarr))
        self.play(Write(s2t5, run_time=5))
        self.play(FadeOut(s2t5), FadeOut(monarr), FadeOut(mon), FadeOut(s2t4))
        self.play(Write(s2t6, run_time=6))
        self.play(GrowFromCenter(te1))
        self.wait()
        self.play(GrowFromCenter(no))
        self.wait(2)
        self.play(GrowFromCenter(te2))
        self.wait(2)
        self.play(Write(s2tf, run_time=15))
        self.play(FadeOut(s2t6), FadeOut(te1), FadeOut(no), FadeOut(s2tf), FadeOut(te2))
        self.play(Write(s2t, run_time=6))
        self.play(Write(s2t7, run_time=4))
        self.wait(2)
        self.play(Write(s2t7a))
        self.wait()
        self.play(Write(at))
        self.wait()
        self.play(Write(s2t8, run_time=8))
        self.play(FadeOut(s2t), FadeOut(s2t7), FadeOut(s2t7a), FadeOut(at), FadeOut(s2t8))
        self.play(Write(s2tff, run_time=4))
        self.play(GrowFromCenter(gul))
        self.play(GrowFromCenter(bag))
        self.wait(4)
        self.play(Write(s2tff1, run_time=6))
        sbg = ImageMobject("./sbg.png").scale(4)
        self.play(FadeIn(sbg), FadeOut(s2tff), FadeOut(s2tff1), FadeOut(gul), FadeOut(bag), FadeOut(bbg))


        

        s3t1 = TextMobject("Remember the proverb").set_color(BLACK)
        s3t1.move_to(2.5*UP)
        s3t1.scale(1.3)
        drop = ImageMobject("./drop.png")
        river = ImageMobject("./river.png")
        drop.move_to(2*LEFT)
        a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        a1.next_to(drop, RIGHT, buff=0.1)
        river.next_to(a1, RIGHT, buff=0.1)

        s3t2 = TextMobject("Adding small amount").set_color(BLACK)
        a2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3t2.move_to(2*DOWN+3*LEFT)
        a2.next_to(s3t2, RIGHT, buff=0.1)
        s3t3 = TextMobject("Gives a big amount").set_color(BLACK)
        s3t3.next_to(a2, RIGHT, buff=0.1)

        s3tf = TextMobject("Adding chillars and\\\\",
        "small amount").set_color(BLACK)
        a3 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3tf.move_to(2*UP+3*LEFT)
        a3.next_to(s3tf, RIGHT, buff=0.1)
        s3tf1 = TextMobject("now being utilised\\\\",
        "as your savings.").set_color(BLACK)
        s3tf1.next_to(a3, RIGHT, buff=0.1)

        s3tff = TextMobject("DOESN'T IT SOUND GREAT?").set_color(BLACK)
        s3tff.scale(1.5)

        s3ta = TextMobject("Like we can do many things to save\\\\",
        "our money but are unaware!").set_color(BLACK)

        s3tb = TextMobject("So, let's move forward to the other\\\\",
        "one that is").set_color(BLACK)
        s3tb.scale(1.3)
        s3tb.move_to(2.7*UP)
        buck = ImageMobject("./bucks.png")
        buck.move_to(2*LEFT+0.5*UP)
        ba = Arrow(LEFT, RIGHT).set_color(BLACK)
        ba.next_to(buck, RIGHT, buff=0.1)
        s3tc = TextMobject("Carry physically").set_color(BLACK)
        s3tc.next_to(ba, RIGHT, buff=0.1)

        buck1 = ImageMobject("./bucks.png")
        no1 = ImageMobject("./no.png")
        buck1.move_to(2*DOWN+2.2*LEFT)
        no1.move_to(2*DOWN+2*LEFT)
        ba1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        ba1.next_to(buck1, RIGHT, buff=0.1)
        s3tc1 = TextMobject("Trend Nowadays").set_color(BLACK)
        s3tc1.next_to(ba1, RIGHT, buff=0.1)

        s3td = TextMobject("Total amount spent by a cashless person is way\\\\",
        "more than a person carrying cash!").set_color(BLACK)
        s3td.move_to(2.7*UP)

        s3te = TextMobject("There’s a simple logic behind it").set_color(BLACK)
        s3te.move_to(2.7*UP)
        buck2 = ImageMobject("./bucks.png")
        buck2.move_to(5*LEFT+UP)
        w1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        w1.next_to(buck2, RIGHT, buff=0.1)
        s3tg = TextMobject("give an impact\\\\",
        "and a thought\\\\",
        "before you spend").set_color(BLACK)
        s3tg.next_to(w1, RIGHT, buff=0.1)
        w2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        w2.next_to(s3tg, RIGHT, buff=0.1)
        s3th = TextMobject("having a physical\\\\"
        "appearance").set_color(BLACK)
        s3th.next_to(w2, RIGHT, buff=0.1)

        s3ti = TextMobject("On the other hand on the digital platforms one just gets\\\\",
        "excited by seeing the offers and end up\\\\"
        "spending their hard earn money.").set_color(BLACK)
        s3ti.move_to(2*DOWN)

        s3tj = TextMobject("This could be achieved by\\\\",
        "making a change in your lifestyle").set_color(BLACK)
        s3tj.move_to(2.7*UP)

        sf = TextMobject("Every weekend\\\\",
        "you go").set_color(BLACK)
        sf.move_to(4*LEFT)
        fa1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        fa1.next_to(sf, RIGHT, buff=0.1)
        sf1 = TextMobject("to some\\\\",
        "hotel").set_color(BLACK)
        sf1.next_to(fa1, RIGHT, buff=0.1)
        fa2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        fa2.next_to(sf1, RIGHT, buff=0.1)
        sf2 = TextMobject("Have your favourite\\\\",
        "food").set_color(BLACK)
        sf2.next_to(fa2, RIGHT, buff=0.1)

        sf3 = TextMobject("BELIEVE ME, THIS WILL WORK").set_color(BLACK)
        sf3.scale(1.5)
        sf3.move_to(2*DOWN)

        ftext = TextMobject("Applying this would not only save your money\\\\",
        "but also makes a step ahead to your discipline.").set_color(BLACK)
        ftext.scale(1.3)
        ftext.move_to(2*UP)
        ftext1 = TextMobject("You can just skip any of your plan\\\\",
        "in a month and there you go.").set_color(BLACK)
        ftext1.scale(1.3)
    



        








        self.play(Write(s3t1, run_time=1.5))
        self.play(FadeIn(drop))
        self.play(Write(a1))
        self.play(FadeIn(river))
        self.play(Write(s3t2, run_time=3))
        self.play(Write(a2))
        self.play(Write(s3t3))
        self.play(FadeOut(s3t1))
        self.play(Write(s3tf, run_time=4))
        self.play(Write(a3))
        self.play(Write(s3tf1, run_time=4))
        self.wait(2)
        self.play(FadeOut(drop), FadeOut(river), FadeOut(a1), FadeOut(s3t2),
        FadeOut(a2), FadeOut(s3t3), FadeOut(s3tf), FadeOut(a3), FadeOut(s3tf1))
        self.play(GrowFromCenter(s3tff))
        self.play(FadeOut(s3tff))
        self.play(Write(s3ta, run_rime=10))
        self.play(FadeOut(s3ta))
        self.play(Write(s3tb, run_time=2))
        self.play(FadeIn(buck))
        self.play(Write(ba))
        self.play(Write(s3tc))
        self.wait(3)
        self.play(FadeIn(buck1))
        self.play(GrowFromCenter(no1))
        self.play(Write(ba1))
        self.play(Write(s3tc1))
        self.wait(6)
        self.play(FadeOut(s3tb))
        self.play(Write(s3td, run_time=9))
        self.play(FadeOut(buck), FadeOut(no1), FadeOut(buck1), FadeOut(s3td),
        FadeOut(ba), FadeOut(ba1), FadeOut(s3tc), FadeOut(s3tc1))
        self.play(Write(s3te, run_time=2))
        self.play(FadeIn(buck2))
        self.wait()
        self.play(Write(w1))
        self.wait()
        self.play(Write(s3tg, run_time=2))
        self.wait()
        self.play(Write(w2))
        self.wait()
        self.play(Write(s3th, run_time=2))
        self.play(Write(s3ti, run_time=15))
        self.wait(10)
        self.play(FadeOut(buck2), FadeOut(w1), FadeOut(w2), FadeOut(s3te),
        FadeOut(s3tg), FadeOut(s3th), FadeOut(s3ti))
        self.play(Write(s3tj, run_time=7))
        self.play(Write(sf))
        self.wait()
        self.play(Write(fa1))
        self.wait()
        self.play(Write(sf1))
        self.wait()
        self.play(Write(fa2))
        self.wait()
        self.play(Write(sf2))
        self.wait(2)
        self.play(GrowFromCenter(sf3))
        self.wait(5)
        self.play(FadeOut(s3tj), FadeOut(sf), FadeOut(sf1), FadeOut(sf2), FadeOut(fa1), FadeOut(fa2), FadeOut(sf3))
        self.play(Write(ftext, run_time=8))
        self.play(Write(ftext1, run_time=8))
        self.wait()
        self.play(FadeOut(ftext), FadeOut(ftext1))


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
        thoughtcloud2text1a = TextMobject("I hope you understood\\\\",
        "the importance\\\\"
        "of savings in one’s life\\\\",
        "that it not only builds you\\\\",
        "wealth but also contribute to\\\\"
        "your discipline,financial goal\\\\"
        "and mony more.").set_color(BLACK)
        
        thoughtcloud2text1a.scale(0.6)
        thoughtcloud2text1a.move_to(3.5*LEFT+2.3*UP)

        tctf1 = TextMobject("These were the strategies and tricks you could apply to save\\\\",
        "your money and if your savings are not enough as to not \\\\",
        "everybody gets a good salary or money don’t worry").set_color(BLACK)
        tctf1.move_to(2.5*UP)

        tctf2 = TextMobject("check out the next episode on earning additional\\\\",
        "income as a student and then you will be crystal\\\\",
        "clear of the facts and start savings.").set_color(BLACK)
        tctf2.move_to(2.5*UP)

        ohyeah = TextMobject("Thank you for being with\\\\",
        "us. Let us meet on the next\\\\",
        "episode of personal finance.").set_color(BLACK)
        ohyeah.scale(0.7)
        ohyeah.move_to(3.5*LEFT+2.3*UP)


        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.play(Write(tctf1, run_time=10))
        self.play(FadeOut(tctf1))
        self.play(Write(tctf2, run_time=10))
        self.play(FadeOut(tctf2))
        self.play(Write(thoughtcloud2a))
        self.play(Write(thoughtcloud2text1a, run_time=10))
        self.wait(8)
        self.play(FadeOut(thoughtcloud2text1a))
        self.play(Write(ohyeah, run_time=6))
        self.wait(3)
        self.play(FadeOut(thoughtcloud2a), FadeOut(ohyeah), ReplacementTransform(car1a, car2a))



        
class vidf2(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
         
        g= NumberPlane()
        self.add_sound("fprojecta.m4a")
        self.wait(51)

        bbg = ImageMobject("./bbg.png")
        budget = ImageMobject("./budget.png")

        bbg.scale(4)

        s2t1 = TextMobject("Lets start with the first one").set_color(BLACK)
        s2t1.scale(1.5)
        s2t1.move_to(2.5*UP)

        s2t2 = TextMobject("Build yourself").set_color(BLACK)
        s2t2.move_to(2*LEFT)
        s2arr1 = Arrow(LEFT,RIGHT).set_color(BLACK)
        s2arr1.next_to(s2t2, RIGHT, buff=0.1)
        budget.next_to(s2arr1, RIGHT, buff=0.1)

        s2t3 = TextMobject("This chart will consist of all the\\\\",
        "expenses that you spend every month.").set_color(BLACK)
        s2t3.move_to(2*DOWN)
        
        s2t4 = TextMobject("Doing this you will come to know").set_color(BLACK)
        s2t4.scale(1.3)
        s2t4.move_to(2.5*UP)
        mon = ImageMobject("./tmoney.png")
        mon.move_to(2*LEFT)
        monarr = Arrow(LEFT,RIGHT).set_color(BLACK)
        monarr.next_to(mon, RIGHT, buff=0.1)
        s2t5 = TextMobject("left or spend").set_color(BLACK)
        s2t5.next_to(monarr, RIGHT, buff=0.1)

        s2t6 = TextMobject("After that give a look to your expense and budget\\\\"
        "things up,\\\\",
        "that means check if you can").set_color(BLACK)
        s2t6.scale(1.3)
        s2t6.move_to(2.5*UP)

        te1 = TextMobject("Any expense").set_color(BLACK)
        te1.move_to(2*LEFT)
        te2 = TextMobject("Can add a\\\\",
        "cheaper alternative").set_color(BLACK)
        te2.move_to(2*RIGHT)
        no = ImageMobject("./no.png")
        no.move_to(2*LEFT)

        s2tf = TextMobject("So, make a point to save 25-30 percent of your\\\\",
        "salary or pocket money as a student,if not that\\\\",
        "much atleast 20 percent should be marked.").set_color(BLACK)
        s2tf.move_to(2*DOWN)

        s2t = TextMobject("Your next question would be that at \\\\",
        "the end of the month there is no money left \\\\",
        "so how will I save my money?").set_color(BLACK)
        s2t.move_to(2*UP)

        s2t7 = TextMobject("Keep up the\\\\",
        "reserve aside").set_color(BLACK)
        s2t7.move_to(2*LEFT)
        s2t7a = Arrow(LEFT, RIGHT).set_color(BLACK)
        s2t7a.next_to(s2t7, RIGHT, buff=0.1)
        at = TextMobject("Starting period\\\\",
        "of the month").set_color(BLACK)
        at.next_to(s2t7a, RIGHT, buff=0.1)
        s2t8 = TextMobject("This will not only save your money but will\\\\",
        "also give you a financial discipline.").set_color(BLACK)
        s2t8.move_to(2*DOWN)

        s2tff = TextMobject("The next thing you can do is add a").set_color(BLACK)
        s2tff.move_to(2.7*UP)
        s2tff1 = TextMobject("Believe me this helps a lot in your savings!").set_color(BLACK)
        s2tff1.move_to(2*DOWN)
        gul = ImageMobject("./gul.png").move_to(2*LEFT)
        bag = ImageMobject("./moneye.png").move_to(2*RIGHT)














        self.play(FadeIn(bbg))
        self.play(Write(s2t1, run_time=4))
        self.play(Write(s2t2))
        self.play(GrowArrow(s2arr1))
        self.play(FadeIn(budget))
        self.play(Write(s2t3, run_time=5))
        self.play(FadeOut(s2t1), FadeOut(s2t2), FadeOut(s2arr1), FadeOut(budget), FadeOut(s2t3))
        self.play(Write(s2t4, run_time=4))
        self.play(FadeIn(mon))
        self.wait()
        self.play(GrowArrow(monarr))
        self.play(Write(s2t5, run_time=5))
        self.play(FadeOut(s2t5), FadeOut(monarr), FadeOut(mon), FadeOut(s2t4))
        self.play(Write(s2t6, run_time=6))
        self.play(GrowFromCenter(te1))
        self.wait()
        self.play(GrowFromCenter(no))
        self.wait(2)
        self.play(GrowFromCenter(te2))
        self.wait(2)
        self.play(Write(s2tf, run_time=15))
        self.play(FadeOut(s2t6), FadeOut(te1), FadeOut(no), FadeOut(s2tf), FadeOut(te2))
        self.play(Write(s2t, run_time=6))
        self.play(Write(s2t7, run_time=4))
        self.wait(2)
        self.play(Write(s2t7a))
        self.wait()
        self.play(Write(at))
        self.wait()
        self.play(Write(s2t8, run_time=8))
        self.play(FadeOut(s2t), FadeOut(s2t7), FadeOut(s2t7a), FadeOut(at), FadeOut(s2t8))
        self.play(Write(s2tff, run_time=4))
        self.play(GrowFromCenter(gul))
        self.play(GrowFromCenter(bag))
        self.wait(4)
        self.play(Write(s2tff1, run_time=6))
        self.play(FadeOut(s2tff), FadeOut(s2tff1), FadeOut(gul), FadeOut(bag), FadeOut(bbg))

class vidf3(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
         
        g= NumberPlane()
        self.add_sound("fprojecta.m4a")
        self.wait(150)

        sbg = ImageMobject("./sbg.png").scale(4)

        s3t1 = TextMobject("Remember the proverb").set_color(BLACK)
        s3t1.move_to(2.5*UP)
        s3t1.scale(1.3)
        drop = ImageMobject("./drop.png")
        river = ImageMobject("./river.png")
        drop.move_to(2*LEFT)
        a1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        a1.next_to(drop, RIGHT, buff=0.1)
        river.next_to(a1, RIGHT, buff=0.1)

        s3t2 = TextMobject("Adding small amount").set_color(BLACK)
        a2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3t2.move_to(2*DOWN+3*LEFT)
        a2.next_to(s3t2, RIGHT, buff=0.1)
        s3t3 = TextMobject("Gives a big amount").set_color(BLACK)
        s3t3.next_to(a2, RIGHT, buff=0.1)

        s3tf = TextMobject("Adding chillars and\\\\",
        "small amount").set_color(BLACK)
        a3 = Arrow(LEFT, RIGHT).set_color(BLACK)
        s3tf.move_to(2*UP+3*LEFT)
        a3.next_to(s3tf, RIGHT, buff=0.1)
        s3tf1 = TextMobject("now being utilised\\\\",
        "as your savings.").set_color(BLACK)
        s3tf1.next_to(a3, RIGHT, buff=0.1)

        s3tff = TextMobject("DOESN'T IT SOUND GREAT?").set_color(BLACK)
        s3tff.scale(1.5)

        s3ta = TextMobject("Like we can do many things to save\\\\",
        "our money but are unaware!").set_color(BLACK)

        s3tb = TextMobject("So, let's move forward to the other\\\\",
        "one that is").set_color(BLACK)
        s3tb.scale(1.3)
        s3tb.move_to(2.7*UP)
        buck = ImageMobject("./bucks.png")
        buck.move_to(2*LEFT+0.5*UP)
        ba = Arrow(LEFT, RIGHT).set_color(BLACK)
        ba.next_to(buck, RIGHT, buff=0.1)
        s3tc = TextMobject("Carry physically").set_color(BLACK)
        s3tc.next_to(ba, RIGHT, buff=0.1)

        buck1 = ImageMobject("./bucks.png")
        no1 = ImageMobject("./no.png")
        buck1.move_to(2*DOWN+2.2*LEFT)
        no1.move_to(2*DOWN+2*LEFT)
        ba1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        ba1.next_to(buck1, RIGHT, buff=0.1)
        s3tc1 = TextMobject("Trend Nowadays").set_color(BLACK)
        s3tc1.next_to(ba1, RIGHT, buff=0.1)

        s3td = TextMobject("Total amount spent by a cashless person is way\\\\",
        "more than a person carrying cash!").set_color(BLACK)
        s3td.move_to(2.7*UP)

        s3te = TextMobject("There’s a simple logic behind it").set_color(BLACK)
        s3te.move_to(2.7*UP)
        buck2 = ImageMobject("./bucks.png")
        buck2.move_to(5*LEFT+UP)
        w1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        w1.next_to(buck2, RIGHT, buff=0.1)
        s3tg = TextMobject("give an impact\\\\",
        "and a thought\\\\",
        "before you spend").set_color(BLACK)
        s3tg.next_to(w1, RIGHT, buff=0.1)
        w2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        w2.next_to(s3tg, RIGHT, buff=0.1)
        s3th = TextMobject("having a physical\\\\"
        "apperance").set_color(BLACK)
        s3th.next_to(w2, RIGHT, buff=0.1)

        s3ti = TextMobject("On the other hand on the digital platforms one just gets\\\\",
        "excited by seeing the offers and end up\\\\"
        "spending their hard earn money.").set_color(BLACK)
        s3ti.move_to(2*DOWN)

        s3tj = TextMobject("This could be achieved by\\\\",
        "making a change in your lifestyle").set_color(BLACK)
        s3tj.move_to(2.7*UP)

        sf = TextMobject("Every weekend\\\\",
        "you go").set_color(BLACK)
        sf.move_to(4*LEFT)
        fa1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        fa1.next_to(sf, RIGHT, buff=0.1)
        sf1 = TextMobject("to some\\\\",
        "hotel").set_color(BLACK)
        sf1.next_to(fa1, RIGHT, buff=0.1)
        fa2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        fa2.next_to(sf1, RIGHT, buff=0.1)
        sf2 = TextMobject("Have your favourite\\\\",
        "food").set_color(BLACK)
        sf2.next_to(fa2, RIGHT, buff=0.1)

        sf3 = TextMobject("BELIEVE ME, THIS WILL WORK").set_color(BLACK)
        sf3.scale(1.5)
        sf3.move_to(2*DOWN)

        ftext = TextMobject("Applying this would not only save your money\\\\",
        "but also makes a step ahead to your discipline.").set_color(BLACK)
        ftext.scale(1.3)
        ftext.move_to(2*UP)
        ftext1 = TextMobject("You can just skip any of your plan\\\\",
        "in a month and there you go.").set_color(BLACK)
        ftext1.scale(1.3)
    



        








        self.play(FadeIn(sbg))
        self.play(Write(s3t1, run_time=3))
        self.play(FadeIn(drop))
        self.play(Write(a1))
        self.play(FadeIn(river))
        self.play(Write(s3t2, run_time=3))
        self.play(Write(a2))
        self.play(Write(s3t3))
        self.play(FadeOut(s3t1))
        self.play(Write(s3tf, run_time=4))
        self.play(Write(a3))
        self.play(Write(s3tf1, run_time=4))
        self.wait(2)
        self.play(FadeOut(drop), FadeOut(river), FadeOut(a1), FadeOut(s3t2),
        FadeOut(a2), FadeOut(s3t3), FadeOut(s3tf), FadeOut(a3), FadeOut(s3tf1))
        self.play(GrowFromCenter(s3tff))
        self.play(FadeOut(s3tff))
        self.play(Write(s3ta, run_rime=6))
        self.play(FadeOut(s3ta))
        self.play(Write(s3tb, run_time=4))
        self.play(FadeIn(buck))
        self.play(Write(ba))
        self.play(Write(s3tc))
        self.wait(3)
        self.play(FadeIn(buck1))
        self.play(GrowFromCenter(no1))
        self.play(Write(ba1))
        self.play(Write(s3tc1))
        self.wait(6)
        self.play(FadeOut(s3tb))
        self.play(Write(s3td, run_time=9))
        self.play(FadeOut(buck), FadeOut(no1), FadeOut(buck1), FadeOut(s3td),
        FadeOut(ba), FadeOut(ba1), FadeOut(s3tc), FadeOut(s3tc1))
        self.play(Write(s3te, run_time=2))
        self.play(FadeIn(buck2))
        self.wait()
        self.play(Write(w1))
        self.wait()
        self.play(Write(s3tg, run_time=2))
        self.wait()
        self.play(Write(w2))
        self.wait()
        self.play(Write(s3th, run_time=2))
        self.play(Write(s3ti, run_time=15))
        self.wait(10)
        self.play(FadeOut(buck2), FadeOut(w1), FadeOut(w2), FadeOut(s3te),
        FadeOut(s3tg), FadeOut(s3th), FadeOut(s3ti))
        self.play(Write(s3tj, run_time=7))
        self.play(Write(sf))
        self.wait()
        self.play(Write(fa1))
        self.wait()
        self.play(Write(sf1))
        self.wait()
        self.play(Write(fa2))
        self.wait()
        self.play(Write(sf2))
        self.wait()
        self.play(GrowFromCenter(sf3))
        self.wait(5)
        self.play(FadeOut(s3tj), FadeOut(sf), FadeOut(sf1), FadeOut(sf2), FadeOut(fa1), FadeOut(fa2), FadeOut(sf3))
        self.play(Write(ftext, run_time=8))
        self.play(Write(ftext1, run_time=8))
        self.wait()
        self.play(FadeOut(ftext), FadeOut(ftext1))






        self.wait()
        self.add(g)

class vidf4(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
         
        g= NumberPlane()

        self.add_sound("fprojecta.m4a")
        self.wait(295)

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
        thoughtcloud2text1a = TextMobject("I hope you understood\\\\",
        "the importance\\\\"
        "of savings in one’s life\\\\",
        "that it not only builds you\\\\",
        "wealth but also contribute to\\\\"
        "your discipline,financial goal\\\\"
        "and mony more.").set_color(BLACK)
        
        thoughtcloud2text1a.scale(0.6)
        thoughtcloud2text1a.move_to(3.5*LEFT+2.3*UP)

        tctf1 = TextMobject("These were the strategies and tricks you could apply to save\\\\",
        "your money and if your savings are not enough as to not \\\\",
        "everybody gets a good salary or money don’t worry").set_color(BLACK)
        tctf1.move_to(2.5*UP)

        tctf2 = TextMobject("check out the next episode on earning additional\\\\",
        "income as a student and then you will be crystal\\\\",
        "clear of the facts and start savings.").set_color(BLACK)
        tctf2.move_to(2.5*UP)

        ohyeah = TextMobject("Thank you for being with\\\\",
        "us. Let us meet on the next\\\\",
        "episode of personal finance.").set_color(BLACK)
        ohyeah.scale(0.7)
        ohyeah.move_to(3.5*LEFT+2.3*UP)


        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.play(Write(tctf1, run_time=10))
        self.play(FadeOut(tctf1))
        self.play(Write(tctf2, run_time=10))
        self.play(FadeOut(tctf2))
        self.play(Write(thoughtcloud2a))
        self.play(Write(thoughtcloud2text1a, run_time=10))
        self.wait(6)
        self.play(FadeOut(thoughtcloud2text1a))
        self.play(Write(ohyeah, run_time=6))
        self.wait(3)
        self.play(FadeOut(thoughtcloud2a), FadeOut(ohyeah), ReplacementTransform(car1a, car2a))










        self.wait()
        self.add(g)
        
        
        





      
