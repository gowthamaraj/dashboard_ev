from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from random import random



            
class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")

class MainApp(App):
    
    def build(self):
        return presentation
    def on_start(self):
        Clock.schedule_interval(self.update, 0.3)

    def update(self, nap):
        x=int(random()*100)
        self.root.ids.screen1.ids.speed.text = str( str(x) +' m/s')
        
        t1="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.screen1.ids.t1.text = t1
        
        t2="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.screen1.ids.t2.text = t2
        
        t3="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.screen1.ids.t3.text = t3
        
        t4="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.screen1.ids.t4.text = t4
        
        soc=int(random()*100)
        self.root.ids.screen1.ids.soc.value =soc
        soc=str(int(random()*100))+'%'
        self.root.ids.screen1.ids.soc_value.text =str(soc)

if __name__ == "__main__":
    MainApp().run()
        
    
