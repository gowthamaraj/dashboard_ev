from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import serial

ser = serial.Serial('COM3',9600,timeout=1)
from time import strftime


class ClockApp(App):
    

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        self.root.ids.time.text = str(ser.readline().decode('ascii'))


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
