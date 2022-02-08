from manimlib.imports import *
class vid3(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
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
        thoughtcloud1text1 = TextMobject("Hi again!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome\\\\"
        "to the episode\\\\",
        "ways to earn\\\\",
        "additional income").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct1 = TextMobject("Till now we had\\\\",
        "learnt how to save\\\\",
        "money and why should\\\\"
        "you do this").set_color(BLACK)
        tct1.move_to(3.5*LEFT+2.5*UP)
        tct1.scale(0.8)


        gard = ImageMobject("./vid3scene.png")
        gard.scale(6.5)
        gard.move_to(2*UP)

        s1t1 = TextMobject("Not everyone gets the same amount\\\\",
        "of money or just they want to earn\\\\",
        "some amount for a better future").set_color(BLACK)
        s1t2 = TextMobject("So, we will share 9 ways so that\\\\",
        "you can earn money.").set_color(BLACK)
        s1t3 = TextMobject("It's not just the money\\\\",
        "you can diversify your knowledge \\\\",
        "skill and work experience too").set_color(BLACK)
        s1t1.move_to(3*LEFT+2.5*UP)
        s1t2.move_to(3*LEFT+3*UP)
        s1t3.move_to(3*LEFT+2.5*UP)
        
        ft1 = TextMobject("1. FreeLancing!").set_color(RED)
        ft1.move_to(3*UP)
        ft1.scale(2)
        ft2 = TextMobject("Freelancing"," is \\\\" 
        "where you do ","not\\\\", 
        "work for any\\\\",
        "specific organization\\\\"
        "or company").set_color(BLACK)
        ft2.scale(0.75)
        ft2.move_to(4*RIGHT+2.7*UP)

        client = ImageMobject("./client.png").scale(2)
        no = ImageMobject("./no.png").scale(2.5)
        client.move_to(3*LEFT+2*DOWN)
        no.move_to(3*LEFT+2*DOWN)

        buck = ImageMobject("./bucks.png")
        nine = ImageMobject("./nine.png")
        nine.move_to(3*LEFT)
        buck.move_to(3*RIGHT)
        barrn = Arrow(nine.get_right(), buck.get_left(), buff=0.1).set_color(BLACK)

        workex = ImageMobject("./workex.png").scale(1.5)
        workex.move_to(3*RIGHT+DOWN)
        skill = ImageMobject('./skill.png').scale(1.5)
        skill.move_to(DOWN)
        know = ImageMobject("./know.png").scale(1.5)
        know.move_to(3*LEFT+DOWN)




        corp =ImageMobject("./corp.png")
        corp.scale(2)
        corp.move_to(4*RIGHT+2*DOWN)
        corpc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpc.scale(2)
        corpc.next_to(corp, UP, buff=0.1)

        ft3 = TextMobject("You just have to\\\\",
        "do specific projects\\\\",
        "and get paid for it").set_color(BLACK)
        
        ft3.move_to(4*RIGHT+2.7*UP)

        desk = ImageMobject("./desk.png")
        m = TextMobject("Money").set_color(BLACK)
        m.move_to(3*LEFT+2*DOWN)
        
        desk.scale(1.5)
        desk.move_to(3*LEFT+2*UP)
        darrm = Arrow(desk.get_bottom(), m.get_top(), buff=0.1).set_color(BLACK)
        

        ft4 = TextMobject("Gain experience and make it\\\\",
        "your full time job").set_color(BLACK)
        fulltime = ImageMobject("./fulltime.png")
        fulltime.scale(2.5)
        fulltime.move_to(3*LEFT)
        ft4.move_to(3*LEFT+3*DOWN)
        ftf = TextMobject("Some of the\\\\",
        "trustworthy\\\\",
        "websites\\\\",
        "are -").set_color(BLACK)
        
        ftf.move_to(4*RIGHT+2.7*UP)
        freelance = ImageMobject("./freelance.png")
        wb1 = TextMobject("www.freelancer.in").set_color(BLACK)
        freelance.scale(2)
        freelance.move_to(3*LEFT+2*DOWN)
        wb1.next_to(freelance, UP, buff=0.1)
        upwork = ImageMobject("./upwork.png")
        upwork.move_to(3*LEFT+2*UP)
        wb2 = TextMobject("www.upwork.com").set_color(BLACK)
        wb2.next_to(upwork, UP, buff=0.01)













        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.wait(0.5)
        self.play(Write(thoughtcloud1))
        self.play(Write(thoughtcloud1text1))
        self.wait()
        self.play(ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(FadeOut(thoughtcloud1text1))
        self.play(Write(thoughtcloud2text1))
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tct1))
        self.wait()
        self.play(FadeOut(thoughtcloud2), FadeOut(tct1), ReplacementTransform(car1, car2))
        self.play(FadeOut(image), FadeOut(trees))
        self.play(FadeInFromDown(gard))
        
        self.wait()
        self.play(Write(s1t1))
        self.play(FadeOut(s1t1))
        self.play(AnimationGroup(Write(s1t2), FadeIn(nine), GrowArrow(barrn), FadeIn(buck), lag_ratio=0.5))
        self.play(FadeOut(s1t2), FadeOut(nine), FadeOut(barrn), FadeOut(buck))
        self.play(AnimationGroup(Write(s1t3),FadeIn(know), FadeIn(skill), FadeIn(workex), lag_ratio=0.5))
        self.play(FadeOut(s1t3), FadeOut(know), FadeOut(skill), FadeOut(workex))
        self.play(AnimationGroup(Write(ft1)))
        self.play(FadeOut(ft1))
        self.play(FadeInFromDown(corp))
        self.play(Write(corpc))
        self.play(Write(ft2))
        self.play(FadeInFromDown(client))
        self.play(GrowFromCenter(no))
        self.play(FadeOut(ft2), FadeOut(client), FadeOut(no))
        self.play(Write(ft3))
        self.play(FadeInFromDown(desk))
        self.play(GrowArrow(darrm))
        self.play(Write(m))
        self.play(FadeOut(m), FadeOut(darrm), FadeOut(desk))
        self.play(FadeIn(fulltime))
        self.play(Write(ft4))
        self.play(FadeOut(fulltime), FadeOut(ft4), FadeOut(ft3))
        self.play(Write(ftf))
        self.play(FadeInFromDown(freelance))
        self.play(Write(wb1))
        self.play(FadeInFromDown(upwork))
        self.play(Write(wb2))
        self.play(FadeOut(wb1), FadeOut(wb2), FadeOut(freelance), FadeOut(upwork),
        FadeOut(ftf), FadeOut(gard), FadeOut(corp), FadeOut(corpc))

        classr = ImageMobject("./class.png").move_to(DOWN)
        classr.scale(5)
        

        tt1 = TextMobject("2. HomeTuitions").set_color(RED)
        tt1.scale(2)
        tt1.move_to(3*UP)

        tt2 = TextMobject("Sharing your knowledge").set_color(BLACK)
        tt3 = ImageMobject("./tmoney.png")
        tt2.move_to(3*UP+3*LEFT)
        tt3.move_to(3*UP+3*RIGHT)
        tarrt = Arrow(tt2.get_right(), tt3.get_left(), buff=0.1).set_color(BLACK)
        
        tt4 = TextMobject("Do it").set_color(BLACK)
        tt4.scale(2)
        tt4.move_to(3*UP)
        or1 = TextMobject("or").set_color(BLACK)
        or1.scale(2)
        offline = ImageMobject("./tuition.png")
        offline.scale(2.5)
        offline.move_to(3*LEFT)
        online = ImageMobject("./onlinet.png")
        online.scale(2)
        online.move_to(3*RIGHT)

        ttf = TextMobject("And in this situation of covid-19\\\\",
        "it is a good opportunity for one to provide\\\\",
        "tuitions as everyone is surfing online now!").set_color(BLACK)
        ttf.move_to(3*UP)
        






        self.play(Write(tt1))
        self.play(FadeIn(classr))
        self.play(FadeOut(tt1))
        self.play(Write(tt2))
        self.play(GrowArrow(tarrt))
        self.play(GrowFromCenter(tt3))
        self.play(FadeOut(tt2), FadeOut(tt3), FadeOut(tarrt))
        self.play(Write(tt4))
        self.play(GrowFromCenter(offline))
        self.play(Write(or1))
        self.play(GrowFromCenter(online))
        self.play(FadeOut(or1), FadeOut(offline), FadeOut(online), Write(ttf), FadeOut(tt4))
        self.wait()
        ibg = ImageMobject("./ibg.png")
        ibg.scale(5)
        self.play(FadeOut(ttf), FadeOut(classr), FadeInFromDown(ibg))

        it1 = TextMobject("3. InternShip").set_color(RED)
        it1.scale(2)
        it1.move_to(3*UP)
        

        i = TextMobject("You can be an intern in any\\\\",
        "company or organization").set_color(BLACK)
        i.move_to(2.5*UP)

        intern1 = ImageMobject("./intern.png").scale(2)
        intern1.move_to(3*LEFT+2*DOWN)

        it2 = TextMobject("You can be an intern in\\\\",
        "any field such as").set_color(BLACK)
        it2.scale(1.5)
        it2.move_to(2.5*UP)

        iacc = ImageMobject("./iacc.png")
        iacc.move_to(4*RIGHT+UP)
        idesign = ImageMobject("./idesign.png")
        idesign.move_to(4*RIGHT+2*DOWN)

        if1 = TextMobject("And Many\\\\",
        "MORE!").set_color(RED)
        if1.scale(2)
        if1.move_to(2.5*UP)
        if2 = TextMobject("In this field you can explore\\\\",
        "and gain experience which will help you\\\\",
        "build your dreams").set_color(BLACK)
        if2.move_to(2.5*UP)

        workerf = ImageMobject("./workerf.png")
        workerf.scale(2.5)
        workerf.move_to(3*LEFT+2*DOWN)
        arr = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr.next_to(workerf)
        imoney = ImageMobject("./imoney.png")
        imoney.scale(2)
        imoney.next_to(arr, RIGHT, buff=0.1)






        
        self.play(Write(it1))
        self.wait()
        self.play(FadeOut(it1))
        self.play(Write(i))
        self.play(FadeOut(i))
        self.play(FadeInFromDown(intern1), Write(it2))
        self.play(GrowFromCenter(iacc))
        self.play(GrowFromCenter(idesign))
        self.play(ReplacementTransform(it2, if1))
        self.play(FadeOut(intern1), FadeOut(if1), FadeOut(iacc), FadeOut(idesign))
        self.play(Write(if2))
        self.play(FadeIn(workerf))
        self.play(GrowArrow(arr))
        self.play(FadeIn(imoney))
        air = ImageMobject("./airport.png")
        air.scale(4)
        self.play(FadeInFromDown(air), FadeOut(workerf), FadeOut(imoney), FadeOut(arr), FadeOut(if2), FadeOut(ibg))

        ta1 = TextMobject("4. Translation Services").set_color(RED)
        ta1.scale(1.5)
        ta1.move_to(2.5*UP)

        

        ta2 = TextMobject("If you know any regional language\\\\",
        "you can perform this service").set_color(BLACK)
        ta2.move_to(3*UP)

        company = ImageMobject("./company.png")
        company.move_to(5*LEFT+UP)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.scale(0.5)
        arr1.next_to(company, RIGHT, buff=0.1)
        arr1t = TextMobject("Switching their content\\\\",
        "to regional languages").set_color(BLACK)
        arr1t.next_to(arr1, buff=0.1)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.scale(0.5)
        arr2.next_to(arr1t, RIGHT, buff=0.1)
        local = ImageMobject("./local1.png")
        local.next_to(arr2, RIGHT, buff=0.1)
        trans = ImageMobject("./translate.png")
        trans.move_to(2*LEFT)
        transtext = TextMobject("Freelancing too!").set_color(BLACK)
        a = Arrow(LEFT,RIGHT).set_color(BLACK)
        a.scale(0.5)
        a.next_to(trans, RIGHT, buff=0.1)
        transtext.next_to(a, RIGHT, buff=0.1)







        
        self.play(Write(ta1))
        self.play(FadeOut(ta1))
        self.play(Write(ta2))
        self.play(FadeIn(company))
        self.play(GrowArrow(arr1))
        self.play(Write(arr1t))
        self.play(GrowArrow(arr2))
        self.play(FadeIn(local))
        self.play(FadeOut(arr1), FadeOut(arr2), FadeOut(local), FadeOut(arr1t),
        FadeOut(company))
        self.play(FadeInFromDown(trans))
        self.play(GrowArrow(a))
        self.play(Write(transtext))
        itbg = ImageMobject("./itbg (1).png")
        itbg.scale(4)
        self.play(FadeInFromDown(itbg), FadeOut(trans), FadeOut(transtext), FadeOut(a),
        FadeOut(ta2), FadeOut(air))

        at1 = TextMobject("5. App and Web development").set_color(RED)
        at1.move_to(3*UP)
        

        at2 = TextMobject("This field is particularly for IT students and\\\\",
        "students in computer programming field").set_color(BLACK)
        at2.move_to(3*UP)

        intu = ImageMobject("./intu.png")
        intu.move_to(UP+2*LEFT)
        intarr = Arrow(LEFT,RIGHT).set_color(BLACK)
        intarr.next_to(intu, RIGHT, buff=0.1)
        grow = TextMobject("Growing").set_color(BLACK)
        grow.next_to(intarr, RIGHT, buff=0.1)

        hire = ImageMobject("./hiring.png").scale(2)
        hire.move_to(0.5*UP)
        at3 = TextMobject("Companies and organisations are hiring people\\\\",
        "for app and web development").set_color(BLACK)
        at3.move_to(3*UP)
        at4 = TextMobject("You can also provide freelancing services\\\\",
        "and generate revenue!").set_color(BLACK)
        at4.move_to(3*UP)

        atf = TextMobject("If you have no skills then you can learns\\\\",
        "over time asit is easy to learn").set_color(BLACK)
        atf.move_to(2.5*UP)






    
        self.play(Write(at1))
        self.play(FadeOut(at1))
        self.play(Write(at2))
        self.play(FadeInFromDown(intu))
        self.play(GrowArrow(intarr))
        self.play(Write(grow))
        self.play(FadeOut(grow), FadeOut(intarr), FadeOut(intu))
        self.play(ReplacementTransform(at2, at3))
        self.play(FadeInFromDown(hire))
        self.play(ReplacementTransform(at3, at4))
        self.play(FadeOut(hire))
        self.play(ReplacementTransform(at4, atf))
        enter = ImageMobject("./entertainment.png")
        enter.scale(4)
        self.play(FadeOut(atf), FadeOut(itbg), FadeInFromDown(enter))

        mt1 = TextMobject("6. Meme Marketing").set_color(RED)
        mt1.scale(2)
        mt1.move_to(3*UP)

        

        mt2 = TextMobject("Maybe you would not have heard of this\\\\",
        "but it is one of the fastest growing industries").set_color(BLACK)
        mt2.move_to(UP)

        creative = ImageMobject("./creative.png")
        creative.scale(2)
        creative.move_to(2*UP+4*LEFT)
        carr = Arrow(LEFT, RIGHT).set_color(BLACK)
        carr.next_to(creative, RIGHT, buff=0.1)
        meme = TextMobject("MEMES").set_color(BLACK)
        meme.next_to(carr, RIGHT, buff=0.1)
        enjoy = TextMobject("Enjoyed by any\\\\" 
        "age group").set_color(BLACK)
        enjoy.scale(0.7)
        enjoy.move_to(2.5*LEFT)
        ar1 = Arrow(meme.get_bottom(), enjoy.get_top(),  buff=0.1).set_color(BLACK)
        bene = TextMobject("Companies are using\\\\",
        "this for their\\\\",
        "benefit").set_color(BLACK)
        bene.scale(0.7)
        bene.move_to(0.5*RIGHT)
        ar2 = Arrow(meme.get_bottom(), bene.get_top(), buff=0.1).set_color(BLACK)
        freel = TextMobject("Can provide\\\\",
        "freelancing services").set_color(BLACK)
        freel.scale(0.7)
        freel.move_to(3.5*RIGHT)
        ar3 = Arrow(meme.get_bottom(), freel.get_top(), buff=0.1).set_color(BLACK)

        ml = TextMobject("You just need to be creative and\\\\",
        "you are READY!").set_color(BLACK)
        ml.scale(1.25)
        ml.move_to(2*UP)










        
        self.play(Write(mt1))
        self.play(Write(mt2))
        self.play(FadeOut(mt1))
        self.play(FadeOut(mt2))
        self.play(FadeIn(creative))
        self.play(GrowArrow(carr))
        self.play(Write(meme))
        self.play(GrowArrow(ar1))
        self.play(Write(enjoy))
        self.play(GrowArrow(ar2))
        self.play(Write(bene))
        self.play(GrowArrow(ar3))
        self.play(Write(freel))
        self.play(FadeOut(meme), FadeOut(carr), FadeOut(ar1), FadeOut(ar2), FadeOut(ar3),
        FadeOut(freel), FadeOut(enjoy), FadeOut(bene), FadeOut(creative))
        self.play(Write(ml))
        writer = ImageMobject("./writer.png")
        writer.scale(4.5)
        self.play(FadeOut(ml), FadeOut(enter), FadeInFromDown(writer))

        cw1 = TextMobject("7. Content Writing").set_color(RED)
        cw1.scale(1.5)
        cw1.move_to(3*UP)

        

        cw2 = TextMobject("If you are passionate about writing\\\\",
        "and have skills, you can be\\\\",
        "a content writer").set_color(BLACK)
        cw2.move_to(3*UP)

        wman = ImageMobject("./wman.png")
        wman.flip(RIGHT)
        wman.move_to(2.5*DOWN+3.5*RIGHT)

        wcloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        wcloud.scale(1.9)
        wcloud.next_to(wman, UP, buff=0.1)

        wct1 = TextMobject("You can post content\\\\",
        "on websites and\\\\",
        "advertisements and\\\\",
        "provide freelancing\\\\",
        "service").set_color(BLACK)
        wct1.scale(0.75)
        wct1.move_to(3.5*RIGHT+1*UP)

        cwf = TextMobject("Competition is more in this field as\\\\",
        "becoming a content writer is easy").set_color(BLACK)
        cwf.move_to(3*UP)







        
        self.play(Write(cw1))
        self.play(FadeOut(cw1))
        self.play(Write(cw2))
        self.play(FadeInFromDown(wman))
        self.play(Write(wcloud))
        self.play(Write(wct1))
        self.play(FadeOut(cw2))
        self.play(FadeOut(wct1), FadeOut(wcloud))
        self.play(Write(cwf))
        gd1 = ImageMobject("./gd.png")
        gd1.scale(5.5)
        self.play(FadeOut(writer), FadeOut(cwf), FadeOut(wman), FadeInFromDown(gd1))

        gd = TextMobject("8. Graphic Designer").set_color(RED)
        gd.scale(2)
        gd.move_to(3*UP)

        
        gd2 = TextMobject("It is another skill one could have\\\\",
        "and it is popularly more in demand\\\\",
        "as every company needs logos, posters etc").set_color(BLACK)
        gd2.move_to(2.5*UP)
        logo = ImageMobject("./logo.png")
        poster = ImageMobject("./poster.png")
        logo.move_to(2*LEFT)
        poster.move_to(2*RIGHT)

        gd3 = TextMobject("Just you have to learn is to\\\\",
        "operate some softwares like-").set_color(BLACK)
        gd3.move_to(2.5*DOWN)

        ps = ImageMobject("./ps.png")
        ae = ImageMobject("./ae.png")
        ps.move_to(2*LEFT)
        ae.move_to(2*RIGHT)









        
        self.play(Write(gd))
        self.play(FadeOut(gd))
        self.play(AnimationGroup(Write(gd2), GrowFromCenter(logo), GrowFromCenter(poster)))
        self.play(Write(gd3))
        self.play(FadeOut(logo), FadeOut(poster))
        self.play(GrowFromCenter(ps))
        self.play(GrowFromCenter(ae))
        buss = ImageMobject("./business.png")
        buss.scale(5)
        buss.move_to(UP)
        self.play(FadeOut(ps), FadeOut(gd1), FadeInFromDown(buss), FadeOut(ae), FadeOut(gd2), FadeOut(gd3))

        ds = TextMobject("9. DropShipping").set_color(RED)
        ds.scale(2)
        ds.move_to(3*UP)

        

        dst1 = TextMobject("Dropshipping is the easiest thing one can do\\\\",
        "for earning, it just needs your time").set_color(BLACK)
        dst1.move_to(3*UP)


        good = ImageMobject("./good.png")
        good.move_to(4*LEFT+UP)
        larr = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr.scale(0.5)
        larr.next_to(good, RIGHT, buff=0.1)
        larrt = TextMobject("Without keeping\\\\",
        "the stock").set_color(BLACK)
        larrt.next_to(larr, RIGHT, buff=0.1)
        larr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr1.next_to(larrt, RIGHT, buff=0.1)
        sell = TextMobject("Sell!").set_color(BLACK)
        sell.next_to(larr1, RIGHT, buff=0.1)

        dstf1 = TextMobject("You basically take the order from\\\\",
        "the customer, add your commisson\\\\",
        "and order to the main business").set_color(BLACK)
        dstf1.move_to(2*DOWN)

        dsf = TextMobject("Quite an easy job").set_color(BLACK)
        dsf.move_to(2*UP)
        




        
        self.play(Write(ds))
        self.play(FadeOut(ds))
        self.play(Write(dst1))
        self.play(FadeInFromDown(good))
        self.play(GrowArrow(larr))
        self.play(Write(larrt))
        self.play(GrowArrow(larr1))
        self.play(Write(sell))
        self.play(Write(dstf1))
        self.play(FadeOut(good), FadeOut(larr), FadeOut(larr1), FadeOut(sell),
        FadeOut(larrt), FadeOut(dstf1), FadeOut(dst1))
        self.play(Write(dsf))
        self.play(FadeOut(dsf), FadeOut(buss), FadeIn(image), FadeInFromDown(trees))

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1text1a = TextMobject("Do remember one thing\\\\",
        "you cannot just sit back\\\\",
        "and get paid right. So you\\\\",
        "must need to do something\\\\",
        "to get paid").set_color(BLACK)
        thoughtcloud1text1a.scale(0.7)
        thoughtcloud1text1a.move_to(3.5*LEFT+2.3*UP)

        fff= TextMobject("So there are many more options regarding\\\\",
        "additional revenues but these were the best\\\\",
        "and the most famous options you can do to\\\\",
        "earn some additional revenue").set_color(BLACK)
        fff.move_to(2*UP)

        fff1 = TextMobject("It not only gives you money other than\\\\",
        "experience, knowledge and helps building your career too.").set_color(BLACK)
        fff1.move_to(2.5*UP)

        pull = TextMobject("Pull up your\\\\",
        "socks and start\\\\",
        "WORKING!").set_color(BLACK)
        pull.move_to(3.5*LEFT+2.5*UP)

        fuck = TextMobject("Thank you for being\\\\",
        "with us, we will\\\\",
        "meet you in the next\\\\",
        "episode of\\\\",
        "personal finance").set_color(BLACK)
        fuck.scale(0.7)
        fuck.move_to(3.5*LEFT+2.3*UP)




        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2))
        self.play(Write(thoughtcloud1text1a))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1a), FadeOut(thoughtcloud2))
        self.play(Write(fff))
        self.play(FadeOut(fff))
        self.play(Write(fff1))
        self.play(FadeOut(fff1))
        self.wait()
        self.play(Write(thoughtcloud2))
        self.play(Write(pull))
        self.play(FadeOut(pull))
        self.play(Write(fuck))
        self.play(FadeOut(thoughtcloud2), FadeOut(fuck), ReplacementTransform(car1a, car2a))
        self.play(FadeOut(image), FadeOut(trees))







        self.wait()
        self.add(g)

class vid31(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(87)

        classr = ImageMobject("./class.png").move_to(DOWN)
        classr.scale(5)
        

        tt1 = TextMobject("2. HomeTuitions").set_color(RED)
        tt1.scale(2)
        tt1.move_to(3*UP)

        tt2 = TextMobject("Sharing your knowledge").set_color(BLACK)
        tt3 = ImageMobject("./tmoney.png")
        tt2.move_to(3*UP+3*LEFT)
        tt3.move_to(3*UP+3*RIGHT)
        tarrt = Arrow(tt2.get_right(), tt3.get_left(), buff=0.1).set_color(BLACK)
        
        tt4 = TextMobject("Do it").set_color(BLACK)
        tt4.scale(2)
        tt4.move_to(3*UP)
        or1 = TextMobject("or").set_color(BLACK)
        or1.scale(2)
        offline = ImageMobject("./tuition.png")
        offline.scale(2.5)
        offline.move_to(3*LEFT)
        online = ImageMobject("./onlinet.png")
        online.scale(2)
        online.move_to(3*RIGHT)

        ttf = TextMobject("And in this situation of covid-19\\\\",
        "it is a good opportunity for one to provide\\\\",
        "tuitions as everyone is surfing online now!").set_color(BLACK)
        ttf.move_to(3*UP)
        






        self.play(Write(tt1, run_time=4))
        self.play(FadeIn(classr))
        self.play(FadeOut(tt1))
        self.play(Write(tt2))
        self.play(GrowArrow(tarrt))
        self.play(GrowFromCenter(tt3))
        self.wait(6)
        self.play(FadeOut(tt2), FadeOut(tt3), FadeOut(tarrt))
        self.play(Write(tt4))
        self.play(GrowFromCenter(offline))
        self.play(Write(or1))
        self.play(GrowFromCenter(online))
        self.wait()
        self.play(FadeOut(or1), FadeOut(offline), FadeOut(online), Write(ttf, run_time=9), FadeOut(tt4))
        self.play(FadeOut(ttf), FadeOut(classr))

class vid32(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g= NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(117)

        it1 = TextMobject("3. InternShip").set_color(RED)
        it1.scale(2)
        it1.move_to(3*UP)
        ibg = ImageMobject("./ibg.png")
        ibg.scale(5)

        i = TextMobject("You can be an intern in any\\\\",
        "company or organization").set_color(BLACK)
        i.move_to(2.5*UP)

        intern1 = ImageMobject("./intern.png").scale(2)
        intern1.move_to(3*LEFT+2*DOWN)

        it2 = TextMobject("You can be an intern in\\\\",
        "any field such as").set_color(BLACK)
        it2.scale(1.5)
        it2.move_to(2.5*UP)

        iacc = ImageMobject("./iacc.png")
        iacc.move_to(4*RIGHT+UP)
        idesign = ImageMobject("./idesign.png")
        idesign.move_to(4*RIGHT+2*DOWN)

        if1 = TextMobject("And Many\\\\",
        "MORE!").set_color(RED)
        if1.scale(2)
        if1.move_to(2.5*UP)
        if2 = TextMobject("In this field you can explore\\\\",
        "and gain experience which will help you\\\\",
        "build your dreams").set_color(BLACK)
        if2.move_to(2.5*UP)

        workerf = ImageMobject("./workerf.png")
        workerf.scale(2.5)
        workerf.move_to(3*LEFT+2*DOWN)
        arr = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr.next_to(workerf)
        imoney = ImageMobject("./imoney.png")
        imoney.scale(2)
        imoney.next_to(arr, RIGHT, buff=0.1)






        self.play(FadeInFromDown(ibg))
        self.play(Write(it1))
        self.wait()
        self.play(FadeOut(it1))
        self.play(Write(i))
        self.wait(2)
        self.play(FadeOut(i))
        self.play(FadeInFromDown(intern1), Write(it2))
        self.play(GrowFromCenter(iacc))
        self.play(GrowFromCenter(idesign))
        self.play(ReplacementTransform(it2, if1))
        self.wait()
        self.play(FadeOut(intern1), FadeOut(if1), FadeOut(iacc), FadeOut(idesign))
        self.play(Write(if2, run_time=5))
        self.play(FadeIn(workerf))
        self.play(GrowArrow(arr))
        self.play(FadeIn(imoney))
        self.wait(2)
        self.play(FadeOut(workerf), FadeOut(imoney), FadeOut(arr), FadeOut(if2), FadeOut(ibg))






        self.wait()
        self.add(g)

class vid33(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g= NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(143)

        ta1 = TextMobject("4. Translation Services").set_color(RED)
        ta1.scale(1.5)
        ta1.move_to(2.5*UP)

        air = ImageMobject("./airport.png")
        air.scale(4)

        ta2 = TextMobject("If you know any regional language\\\\",
        "you can perform this service").set_color(BLACK)
        ta2.move_to(3*UP)

        company = ImageMobject("./company.png")
        company.move_to(5*LEFT+UP)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.scale(0.5)
        arr1.next_to(company, RIGHT, buff=0.1)
        arr1t = TextMobject("Switching their content\\\\",
        "to regional languages").set_color(BLACK)
        arr1t.next_to(arr1, buff=0.1)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.scale(0.5)
        arr2.next_to(arr1t, RIGHT, buff=0.1)
        local = ImageMobject("./local1.png")
        local.next_to(arr2, RIGHT, buff=0.1)
        trans = ImageMobject("./translate.png")
        trans.move_to(2*LEFT)
        transtext = TextMobject("Freelancing too!").set_color(BLACK)
        a = Arrow(LEFT,RIGHT).set_color(BLACK)
        a.scale(0.5)
        a.next_to(trans, RIGHT, buff=0.1)
        transtext.next_to(a, RIGHT, buff=0.1)







        self.play(FadeInFromDown(air))
        self.play(Write(ta1))
        self.wait()
        self.play(FadeOut(ta1))
        self.play(Write(ta2, run_time=6))
        self.play(FadeIn(company))
        self.play(GrowArrow(arr1))
        self.play(Write(arr1t))
        self.play(GrowArrow(arr2))
        self.play(FadeIn(local))
        self.play(FadeOut(arr1), FadeOut(arr2), FadeOut(local), FadeOut(arr1t),
        FadeOut(company))
        self.play(FadeInFromDown(trans))
        self.play(GrowArrow(a))
        self.play(Write(transtext))
        self.play(FadeOut(trans), FadeOut(transtext), FadeOut(a),
        FadeOut(ta2))

class vid34(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(166)
        at1 = TextMobject("5. App and Web development").set_color(RED)
        at1.move_to(3*UP)
        itbg = ImageMobject("./itbg (1).png")
        itbg.scale(4)

        at2 = TextMobject("This field is particularly for IT students and\\\\",
        "students in computer programming field").set_color(BLACK)
        at2.move_to(3*UP)

        intu = ImageMobject("./intu.png")
        intu.move_to(UP+2*LEFT)
        intarr = Arrow(LEFT,RIGHT).set_color(BLACK)
        intarr.next_to(intu, RIGHT, buff=0.1)
        grow = TextMobject("Growing").set_color(BLACK)
        grow.next_to(intarr, RIGHT, buff=0.1)

        hire = ImageMobject("./hiring.png").scale(2)
        hire.move_to(0.5*UP)
        at3 = TextMobject("Companies and organisations are hiring people\\\\",
        "for app and web development").set_color(BLACK)
        at3.move_to(3*UP)
        at4 = TextMobject("You can also provide freelancing services\\\\",
        "and generate revenue!").set_color(BLACK)
        at4.move_to(3*UP)

        atf = TextMobject("If you have no skills then you can learns\\\\",
        "over time asit is easy to learn").set_color(BLACK)
        atf.move_to(2.5*UP)






        self.play(FadeInFromDown(itbg))
        self.play(Write(at1))
        self.play(FadeOut(at1))
        self.play(Write(at2, run_time=6))
        self.play(FadeInFromDown(intu))
        self.play(GrowArrow(intarr))
        self.play(Write(grow))
        self.wait(2)
        self.play(FadeOut(grow), FadeOut(intarr), FadeOut(intu))
        self.play(ReplacementTransform(at2, at3))
        self.wait(4)
        self.play(FadeInFromDown(hire))
        self.play(ReplacementTransform(at3, at4))
        self.wait(4)
        self.play(FadeOut(hire))
        self.play(ReplacementTransform(at4, atf))
        self.wait(4)
        self.play(FadeOut(atf))

class vid35(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
        
        g = NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(198)
        mt1 = TextMobject("6. Meme Marketing").set_color(RED)
        mt1.scale(2)
        mt1.move_to(3*UP)

        enter = ImageMobject("./entertainment.png")
        enter.scale(4)

        mt2 = TextMobject("Maybe you would not have heard of this\\\\",
        "but it is one of the fastest growing industries").set_color(BLACK)
        mt2.move_to(UP)

        creative = ImageMobject("./creative.png")
        creative.scale(2)
        creative.move_to(2*UP+4*LEFT)
        carr = Arrow(LEFT, RIGHT).set_color(BLACK)
        carr.next_to(creative, RIGHT, buff=0.1)
        meme = TextMobject("MEMES").set_color(BLACK)
        meme.next_to(carr, RIGHT, buff=0.1)
        enjoy = TextMobject("Enjoyed by any\\\\" 
        "age group").set_color(BLACK)
        enjoy.scale(0.7)
        enjoy.move_to(2.5*LEFT)
        ar1 = Arrow(meme.get_bottom(), enjoy.get_top(),  buff=0.1).set_color(BLACK)
        bene = TextMobject("Companies are using\\\\",
        "this for their\\\\",
        "benefit").set_color(BLACK)
        bene.scale(0.7)
        bene.move_to(0.5*RIGHT)
        ar2 = Arrow(meme.get_bottom(), bene.get_top(), buff=0.1).set_color(BLACK)
        freel = TextMobject("Can provide\\\\",
        "freelancing services").set_color(BLACK)
        freel.scale(0.7)
        freel.move_to(3.5*RIGHT)
        ar3 = Arrow(meme.get_bottom(), freel.get_top(), buff=0.1).set_color(BLACK)

        ml = TextMobject("You just need to be creative and\\\\",
        "you are READY!").set_color(BLACK)
        ml.scale(1.25)
        ml.move_to(2*UP)










        self.play(FadeInFromDown(enter))
        self.play(Write(mt1, run_time=3))
        self.wait(5)
        self.play(Write(mt2, run_time=6))
        self.play(FadeOut(mt1))
        self.play(FadeOut(mt2))
        self.play(FadeIn(creative))
        self.play(GrowArrow(carr))
        self.play(Write(meme))
        self.wait(2)
        self.play(GrowArrow(ar1))
        self.play(Write(enjoy))
        self.play(GrowArrow(ar2))
        self.play(Write(bene))
        self.play(GrowArrow(ar3))
        self.play(Write(freel))
        self.wait()
        self.play(FadeOut(meme), FadeOut(carr), FadeOut(ar1), FadeOut(ar2), FadeOut(ar3),
        FadeOut(freel), FadeOut(enjoy), FadeOut(bene), FadeOut(creative))
        self.play(Write(ml, run_time=3))
        self.play(FadeOut(ml))







        self.wait()
        self.add(g)

class vid36(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(235)

        cw1 = TextMobject("7. Content Writing").set_color(RED)
        cw1.scale(1.5)
        cw1.move_to(3*UP)

        writer = ImageMobject("./writer.png")
        writer.scale(4.5)

        cw2 = TextMobject("If you are passionate about writing\\\\",
        "and have skills, you can be\\\\",
        "a content writer").set_color(BLACK)
        cw2.move_to(3*UP)

        wman = ImageMobject("./wman.png")
        wman.flip(RIGHT)
        wman.move_to(2.5*DOWN+3.5*RIGHT)

        wcloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        wcloud.scale(1.9)
        wcloud.next_to(wman, UP, buff=0.1)

        wct1 = TextMobject("You can post content\\\\",
        "on websites and\\\\",
        "advertisements and\\\\",
        "provide freelancing\\\\",
        "service").set_color(BLACK)
        wct1.scale(0.75)
        wct1.move_to(3.5*RIGHT+1*UP)

        cwf = TextMobject("Competition is more in this field as\\\\",
        "becoming a content writer is easy").set_color(BLACK)
        cwf.move_to(3*UP)







        self.play(FadeInFromDown(writer))
        self.play(Write(cw1))
        self.wait(3)
        self.play(FadeOut(cw1))
        self.play(Write(cw2, run_time=4))
        self.play(FadeInFromDown(wman))
        self.play(Write(wcloud,))
        self.play(Write(wct1, run_time=4))
        self.play(FadeOut(cw2))
        self.play(FadeOut(wct1), FadeOut(wcloud))
        self.play(Write(cwf, run_time=3))
        self.wait(4)
        self.play(FadeOut(cwf), FadeOut(wman))



        self.add(g)

class vid37(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()

        self.add_sound("./project4a.m4a")
        self.wait(260)
        gd = TextMobject("8. Graphic Designer").set_color(RED)
        gd.scale(2)
        gd.move_to(3*UP)

        gd1 = ImageMobject("./gd.png")
        gd1.scale(5.5)

        gd2 = TextMobject("It is another skill one could have\\\\",
        "and it is popularly more in demand\\\\",
        "as every company needs logos, posters etc").set_color(BLACK)
        gd2.move_to(2.5*UP)
        logo = ImageMobject("./logo.png")
        poster = ImageMobject("./poster.png")
        logo.move_to(2*LEFT)
        poster.move_to(2*RIGHT)

        gd3 = TextMobject("Just you have to learn is to\\\\",
        "operate some softwares like-").set_color(BLACK)
        gd3.move_to(2.5*DOWN)

        ps = ImageMobject("./ps.png")
        ae = ImageMobject("./ae.png")
        ps.move_to(2*LEFT)
        ae.move_to(2*RIGHT)









        self.play(FadeIn(gd1))
        self.play(Write(gd))
        self.wait(5)
        self.play(FadeOut(gd))
        self.play(AnimationGroup(Write(gd2, run_time=7), GrowFromCenter(logo), GrowFromCenter(poster)))
        self.wait(6)
        self.play(Write(gd3, run_time=5))
        self.play(FadeOut(logo), FadeOut(poster))
        self.play(GrowFromCenter(ps))
        self.play(GrowFromCenter(ae))
        self.play(FadeOut(ps), FadeOut(ae), FadeOut(gd2), FadeOut(gd3))





        self.wait()
        self.add(g)

class vid38(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):

        g = NumberPlane()
        self.add_sound("./project4a.m4a")
        self.wait(290)

        ds = TextMobject("9. DropShipping").set_color(RED)
        ds.scale(2)
        ds.move_to(3*UP)

        buss = ImageMobject("./business.png")
        buss.scale(5)
        buss.move_to(UP)

        dst1 = TextMobject("Dropshipping is the easiest thing one can do\\\\",
        "for earning, it just needs your time").set_color(BLACK)
        dst1.move_to(3*UP)


        good = ImageMobject("./good.png")
        good.move_to(4*LEFT+UP)
        larr = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr.scale(0.5)
        larr.next_to(good, RIGHT, buff=0.1)
        larrt = TextMobject("Without keeping\\\\",
        "the stock").set_color(BLACK)
        larrt.next_to(larr, RIGHT, buff=0.1)
        larr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr1.next_to(larrt, RIGHT, buff=0.1)
        sell = TextMobject("Sell!").set_color(BLACK)
        sell.next_to(larr1, RIGHT, buff=0.1)

        dstf1 = TextMobject("You basically take the order from\\\\",
        "the customer, add your commisson\\\\",
        "and order to the main business").set_color(BLACK)
        dstf1.move_to(2*DOWN)

        dsf = TextMobject("Quite an easy job").set_color(BLACK)
        dsf.move_to(2*UP)
        




        self.play(FadeInFromDown(buss))
        self.play(Write(ds))
        self.wait(7)
        self.play(FadeOut(ds))
        self.play(Write(dst1, run_time=5))
        self.play(FadeInFromDown(good))
        self.play(GrowArrow(larr))
        self.play(Write(larrt, run_time=2))
        self.play(GrowArrow(larr1))
        self.play(Write(sell))
        self.wait()
        self.play(Write(dstf1, run_time=6))
        self.play(FadeOut(good), FadeOut(larr), FadeOut(larr1), FadeOut(sell),
        FadeOut(larrt), FadeOut(dstf1), FadeOut(dst1))
        self.play(Write(dsf, run_time=3))
        self.wait(2)
        self.play(FadeOut(dsf))





        self.wait()
        self.add(g)

class vid39(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        image=ImageMobject("./road1.png")
        image.scale(5.6)
        trees = ImageMobject("./trees.png")
        trees.scale(8)
        trees.move_to(0.52*UP)

        self.add_sound("./project4a.m4a")
        self.wait(327)

        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1text1a = TextMobject("Do remember one thing\\\\",
        "you cannot just sit back\\\\",
        "and get paid right. So you\\\\",
        "must need to do something\\\\",
        "to get paid").set_color(BLACK)
        thoughtcloud1text1a.scale(0.7)
        thoughtcloud1text1a.move_to(3.5*LEFT+2.3*UP)

        fff= TextMobject("So there are many more options regarding\\\\",
        "additional revenues but these were the best\\\\",
        "and the most famous options you can do to\\\\",
        "earn some additional revenue").set_color(BLACK)
        fff.move_to(2*UP)

        fff1 = TextMobject("It not only gives you money other than\\\\",
        "experience, knowledge and helps building your career too.").set_color(BLACK)
        fff1.move_to(2.5*UP)

        pull = TextMobject("Pull up your\\\\",
        "socks and start\\\\",
        "WORKING!").set_color(BLACK)
        pull.move_to(3.5*LEFT+2.5*UP)

        fuck = TextMobject("Thank you for being\\\\",
        "with us, we will\\\\",
        "meet you in the next\\\\",
        "episode of\\\\",
        "personal finance").set_color(BLACK)
        fuck.scale(0.7)
        fuck.move_to(3.5*LEFT+2.3*UP)



        self.play(FadeIn(image))
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2))
        self.play(Write(thoughtcloud1text1a, run_time=8))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1a), FadeOut(thoughtcloud2))
        self.play(Write(fff, run_time=8))
        self.play(FadeOut(fff))
        self.play(Write(fff1, run_time=7))
        self.play(FadeOut(fff1))
        self.wait()
        self.play(Write(thoughtcloud2))
        self.play(Write(pull))
        self.play(FadeOut(pull))
        self.play(Write(fuck, run_time=4))
        self.play(FadeOut(thoughtcloud2), FadeOut(fuck), ReplacementTransform(car1a, car2a))
        self.play(FadeOut(image), FadeOut(trees))

class vid3f(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }

    def construct(self):

        g=NumberPlane()
        self.add_sound("./project4a.m4a")
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
        thoughtcloud1text1 = TextMobject("Hi again!").set_color(BLACK)
        thoughtcloud1text1.move_to(3.5*LEFT+1.25*UP)

        thoughtcloud2 = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        thoughtcloud2.scale(2)
        thoughtcloud2.move_to(3.5*LEFT+1.8*UP)
        thoughtcloud2text1 = TextMobject(" Welcome\\\\"
        "to the episode\\\\",
        "ways to earn\\\\",
        "additional income").set_color(BLACK)
        thoughtcloud2text1.move_to(3.5*LEFT+2.5*UP)

        tct1 = TextMobject("So far we have\\\\",
        "learnt how to save\\\\",
        "money and why should\\\\"
        "you do this").set_color(BLACK)
        tct1.move_to(3.5*LEFT+2.5*UP)
        tct1.scale(0.8)


        gard = ImageMobject("./vid3scene.png")
        gard.scale(6.5)
        gard.move_to(2*UP)

        s1t1 = TextMobject("Not everybody gets the same amount\\\\",
        "of money or just want to earn\\\\",
        "some amount for a better future").set_color(BLACK)
        s1t2 = TextMobject("So, I will share 9 ways so that\\\\",
        "you can earn extra money.").set_color(BLACK)
        s1t3 = TextMobject("It's not just the money\\\\",
        "you can slso diversify your knowledge, \\\\",
        "skill and work experience too").set_color(BLACK)
        s1t1.move_to(3*LEFT+2.5*UP)
        s1t2.move_to(3*LEFT+3*UP)
        s1t3.move_to(3*LEFT+2.5*UP)
        
        ft1 = TextMobject("1. FreeLancing!").set_color(RED)
        ft1.move_to(3*UP)
        ft1.scale(2)
        ft2 = TextMobject("Freelancing"," is \\\\" 
        "basically where you do\\\\", 
        "not work for any\\\\",
        "specific organization\\\\"
        "or company").set_color(BLACK)
        ft2.scale(0.75)
        ft2.move_to(4*RIGHT+2.7*UP)

        client = ImageMobject("./client.png").scale(2)
        no = ImageMobject("./no.png").scale(2.5)
        client.move_to(3*LEFT+2*DOWN)
        no.move_to(3*LEFT+2*DOWN)

        buck = ImageMobject("./bucks.png")
        nine = ImageMobject("./nine.png")
        nine.move_to(3*LEFT)
        buck.move_to(3*RIGHT)
        barrn = Arrow(nine.get_right(), buck.get_left(), buff=0.1).set_color(BLACK)

        workex = ImageMobject("./workex.png").scale(1.5)
        workex.move_to(3*RIGHT+DOWN)
        skill = ImageMobject('./skill.png').scale(1.5)
        skill.move_to(DOWN)
        know = ImageMobject("./know.png").scale(1.5)
        know.move_to(3*LEFT+DOWN)




        corp =ImageMobject("./corp.png")
        corp.scale(2)
        corp.move_to(4*RIGHT+2*DOWN)
        corpc = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        corpc.scale(2)
        corpc.next_to(corp, UP, buff=0.1)

        ft3 = TextMobject("You just have to\\\\",
        "do specific projects\\\\",
        "and get paid for it").set_color(BLACK)
        
        ft3.move_to(4*RIGHT+2.7*UP)

        desk = ImageMobject("./desk.png")
        m = TextMobject("Money").set_color(BLACK)
        m.move_to(3*LEFT+2*DOWN)
        
        desk.scale(1.5)
        desk.move_to(3*LEFT+2*UP)
        darrm = Arrow(desk.get_bottom(), m.get_top(), buff=0.1).set_color(BLACK)
        

        ft4 = TextMobject("Gain experience and make it\\\\",
        "your full time job").set_color(BLACK)
        fulltime = ImageMobject("./fulltime.png")
        fulltime.scale(2.5)
        fulltime.move_to(3*LEFT)
        ft4.move_to(3*LEFT+3*DOWN)
        ftf = TextMobject("Some of the\\\\",
        "trustworthy\\\\",
        "websites\\\\",
        "are -").set_color(BLACK)
        
        ftf.move_to(4*RIGHT+2.7*UP)
        freelance = ImageMobject("./freelance.png")
        wb1 = TextMobject("www.freelancer.in").set_color(BLACK)
        freelance.scale(2)
        freelance.move_to(3*LEFT+2*DOWN)
        wb1.next_to(freelance, UP, buff=0.1)
        upwork = ImageMobject("./upwork.png")
        upwork.move_to(3*LEFT+2*UP)
        wb2 = TextMobject("www.upwork.com").set_color(BLACK)
        wb2.next_to(upwork, UP, buff=0.01)













        self.add(image)
        self.play(FadeInFromDown(trees))
        self.play(ReplacementTransform(car, car1))
        self.play(Write(thoughtcloud1), Write(thoughtcloud1text1))
        self.play(FadeOut(thoughtcloud1text1))
        self.play(ReplacementTransform(thoughtcloud1, thoughtcloud2))
        self.play(Write(thoughtcloud2text1))
        self.play(FadeOut(thoughtcloud2text1))
        self.play(Write(tct1, run_time=3))
        self.play(FadeOut(thoughtcloud2), FadeOut(tct1), ReplacementTransform(car1, car2))
        self.play(FadeOut(image), FadeOut(trees), FadeInFromDown(gard))
        
        self.play(Write(s1t1, run_time=9))
        self.play(FadeOut(s1t1))
        self.play(AnimationGroup(Write(s1t2, run_time=5), FadeIn(nine), GrowArrow(barrn), FadeIn(buck), lag_ratio=0.5))
        self.play(FadeOut(s1t2), FadeOut(nine), FadeOut(barrn), FadeOut(buck))
        self.play(AnimationGroup(Write(s1t3, run_time=8.5),FadeIn(know), FadeIn(skill), FadeIn(workex), lag_ratio=0.5))
        self.play(FadeOut(s1t3), FadeOut(know), FadeOut(skill), FadeOut(workex))
        self.play(Write(ft1))
        self.wait(4)
        self.play(FadeOut(ft1))
        self.play(FadeInFromDown(corp))
        self.play(Write(corpc))
        self.play(Write(ft2, run_time=6))
        self.play(FadeInFromDown(client))
        self.play(GrowFromCenter(no))
        self.play(FadeOut(ft2), FadeOut(client), FadeOut(no))
        self.play(Write(ft3))
        self.play(FadeInFromDown(desk))
        self.play(GrowArrow(darrm))
        self.play(Write(m))
        self.wait(4)
        self.play(FadeOut(m), FadeOut(darrm), FadeOut(desk))
        self.play(FadeIn(fulltime))
        self.play(Write(ft4, run_time=3))
        self.play(FadeOut(fulltime), FadeOut(ft4), FadeOut(ft3))
        self.wait(2)
        self.play(Write(ftf))
        self.play(FadeInFromDown(upwork))
        self.play(Write(wb2))
        self.wait(4)
        self.play(FadeInFromDown(freelance))
        self.play(Write(wb1))
        self.wait(3)
        self.play(FadeOut(wb1), FadeOut(wb2), FadeOut(freelance), FadeOut(upwork),
        FadeOut(ftf), FadeOut(gard), FadeOut(corp), FadeOut(corpc))

        classr = ImageMobject("./class.png").move_to(DOWN)
        classr.scale(5)
        

        tt1 = TextMobject("2. HomeTuitions").set_color(RED)
        tt1.scale(2)
        tt1.move_to(3*UP)

        tt2 = TextMobject("Sharing your knowledge").set_color(BLACK)
        tt3 = ImageMobject("./tmoney.png")
        tt2.move_to(3*UP+3*LEFT)
        tt3.move_to(3*UP+3*RIGHT)
        tarrt = Arrow(tt2.get_right(), tt3.get_left(), buff=0.1).set_color(BLACK)
        
        tt4 = TextMobject("Do it").set_color(BLACK)
        tt4.scale(2)
        tt4.move_to(3*UP)
        or1 = TextMobject("or").set_color(BLACK)
        or1.scale(2)
        offline = ImageMobject("./tuition.png")
        offline.scale(2.5)
        offline.move_to(3*LEFT)
        online = ImageMobject("./onlinet.png")
        online.scale(2)
        online.move_to(3*RIGHT)

        ttf = TextMobject("And in this situation of covid-19\\\\",
        "it is a good opportunity for you to provide\\\\",
        "tuitions as everyone is surfing online now!").set_color(BLACK)
        ttf.move_to(3*UP)
        






        self.play(Write(tt1, run_time=4))
        self.play(FadeIn(classr))
        self.play(FadeOut(tt1))
        self.play(Write(tt2))
        self.play(GrowArrow(tarrt))
        self.play(GrowFromCenter(tt3))
        self.wait(4)
        self.play(FadeOut(tt2), FadeOut(tt3), FadeOut(tarrt))
        self.play(Write(tt4))
        self.play(GrowFromCenter(offline))
        self.play(Write(or1))
        self.play(GrowFromCenter(online))
        self.wait()
        ibg = ImageMobject("./ibg.png")
        ibg.scale(5)
        self.play(FadeOut(or1), FadeOut(offline), FadeOut(online), Write(ttf, run_time=9), FadeOut(tt4))
        self.play(FadeOut(ttf), FadeOut(classr), FadeInFromDown(ibg))



        it1 = TextMobject("3. InternShip").set_color(RED)
        it1.scale(2)
        it1.move_to(3*UP)
        

        i = TextMobject("You can be an intern in any\\\\",
        "company or organization").set_color(BLACK)
        i.move_to(2.5*UP)

        intern1 = ImageMobject("./intern.png").scale(2)
        intern1.move_to(3*LEFT+2*DOWN)

        it2 = TextMobject("You can be an intern in\\\\",
        "any field such as").set_color(BLACK)
        it2.scale(1.5)
        it2.move_to(2.5*UP)

        iacc = ImageMobject("./iacc.png")
        iacc.move_to(4*RIGHT+UP)
        idesign = ImageMobject("./idesign.png")
        idesign.move_to(4*RIGHT+2*DOWN)

        if1 = TextMobject("And Many\\\\",
        "MORE!").set_color(RED)
        if1.scale(2)
        if1.move_to(2.5*UP)
        if2 = TextMobject("In this field you can explore\\\\",
        "and gain experience which will help you\\\\",
        "build your dreams as well").set_color(BLACK)
        if2.move_to(2.5*UP)

        workerf = ImageMobject("./workerf.png")
        workerf.scale(2.5)
        workerf.move_to(3*LEFT+2*DOWN)
        arr = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr.next_to(workerf)
        imoney = ImageMobject("./imoney.png")
        imoney.scale(2)
        imoney.next_to(arr, RIGHT, buff=0.1)






        self.wait()
        self.play(Write(it1))
        self.wait()
        self.play(FadeOut(it1))
        self.play(Write(i))
        self.wait(2)
        self.play(FadeOut(i))
        self.play(FadeInFromDown(intern1), Write(it2))
        self.play(GrowFromCenter(iacc))
        self.play(GrowFromCenter(idesign))
        self.play(ReplacementTransform(it2, if1))
        self.wait()
        self.play(FadeOut(intern1), FadeOut(if1), FadeOut(iacc), FadeOut(idesign))
        self.play(Write(if2, run_time=5))
        self.play(FadeIn(workerf))
        self.play(GrowArrow(arr))
        self.play(FadeIn(imoney))
        self.wait(2)
        air = ImageMobject("./airport.png")
        air.scale(4)
        self.play(FadeOut(workerf), FadeOut(imoney), FadeOut(arr), FadeOut(if2), FadeOut(ibg), FadeInFromDown(air))

        ta1 = TextMobject("4. Translation Services").set_color(RED)
        ta1.scale(1.5)
        ta1.move_to(2.5*UP)

        

        ta2 = TextMobject("If you know many regional language\\\\",
        "you can step into service").set_color(BLACK)
        ta2.move_to(3*UP)

        company = ImageMobject("./company.png")
        company.move_to(5*LEFT+UP)
        arr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr1.scale(0.5)
        arr1.next_to(company, RIGHT, buff=0.1)
        arr1t = TextMobject("Switching their content\\\\",
        "to regional languages").set_color(BLACK)
        arr1t.next_to(arr1, buff=0.1)
        arr2 = Arrow(LEFT, RIGHT).set_color(BLACK)
        arr2.scale(0.5)
        arr2.next_to(arr1t, RIGHT, buff=0.1)
        local = ImageMobject("./local1.png")
        local.next_to(arr2, RIGHT, buff=0.1)
        trans = ImageMobject("./translate.png")
        trans.move_to(2*LEFT)
        transtext = TextMobject("Freelancing too!").set_color(BLACK)
        a = Arrow(LEFT,RIGHT).set_color(BLACK)
        a.scale(0.5)
        a.next_to(trans, RIGHT, buff=0.1)
        transtext.next_to(a, RIGHT, buff=0.1)







        self.wait()
        self.play(Write(ta1))
        self.wait()
        self.play(FadeOut(ta1))
        self.play(Write(ta2, run_time=6))
        self.play(FadeIn(company))
        self.play(GrowArrow(arr1))
        self.play(Write(arr1t))
        self.play(GrowArrow(arr2))
        self.play(FadeIn(local))
        self.play(FadeOut(arr1), FadeOut(arr2), FadeOut(local), FadeOut(arr1t),
        FadeOut(company))
        self.play(FadeInFromDown(trans))
        self.play(GrowArrow(a))
        self.play(Write(transtext))
        itbg = ImageMobject("./itbg (1).png")
        itbg.scale(4)
        self.play(FadeOut(trans), FadeOut(transtext), FadeOut(a),
        FadeOut(ta2), FadeOut(air), FadeInFromDown(itbg))

        at1 = TextMobject("5. App and Web development").set_color(RED)
        at1.move_to(3*UP)
        

        at2 = TextMobject("This field is particularly for IT students and\\\\",
        "students in computer programming field").set_color(BLACK)
        at2.move_to(3*UP)

        intu = ImageMobject("./intu.png")
        intu.move_to(UP+2*LEFT)
        intarr = Arrow(LEFT,RIGHT).set_color(BLACK)
        intarr.next_to(intu, RIGHT, buff=0.1)
        grow = TextMobject("Growing").set_color(BLACK)
        grow.next_to(intarr, RIGHT, buff=0.1)

        hire = ImageMobject("./hiring.png").scale(2)
        hire.move_to(0.5*UP)
        at3 = TextMobject("Companies and organisations are hiring people\\\\",
        "for app and web development").set_color(BLACK)
        at3.move_to(3*UP)
        at4 = TextMobject("You can also provide freelancing services\\\\",
        "and generate revenue!").set_color(BLACK)
        at4.move_to(3*UP)

        atf = TextMobject("If you have no skills then you can just learn\\\\",
        "over time as it is easy to learn").set_color(BLACK)
        atf.move_to(2.5*UP)






        self.wait()
        self.play(Write(at1))
        self.play(FadeOut(at1))
        self.play(Write(at2, run_time=6))
        self.play(FadeInFromDown(intu))
        self.play(GrowArrow(intarr))
        self.play(Write(grow))
        self.wait(2)
        self.play(FadeOut(grow), FadeOut(intarr), FadeOut(intu))
        self.play(ReplacementTransform(at2, at3))
        self.wait(4)
        self.play(FadeInFromDown(hire))
        self.play(ReplacementTransform(at3, at4))
        self.wait(4)
        self.play(FadeOut(hire))
        self.play(ReplacementTransform(at4, atf))
        self.wait(4)
        enter = ImageMobject("./entertainment.png")
        enter.scale(4)
        self.play(FadeOut(atf), FadeOut(itbg), FadeInFromDown(enter))



        mt1 = TextMobject("6. Meme Marketing").set_color(RED)
        mt1.scale(2)
        mt1.move_to(3*UP)

        

        mt2 = TextMobject("Maybe you would not have heard about this\\\\",
        "but it is one of the fastest growing industries").set_color(BLACK)
        mt2.move_to(UP)

        creative = ImageMobject("./creative.png")
        creative.scale(2)
        creative.move_to(2*UP+4*LEFT)
        carr = Arrow(LEFT, RIGHT).set_color(BLACK)
        carr.next_to(creative, RIGHT, buff=0.1)
        meme = TextMobject("MEMES").set_color(BLACK)
        meme.next_to(carr, RIGHT, buff=0.1)
        enjoy = TextMobject("Enjoyed by any\\\\" 
        "age group").set_color(BLACK)
        enjoy.scale(0.7)
        enjoy.move_to(2.5*LEFT)
        ar1 = Arrow(meme.get_bottom(), enjoy.get_top(),  buff=0.1).set_color(BLACK)
        bene = TextMobject("Companies are using\\\\",
        "this for their\\\\",
        "benefit").set_color(BLACK)
        bene.scale(0.7)
        bene.move_to(0.5*RIGHT)
        ar2 = Arrow(meme.get_bottom(), bene.get_top(), buff=0.1).set_color(BLACK)
        freel = TextMobject("Can provide\\\\",
        "freelancing services").set_color(BLACK)
        freel.scale(0.7)
        freel.move_to(3.5*RIGHT)
        ar3 = Arrow(meme.get_bottom(), freel.get_top(), buff=0.1).set_color(BLACK)

        ml = TextMobject("You just need to be creative and\\\\",
        "you are READY!").set_color(BLACK)
        ml.scale(1.25)
        ml.move_to(2*UP)










        
        self.play(Write(mt1, run_time=3))
        self.wait(5)
        self.play(Write(mt2, run_time=6))
        self.play(FadeOut(mt1))
        self.play(FadeOut(mt2))
        self.play(FadeIn(creative))
        self.play(GrowArrow(carr))
        self.play(Write(meme))
        self.wait()
        self.play(GrowArrow(ar1))
        self.play(Write(enjoy))
        self.play(GrowArrow(ar2))
        self.play(Write(bene))
        self.play(GrowArrow(ar3))
        self.play(Write(freel))
        self.wait()
        self.play(FadeOut(meme), FadeOut(carr), FadeOut(ar1), FadeOut(ar2), FadeOut(ar3),
        FadeOut(freel), FadeOut(enjoy), FadeOut(bene), FadeOut(creative))
        self.play(Write(ml, run_time=3))
        writer = ImageMobject("./writer.png")
        writer.scale(4.5)
        self.play(FadeOut(ml), FadeOut(enter), FadeInFromDown(writer))

        cw1 = TextMobject("7. Content Writing").set_color(RED)
        cw1.scale(1.5)
        cw1.move_to(3*UP)

        

        cw2 = TextMobject("If you are passionate about writing\\\\",
        "and have skills, you can be\\\\",
        "a content writer").set_color(BLACK)
        cw2.move_to(3*UP)

        wman = ImageMobject("./wman.png")
        wman.flip(RIGHT)
        wman.move_to(2.5*DOWN+3.5*RIGHT)

        wcloud = SVGMobject("./cloud1.svg").set_stroke(BLACK)
        wcloud.scale(1.9)
        wcloud.next_to(wman, UP, buff=0.1)

        wct1 = TextMobject("You can post content\\\\",
        "in websites and\\\\",
        "advertisements and\\\\",
        "provide freelancing\\\\",
        "service").set_color(BLACK)
        wct1.scale(0.75)
        wct1.move_to(3.5*RIGHT+1*UP)

        cwf = TextMobject("Competition is tight in this field as\\\\",
        "becoming a content writer is no tough job").set_color(BLACK)
        cwf.move_to(3*UP)







        
        self.play(Write(cw1))
        self.wait(3)
        self.play(FadeOut(cw1))
        self.play(Write(cw2, run_time=4))
        self.play(FadeInFromDown(wman))
        self.play(Write(wcloud,))
        self.play(Write(wct1, run_time=4))
        self.play(FadeOut(cw2))
        self.play(FadeOut(wct1), FadeOut(wcloud))
        self.play(Write(cwf, run_time=3))
        self.wait(4)
        gd1 = ImageMobject("./gd.png")
        gd1.scale(5.5)
        self.play(FadeOut(cwf), FadeOut(wman), FadeOut(writer), FadeIn(gd1))


        gd = TextMobject("8. Graphic Designer").set_color(RED)
        gd.scale(2)
        gd.move_to(3*UP)

        

        gd2 = TextMobject("It is another skill one could have\\\\",
        "and it is popularly more in demand\\\\",
        "and every company needs logos, posters etc").set_color(BLACK)
        gd2.move_to(2.5*UP)
        logo = ImageMobject("./logo.png")
        poster = ImageMobject("./poster.png")
        logo.move_to(2*LEFT)
        poster.move_to(2*RIGHT)

        gd3 = TextMobject("Just you have to learn is to\\\\",
        "operate some softwares like-").set_color(BLACK)
        gd3.move_to(2.5*DOWN)

        ps = ImageMobject("./ps.png")
        ae = ImageMobject("./ae.png")
        ps.move_to(2*LEFT)
        ae.move_to(2*RIGHT)









        
        self.play(Write(gd))
        self.wait(5)
        self.play(FadeOut(gd))
        self.play(AnimationGroup(Write(gd2, run_time=7), GrowFromCenter(logo), GrowFromCenter(poster)))
        self.wait(4)
        self.play(Write(gd3, run_time=5))
        self.play(FadeOut(logo), FadeOut(poster))
        self.play(GrowFromCenter(ps))
        self.play(GrowFromCenter(ae))
        buss = ImageMobject("./business.png")
        buss.scale(5)
        buss.move_to(UP)
        self.play(FadeOut(ps), FadeOut(ae), FadeOut(gd2), FadeOut(gd3), FadeOut(gd1), FadeInFromDown(buss))

        ds = TextMobject("9. DropShipping").set_color(RED)
        ds.scale(2)
        ds.move_to(3*UP)

        

        dst1 = TextMobject("Dropshipping is the easiest thing one can do\\\\",
        "for earning, it just needs your time").set_color(BLACK)
        dst1.move_to(3*UP)


        good = ImageMobject("./good.png")
        good.move_to(4*LEFT+UP)
        larr = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr.scale(0.5)
        larr.next_to(good, RIGHT, buff=0.1)
        larrt = TextMobject("Without keeping\\\\",
        "the stock").set_color(BLACK)
        larrt.next_to(larr, RIGHT, buff=0.1)
        larr1 = Arrow(LEFT, RIGHT).set_color(BLACK)
        larr1.next_to(larrt, RIGHT, buff=0.1)
        sell = TextMobject("Sell!").set_color(BLACK)
        sell.next_to(larr1, RIGHT, buff=0.1)

        dstf1 = TextMobject("You basically take the order from\\\\",
        "the customer, add your commisson\\\\",
        "and order to the main business").set_color(BLACK)
        dstf1.move_to(2*DOWN)

        dsf = TextMobject("Quite an easy job").set_color(BLACK)
        dsf.move_to(2*UP)
        




        
        self.play(Write(ds))
        self.wait(7)
        self.play(FadeOut(ds))
        self.play(Write(dst1, run_time=5))
        self.play(FadeInFromDown(good))
        self.play(GrowArrow(larr))
        self.play(Write(larrt, run_time=2))
        self.play(GrowArrow(larr1))
        self.play(Write(sell))
        self.wait()
        self.play(Write(dstf1, run_time=6))
        self.play(FadeOut(good), FadeOut(larr), FadeOut(larr1), FadeOut(sell),
        FadeOut(larrt), FadeOut(dstf1), FadeOut(dst1))
        self.play(Write(dsf, run_time=3))
        self.wait(2)
        self.play(FadeOut(dsf), FadeOut(buss), FadeIn(image), FadeInFromDown(trees))


        


        cara = ImageMobject("./car.png")
        cara.move_to(1*DOWN+10*LEFT)
        car1a = ImageMobject("./car.png")
        car1a.move_to(1*DOWN+3.5*LEFT)
        car2a = ImageMobject("./car.png")
        car2a.move_to(1*DOWN+10*RIGHT)

        thoughtcloud1text1a = TextMobject("Do remember one thing\\\\",
        "you cannot just sit back\\\\",
        "and get paid right. So you\\\\",
        "must need to do something\\\\",
        "to get paid").set_color(BLACK)
        thoughtcloud1text1a.scale(0.7)
        thoughtcloud1text1a.move_to(3.5*LEFT+2.3*UP)

        fff= TextMobject("So there are plethora of options regarding\\\\",
        "additional revenues but these were the best\\\\",
        "and the most famous options you can do to\\\\",
        "earn some additional revenue").set_color(BLACK)
        fff.move_to(2*UP)

        fff1 = TextMobject("It not only gives you money other than\\\\",
        "experience, knowledge and helps building your career too.").set_color(BLACK)
        fff1.move_to(2.5*UP)

        pull = TextMobject("Pull up your\\\\",
        "socks and start\\\\",
        "WORKING!").set_color(BLACK)
        pull.move_to(3.5*LEFT+2.5*UP)

        fuck = TextMobject("Thank you for being\\\\",
        "with us, we will\\\\",
        "meet you in the next\\\\",
        "episode of\\\\",
        "personal finance").set_color(BLACK)
        fuck.scale(0.7)
        fuck.move_to(3.5*LEFT+2.3*UP)



        
        self.play(ReplacementTransform(cara, car1a))
        self.wait(0.5)
        self.play(Write(thoughtcloud2))
        self.play(Write(thoughtcloud1text1a, run_time=8))
        self.wait()
        self.play(FadeOut(thoughtcloud1text1a), FadeOut(thoughtcloud2))
        self.play(Write(fff, run_time=8))
        self.play(FadeOut(fff))
        self.wait(2)
        self.play(Write(fff1, run_time=7))
        self.play(FadeOut(fff1))
        self.wait(2)
        self.play(Write(thoughtcloud2))
        self.play(Write(pull))
        self.play(FadeOut(pull))
        self.play(Write(fuck, run_time=4))
        self.play(FadeOut(thoughtcloud2), FadeOut(fuck), ReplacementTransform(car1a, car2a))
        self.play(FadeOut(image), FadeOut(trees))




        
        
