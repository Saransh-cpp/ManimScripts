from manimlib.imports import *
class test(Scene):
    CONFIG={
        "camera_config": {"background_color":BLUE},
    }
    def construct(self):
    
        
        build = ImageMobject("./build.png")
        build.scale(4.6)
        self.play(FadeIn(build))