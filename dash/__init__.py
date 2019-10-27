 
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty,ListProperty,StringProperty
Builder.load_string('''
<Dash>:
    FloatLayout:
        size_hint:None,None
        pos_hint:{"center_x":.5,"center_y":.5}
        size:1*min(root.size),1*min(root.size)
        canvas:
            Color:
                rgba:0,1,1,1
            Ellipse:
                pos:self.pos
                size:self.size
                source:"asset/ring_besar.png"
    FloatLayout:
        size_hint:None,None
        pos_hint:{"center_x":.5,"center_y":.5}
        size:1*min(root.size),1*min(root.size)
        canvas:
            Color:
                rgba:0,1,1,.2
            Ellipse:
                pos:self.pos
                size:self.size
                source:"asset/kaca_bulat.png"

    FloatLayout:
        size_hint:None,None
        pos_hint:{"center_x":.5,"center_y":.5}
        size:1*min(root.size),1*min(root.size)
        canvas.before:
            PushMatrix
            Rotate:
                angle: 140-root.jarum_value
                origin: self.center
        canvas:
            Color:
                rgba:1,1,1,1
            Ellipse:
                pos:self.pos
                size:self.size
                source:"asset/jarum_panjang.png"
        canvas.after:
            PopMatrix
    FloatLayout:
        size_hint:None,None
        pos_hint:{"center_x":.5,"center_y":.5}
        size:1*min(root.size),1*min(root.size)
        canvas:
            Color:
                rgba:0,1,1,1
            Ellipse:
                pos:self.pos
                size:self.size
                source:root.dial_src
        Label:
            pos_hint:{"center_x":.5,"center_y":.5}
            text:str(int(root.value))
            font_size:self.height/3.5
            color:0,1,1,1
    
''')
class Dash(FloatLayout):
    value=NumericProperty(0)
    dial_src=StringProperty("asset/rpm.png")
    
    def __init__(self, *args,**kwargs):
        super(Dash,self).__init__(*args,**kwargs)
class DashTacho(Dash):
    value=NumericProperty(0)
    dial_src=StringProperty("asset/rpm.png")
    jarum_value=NumericProperty(0)
    def __init__(self, *args,**kwargs):
        super(DashTacho,self).__init__(*args,**kwargs)

        self.demo()
    def demo(self):
        self.value=14000
        self.anim = Animation(jarum_value=self.value*280/14000, duration=1)
        self.anim.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.anim = Animation(jarum_value=self.value*280/14000, duration=2)
        self.anim.start(self)
    def show_value(self,data):
        self.anim = Animation(jarum_value=self.value*280/14000,duration=1,t="linear")
        self.anim.start(self)
    def reset(self):
        self.jarum_value = 0
        self.value = 0
class DashTps(Dash):
    value=NumericProperty(0)
    dial_src=StringProperty("asset/throttle.png")
    jarum_value=NumericProperty(0)
    def __init__(self, *args,**kwargs):
        super(DashTps,self).__init__(*args,**kwargs)
        self.demo()
    def demo(self):
        self.value=100
        self.anim = Animation(jarum_value=self.value*280/100, duration=1)
        self.anim.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.anim = Animation(jarum_value=self.value*280/100, duration=2)
        self.anim.start(self)
    def show_value(self,data):
        self.anim = Animation(jarum_value=self.value*280/100,duration=1,t="linear")
        self.anim.start(self)
    def reset(self):
        self.jarum_value = 0
        self.value = 0
class DashBatt(Dash):
    value=NumericProperty(0)
    jarum_value=NumericProperty(0)
    dial_src=StringProperty("asset/batt.png")
    def __init__(self, *args,**kwargs):
        super(DashBatt,self).__init__(*args,**kwargs)
        self.demo()
    def demo(self):
        self.value=16
        self.anim = Animation(jarum_value=self.value*17.5, duration=1)
        self.anim.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.anim = Animation(jarum_value=self.value*17.5, duration=2)
        self.anim.start(self)
    def show_value(self,data):
        self.anim = Animation(jarum_value=self.value*17.5,duration=1,t="linear")
        self.anim.start(self)
    def reset(self):
        self.jarum_value = 0
        self.value = 0

class My(App):
    def build(self):
        return DashTacho()


if __name__=="__main__":
    My().run()