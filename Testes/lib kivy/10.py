# Clock

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        self.cont = 0
        self.lbl = Label()
        Clock.schedule_interval(self.tick, 1)
        return self.lbl

    def tick(self, dt):
        self.cont += 1
        self.lbl.text = f"{self.cont}"
    
MyApp().run()
