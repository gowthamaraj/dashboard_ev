from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from random import random


class RootWidget(GridLayout):
    pass

class RevElectricApp(App):
    def build(self):
        return RootWidget()
    
    def on_start(self):
        Clock.schedule_interval(self.update, 0.3)

    def update(self, nap):
        x=int(random()*100)
        self.root.ids.speed.text = str( str(x) +' m/s')
        
        t1="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.t1.text = t1
        
        t2="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.t2.text = t2
        
        t3="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.t3.text = t3
        
        t4="[b][color=f47141]Temperature [/color][/b][color=f47141] \n [size=40] %d [/size] [/color]" % (x)
        self.root.ids.t4.text = t4
        
        soc=int(random()*100)
        self.root.ids.soc.value =soc
        soc=str(int(random()*100))+'%'
        self.root.ids.soc_value.text =str(soc)



if __name__ == "__main__":
    RevElectricApp().run()
    
    
    
    
    
    
    
    
